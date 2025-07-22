# 📈 Stock Investment Transaction Analysis and Portfolio Risk Monitoring System

# Industrial-Grade Electronic Stock Investment Transaction & Portfolio Management System:

✅ What it basically does
This project simulates a complete electronic stock investment system for financial institutions and retail brokers.

**It does three main things:**

1️. Simulates real-time stock transactions:
It generates large, realistic trade data — thousands of buys and sells — for multiple investors and stocks.

2️. Performs ETL and data warehousing:
It ingests these transactions, stores them in a relational database (MySQL), and runs advanced SQL logic (joins, subqueries) to aggregate data into investor portfolios.

3️. Provides insights and monitoring:
It calculates each investor's total holdings, average buy prices, and assigns basic risk scores. It visualizes this data to help detect unusual trading activity or concentrated risk.

**How it may help institutions:**

1. Retail brokerages & fintech startups:
Can use similar pipelines to process daily buy/sell orders, calculate customer holdings, and keep portfolios up-to-date.

2. Investment banks:
Can adapt the logic to detect high-risk or unusual trades, helping compliance and risk management teams flag suspicious activity.

3. Data analysts & quants:
Can extend this pipeline for deeper portfolio performance analysis, profit/loss reporting, or trade pattern detection.

4. Automation benefit:
The system runs in batch mode (hourly or daily) or can be extended for real-time, just like production-grade trading systems.



✅ Technologies Used & How:

| 📌 **Technology**                                  | 🔍 **What it’s used for**                                                                                     |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Python**                                         | Core scripting language for ETL (Extract, Transform, Load), data generation, analytics, automation            |
| **Python Libraries (pandas, seaborn, matplotlib)** | 'pandas' handles CSVs & DB data; `seaborn` & `matplotlib` visualize investor portfolios                       |
| **SQLAlchemy + PyMySQL**                           | Python ORM + MySQL connector: they connect Python code to MySQL securely                                      |
| **MySQL**                                          | Relational database to store transactions & portfolios; handles advanced 'JOIN's & 'SUBQUERY' operations      |
| **SQL Joins & Subqueries**                         | Used to aggregate raw trade data into investor-level summaries (total holdings, average prices, risk scoring) |
| **Batch Scheduling (cron)**                        | Automates ETL to run periodically, simulating real-time trade settlement pipelines                            |
| **Real-Time Option (File Watcher or Kafka)**       | Extends the batch process to detect new trades and process instantly                                          |


**Key Industrial Features:**
✔ Big data simulation: Generates 10,000+ realistic trade records.
✔ Production-style ETL: Structured pipelines for ingestion, transformation, and storage.
✔ Data integrity: Uses foreign keys & schema design to enforce consistency.
✔ SQL optimization: Leverages JOIN and CASE WHEN for conditional calculations.
✔ Risk scoring: Demonstrates how institutions may flag large or unusual positions.
✔ Automation-ready: Runs in batch or real-time.
✔ Visual dashboard: Investors' positions are visualized, helping detect trends or anomalies.



**HOW TO RUN:**

1. Clone this repo: git clone https://github.com/hrishabhkothary/Stock-Investment-Transaction-Analysis-and-Portfolio-Risk-Monitoring-System.git
2. The final Project tree should look like:
   
StockInvestmentProject/
│
├── db_config.py
├── create_tables.sql
├── generate_dummy_data.py
├── transactions.csv
├── load_transactions.py
├── update_portfolio.py
├── analyze.py
├── psuedo_realtime.py
├── requirements.txt
├── .gitignore
└── README.md

3. Install Python packages(Terminal):
   
   pip install -r requirements.txt

4. Setup MySQL DB:
   Open terminal:
   
   mysql -u root -p < create_tables.sql
   
   **This:**
   Creates your stock_investments DB
   Creates tables: investors, transactions, portfolios.

5. Add a dummy CSV (one time)
   
   Make sure transactions.csv exists(already existing in folder).
   
   OR Run,
   
   python generate_dummy_data.py
   
   This will create a big file (transactions.csv with 10,000+ rows).

6. Load transactions into DB:
   
   Run,
   
   python load_transactions.py

7. Update portfolios:
    
   Run,
   
   python update_portfolio.py

   **This:**
     Runs a JOIN & subquery.
     Calculates total quantity, average buy price, risk score.
     Stores it in portfolios.


8. Analyze and Visualize:
    
   Run,
   
   python analyze.py

   **This:**
   
    Pulls portfolios data.
    Plots a bar chart with seaborn.
    Opens a window so you see who owns what stocks.



**✅Batch Mode**

In Batch Mode, you run the ETL automatically at intervals (like hourly).

How to do it?

1. Open terminal:
   
Run,

crontab -e

2️. Add:


0 * * * * /usr/bin/python3 /path/to/StockInvestmentProject/load_transactions.py    (# Run loader every hour)


5 * * * * /usr/bin/python3 /path/to/StockInvestmentProject/update_portfolio.py      (# Run updater every hour, 5 mins later)

**This:**

Loads new transactions hourly.
Updates portfolios hourly.



**✅Real-Time Mode**
Batch means “process all at once, on schedule”.
Real-time means “process each new trade immediately”.

A simple version for real-time:

-Use watchdog (a Python library) to monitor a folder for a new CSV.

-Or connect to a message broker (Kafka, RabbitMQ, etc).

Example simple loop:

# pseudo-realtime.py

import time

import os

while True:

    if os.path.exists("transactions.csv"):
        os.system("python load_transactions.py")
        os.system("python update_portfolio.py")
    time.sleep(10)  # check every 10 sec
    

   **OR for Kafka-style:**
   

     -Send each new trade as a message.

     -Have a Python consumer that runs update_portfolio.py instantly.












