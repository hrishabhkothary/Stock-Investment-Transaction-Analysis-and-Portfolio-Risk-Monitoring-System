from sqlalchemy import text
from db_config import get_engine

def seed_investors():
    engine = get_engine()
    sql = """
    INSERT IGNORE INTO investors (investor_id, name) VALUES
        (1001, 'Investor One'),
        (1002, 'Investor Two'),
        (1003, 'Investor Three'),
        (1004, 'Investor Four'),
        (1005, 'Investor Five');
    """
    with engine.connect() as conn:
        conn.execute(text(sql))
        print("✔️ Investors seeded successfully!")

if __name__ == "__main__":
    seed_investors()
