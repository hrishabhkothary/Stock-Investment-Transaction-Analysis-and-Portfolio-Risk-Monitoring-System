import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from db_config import get_engine

def portfolio_summary():
    engine = get_engine()
    query = """
    SELECT investor_id, stock_symbol, total_quantity, avg_buy_price, risk_score
    FROM portfolios;
    """
    df = pd.read_sql(query, engine)
    print(df.head())

    sns.barplot(x='stock_symbol', y='total_quantity', hue='investor_id', data=df)
    plt.title('Stock Holdings by Investor')
    plt.show()

if __name__ == "__main__":
    portfolio_summary()
