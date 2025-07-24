# pseudo-realtime.py
import random
import time
from datetime import datetime
from sqlalchemy import text
from db_config import get_engine

# Same investor IDs as your seeded investors
INVESTOR_IDS = [1001, 1002, 1003, 1004, 1005]
STOCK_SYMBOLS = ['AAPL', 'TSLA', 'MSFT', 'GOOG', 'AMZN', 'NFLX', 'META']
TXN_TYPES = ['BUY', 'SELL']

def generate_transaction():
    """Generate one random transaction row"""
    investor_id = random.choice(INVESTOR_IDS)
    stock_symbol = random.choice(STOCK_SYMBOLS)
    txn_type = random.choice(TXN_TYPES)
    quantity = random.randint(1, 100)
    price = round(random.uniform(100, 1500), 2)
    txn_date = datetime.now().strftime('%Y-%m-%d')

    return (investor_id, stock_symbol, txn_type, quantity, price, txn_date)

def insert_transaction(engine, txn):
    """Insert single transaction"""
    sql = """
        INSERT INTO transactions (investor_id, stock_symbol, txn_type, quantity, price, txn_date)
        VALUES (:investor_id, :stock_symbol, :txn_type, :quantity, :price, :txn_date);
    """
    with engine.connect() as conn:
        conn.execute(
            text(sql),
            {
                'investor_id': txn[0],
                'stock_symbol': txn[1],
                'txn_type': txn[2],
                'quantity': txn[3],
                'price': txn[4],
                'txn_date': txn[5]
            }
        )

if __name__ == "__main__":
    engine = get_engine()
    print("✅ Starting pseudo-realtime transaction feed...")
    try:
        while True:
            txn = generate_transaction()
            insert_transaction(engine, txn)
            print(f"✅ Inserted: {txn} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            time.sleep(3)  # Wait 3 seconds before next transaction
    except KeyboardInterrupt:
        print("\n🛑 Stopped pseudo-realtime feed.")

