import pandas as pd
from db_config import get_engine

def load_transactions(file_path):
    df = pd.read_csv(file_path)
    engine = get_engine()
    df.to_sql('transactions', con=engine, if_exists='append', index=False)
    print(f"{len(df)} transactions loaded successfully.")

if __name__ == "__main__":
    load_transactions('transactions.csv')
