CREATE DATABASE IF NOT EXISTS stock_investments;

USE stock_investments;

CREATE TABLE IF NOT EXISTS investors (
    investor_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS transactions (
    txn_id INT AUTO_INCREMENT PRIMARY KEY,
    investor_id INT,
    stock_symbol VARCHAR(10),
    txn_type VARCHAR(10),
    quantity INT,
    price DECIMAL(10, 2),
    txn_date DATE,
    FOREIGN KEY (investor_id) REFERENCES investors(investor_id)
);

CREATE TABLE IF NOT EXISTS portfolio (
    investor_id INT PRIMARY KEY,
    total_investment DECIMAL(15, 2),
    total_stocks INT,
    risk_score DECIMAL(5, 2)
);
