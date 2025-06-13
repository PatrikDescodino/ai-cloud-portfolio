import pandas as pd
import numpy as np
import datetime as dt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def generate_sample_data():
    n_rows = 1000

    customer_ids = list(range(1, n_rows + 1))
    transaction_types = np.random.choice(['deposit', 'withdrawal', 'transfer'], size=n_rows)
    amounts = np.random.randint(1,50000, size=n_rows)

    start_date = pd.to_datetime('2023-01-01')
    end_date = pd.to_datetime('2024-12-31')
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    random_indices = np.random.randint(0, len(date_range), size=n_rows)
    transaction_dates = date_range[random_indices]

    account_balances = np.random.randint(0,100000, size=n_rows)

    df = pd.DataFrame({
        'customer_id': customer_ids, 
        'transaction_date': transaction_dates, 
        'amount': amounts, 
        'transaction_type': transaction_types,
        'account_balance': account_balances
    })

    return df

# ========== ČÁST 2: ML MODEL PRO ÚVĚROVÉ RIZIKO ==========
data = generate_sample_data()

def create_risk_label(df):
    high_amount = df['amount'] > 30000
    low_balance = df['account_balance'] < 10000
    withdrawal = df['transaction_type'] == 'withdrawal'
    
    risk_score = high_amount.astype(int) + low_balance.astype(int) + withdrawal.astype(int)
    
    is_risky = risk_score >= 2
    
    return is_risky.astype(int)

# ========== ČÁST 3: ML MODEL ==========

# Features (X) - co používáme pro predikci
X = data[['amount', 'account_balance']]  # Začneme jen s číselnými

# Target (y) - co chceme předpovědět  
y = data['is_risky']

print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")