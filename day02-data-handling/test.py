import pandas as pd
import numpy as np
import datetime as dt

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

