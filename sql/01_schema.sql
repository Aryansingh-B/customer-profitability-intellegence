-- Project: Customer Profitability & Revenue Leakage Intelligence

CREATE DATABASE IF NOT EXISTS customer_profitability;

USE customer_profitability;

-- Inspect column names and data types
DESCRIBE `sample - superstore`;

-- Previewing the imported records
SELECT *
FROM `sample - superstore`
LIMIT 10;

-- Checking total number of rows
SELECT COUNT(*) AS total_rows
FROM `sample - superstore`;

-- Checking for missing values in important columns
SELECT 
    SUM(Sales IS NULL) AS missing_sales,
    SUM(Profit IS NULL) AS missing_profit,
    SUM(Discount IS NULL) AS missing_discount,
    SUM(`Order ID` IS NULL) AS missing_order_ids
FROM `sample - superstore`;