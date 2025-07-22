import pandas as pd
from db_config import get_engine

def update_portfolios():
    engine = get_engine()

    query = """
    SELECT 
        investor_id,
        stock_symbol,
        SUM(CASE WHEN txn_type = 'BUY' THEN quantity ELSE -quantity END) AS total_quantity,
        SUM(CASE WHEN txn_type = 'BUY' THEN quantity * price ELSE 0 END) / NULLIF(SUM(CASE WHEN txn_type = 'BUY' THEN quantity ELSE 0 END), 0) AS avg_buy_price
    FROM transactions
    GROUP BY investor_id, stock_symbol;
    """

    df = pd.read_sql(query, engine)
    df['risk_score'] = df['total_quantity'].apply(lambda x: 50 if x > 100 else 20)
    df['last_updated'] = pd.Timestamp.now()

    df.to_sql('portfolios', con=engine, if_exists='replace', index=False)
    print("Portfolio updated successfully.")

if __name__ == "__main__":
    update_portfolios()
