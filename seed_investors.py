from sqlalchemy import text
from db_config import get_engine
from constants import INVESTOR_IDS

def seed_investors():
    engine = get_engine()
    values = ",\n".join(
        f"({id}, 'Investor {id}')" for id in INVESTOR_IDS
    )
    sql = f"""
    INSERT IGNORE INTO investors (investor_id, name) VALUES
    {values};
    """
    with engine.connect() as conn:
        conn.execute(text(sql))
        print(f"✔️ Investors seeded successfully: {INVESTOR_IDS}")

if __name__ == "__main__":
    seed_investors()
