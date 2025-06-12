# TEST NA RANDOM DATUM 
"""
print("Test 3: Random datum")

start_date = pd.to_datetime('2023-01-01')
end_date = pd.to_datetime('2024-12-31')

date_range = pd.date_range(start=start_date, end=end_date, freq='D')
print(f"Máme {len(date_range)} dní na výběr")

# TOHLE JE KLÍČ - vybereme náhodné INDEXY místo přímo datumů
random_indices = np.random.randint(0, len(date_range), size=10)
random_dates = date_range[random_indices]

clean_dates = [date.date() for date in random_dates]
print("10 náhodných datumů:")
print(clean_dates)
"""

# TEST NA RANDOM ČÍSLA
"""
print("Test 1: Random čísla")
random_amounts = np.random.randint(100,50000, size=5)
print(random_amounts)
"""

# TEST NA RANDOM MOŽNOSTI
"""
print("Test 2: Random výběr z možností")
options= ['deposit', 'withdrawal', 'transfer']
random_choice = np.random.choice(options, size=5)

print(random_choice)
"""

