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
├── constants.py
├── seed_investors.py
├── load_transactions.py
├── update_portfolio.py
├── analyze.py
├── master_etl.py
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

   ## 🚀 Run the entire ETL pipeline:


python master_etl.py

This will:

-Generate new dummy transactions

-Seed investors (safe for re-runs)

-Load transactions to MySQL

-Update portfolio risk scores

-Show analysis plots



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
📌 What pseudo_realtime.py does:

In this kind of stock/transactions pipeline, pseudo_realtime.py is:

1. A simulation script.

2. It mimics how new transactions arrive in “near-real time.”

3. It continuously appends new rows to your transactions table (or your CSV) every few seconds/minutes.

4. It calls the same DB connection (db_config.py) to push rows one by one or in small batches.

- So it simulates a real trading feed — think:

   'Streaming new transactions → Insert → Portfolio gets updated → Reports refresh'


***********************************************************************************************************************************************************************************************************


✅ When should we run pseudo_realtime.py?

We run it:

1️⃣ AFTER your main tables exist.

So, run:

1. create_tables.sql

2. seed_investors.py

3. load_transactions.py

4. update_portfolio.py (or master_etl.py)


2️⃣ Then run pseudo_realtime.py in parallel or in another terminal:

'python pseudo_realtime.py'


3️⃣ It will keep inserting new transactions in loop (or on a schedule).


4️⃣ You can then run 'update_portfolio.py' again periodically or make it watch for new data — so your portfolio risk stays up to date.


***********************************************************************************************************************************************************************************************************

✅ This is how we simulate:



Batch mode: load_transactions.py inserts 10,000 rows once.

Pseudo real-time: pseudo_realtime.py keeps adding rows forever.

📌 When do we stop it?

When you’re done demonstrating or testing:

Just Ctrl + C in the terminal to stop it.

The data stays in MySQL.


***********************************************************************************************************************************************************************************************************

✅ Typical run order (FULL)

Batch mode:


mysql -u root -p
SOURCE create_tables.sql;
python seed_investors.py
python generate_dummy_data.py
python load_transactions.py
python update_portfolio.py
python analyze.py


Pseudo real-time mode:

# In Terminal 1
python pseudo_realtime.py

# In Terminal 2 (periodically)
python update_portfolio.py

# Or watch your DB in real-time!


***********************************************************************************************************************************************************************************************************

✅ Where does db_config.py fit in?

➡️ pseudo_realtime.py also says:

'from db_config import get_engine'

   So it reuses the same DB connection.

👉 pseudo_realtime.py NEEDS:

-investors to exist

-transactions to exist

-investor_id values in the dummy rows to match seeded IDs.


***********************************************************************************************************************************************************************************************************

✅ How to test it

# 1. Make sure investors table has correct IDs:
      SELECT * FROM investors;

# 2. Make sure your pseudo_realtime.py uses only those IDs:
      INVESTOR_IDS = [1001, 1002, 1003, 1004, 1005]

# 3. Run it:
      python pseudo_realtime.py


Check your transactions table:

      SELECT COUNT(*) FROM transactions;

      The count should keep going up.

✅ Wrap up:

pseudo_realtime.py → For demo, stress test, simulating live feed.

Run order:

Always AFTER schema + initial seed + first batch load.


✅ How this works

Runs forever until you Ctrl + C.

Every 3 seconds, generates 1 new random transaction.

Uses only investor IDs 1001–1005 → So FK always valid.

Uses db_config.py → same connection, so always in sync.

✅ How to run

1️⃣ Make sure:

create_tables.sql run ✅

seed_investors.py run ✅

transactions table exists ✅

2️⃣ Run your batch:

python load_transactions.py

3️⃣ Now run:

python pseudo_realtime.py

4️⃣ Open a second terminal, run:

python update_portfolio.py

or re-run analyze.py — you’ll see new live data!

✅ Stop anytime

Ctrl + C in the terminal → the script stops adding new rows.











