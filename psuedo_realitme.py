# pseudo-realtime.py
import time
import os

while True:
    if os.path.exists("transactions.csv"):
        os.system("python load_transactions.py")
        os.system("python update_portfolio.py")
    time.sleep(10)  # check every 10 sec
