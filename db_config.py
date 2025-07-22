from sqlalchemy import create_engine

def get_engine():
    username = 'root'
    password = 'yourpassword'
    host = 'localhost'
    port = '3306'
    database = 'stock_investments'

    engine_url = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
    engine = create_engine(engine_url)
    return engine
