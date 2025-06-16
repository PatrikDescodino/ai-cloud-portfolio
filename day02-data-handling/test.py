import pandas as pd
import numpy as np
import datetime as dt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def generate_sample_data():
    n_rows = 10000
    
    customer_ids = list(range(1, n_rows + 1))
    transaction_types = np.random.choice(['deposit', 'withdrawal', 'transfer'], size=n_rows)
    amounts = np.random.randint(1, 50000, size=n_rows)
    
    start_date = pd.to_datetime('2023-01-01')
    end_date = pd.to_datetime('2024-12-31')
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    random_indices = np.random.randint(0, len(date_range), size=n_rows)
    transaction_dates = date_range[random_indices]
    
    account_balances = np.random.randint(0, 100000, size=n_rows)
    
    df = pd.DataFrame({
        'customer_id': customer_ids,
        'transaction_date': transaction_dates,
        'amount': amounts,
        'transaction_type': transaction_types,
        'account_balance': account_balances
    })
    
    return df

def create_risk_label(df):
    high_amount = df['amount'] > 30000
    low_balance = df['account_balance'] < 10000
    withdrawal = df['transaction_type'] == 'withdrawal'
    
    risk_score = high_amount.astype(int) + low_balance.astype(int) + withdrawal.astype(int)
    is_risky = risk_score >= 2
    
    return is_risky.astype(int)

# ML MODEL
data = generate_sample_data()
data['is_risky'] = create_risk_label(data)

transaction_dummies = pd.get_dummies(data['transaction_type'], prefix='trans')
data['amount_to_balance_ratio'] = data['amount'] / (data['account_balance'] + 1)  # +1 proti dělení nulou
data['is_large_transaction'] = (data['amount'] > data['amount'].quantile(0.8)).astype(int)
data['is_low_balance'] = (data['account_balance'] < data['account_balance'].quantile(0.2)).astype(int)


X = pd.concat([
    data[['amount', 'account_balance', 'amount_to_balance_ratio', 'is_large_transaction', 'is_low_balance']],
    transaction_dummies
], axis=1)

y = data['is_risky']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model accuracy: {accuracy:.2f} ({accuracy*100:.1f}%)")

print("\n" + "="*50)
print("🏦 ČNB RISK ASSESSMENT MODEL")
print("="*50)
print(f"✅ Model accuracy: {accuracy:.1%}")
print(f"✅ Testováno na: {len(y_test)} klientech")
print(f"✅ Správně klasifikováno: {int(accuracy * len(y_test))} klientů")
print(f"✅ Chybná klasifikace: {len(y_test) - int(accuracy * len(y_test))} klientů")

risky_clients = sum(y_test)
safe_clients = len(y_test) - risky_clients
print(f"📊 Rizikových klientů: {risky_clients}")
print(f"📊 Bezpečných klientů: {safe_clients}")