import pandas as pd
import random
from datetime import datetime, timedelta

def generate_transactions(num_records=10000):
    investor_ids = [1001, 1002, 1003, 1004, 1005]
    stock_symbols = ['AAPL', 'TSLA', 'MSFT', 'GOOG', 'AMZN', 'NFLX', 'META']
    txn_types = ['BUY', 'SELL']

    transactions = []

    for _ in range(num_records):
        investor_id = random.choice(investor_ids)
        stock_symbol = random.choice(stock_symbols)
        txn_type = random.choice(txn_types)
        quantity = random.randint(1, 500)
        price = round(random.uniform(50, 1500), 2)
        txn_date = datetime.now() - timedelta(days=random.randint(0, 365))

        transactions.append([
            investor_id, stock_symbol, txn_type, quantity, price, txn_date.strftime('%Y-%m-%d')
        ])

    df = pd.DataFrame(transactions, columns=[
        'investor_id', 'stock_symbol', 'txn_type', 'quantity', 'price', 'txn_date'
    ])

    df.to_csv('transactions.csv', index=False)
    print(f"Generated {num_records} dummy transactions in transactions.csv")

if __name__ == "__main__":
    generate_transactions()
