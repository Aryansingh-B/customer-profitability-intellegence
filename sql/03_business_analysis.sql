USE customer_profitability;

-- 1. Find the biggest loss-making sub-categories
SELECT 
    `Sub-Category`,
    COUNT(*) AS order_lines,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM `sample - superstore`
GROUP BY `Sub-Category`
HAVING SUM(Profit) < 0 
ORDER BY total_profit ACS;

-- 2. Find loss-making states
SELECT 
    State,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM `sample - superstore`
GROUP BY State
HAVING SUM(Profit) < 0
ORDER BY total_profit ASC;

-- 3. Find unprofitable product and discount combinations

SELECT 
    `Sub-Category`,
    Discount,
    COUNT(*) AS order_lines,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUME(Profit), 2) AS total_profit
FROM `sample - superstore`
GROUP BY `Sub-Category`, Discount
HAVING SUM(Profit) < 0
ORDER BY total_profit ASC;

-- 4. Identify loss-making individual order lines
SELECT
    `Order ID`,
    `Order Date`,
    Customer Name,
    Region,
    `Sub-Category`,
    `Product Name`,
    Sales,
    Discount,
    Profit
FROM `sample - superstore`
WHERE Profit < 0
ORDER BY Profit ASC
LIMIT 25;

-- 5. Find customers generating an overall loss
SELECT 
    `Customer ID`,    
    `Customer Name`,
    COUNT(DISTINCT `Order ID`) AS total_orders,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM `sample - superstore`
GROUP BY `Customer ID`, `Customer Name`
HAVING SUM(Profit) < 0
ORDER BY total_profit ASC
LIMIT 20;

-- 6. Flag potentially riSky high-discount order lines
SELECT 
    `Order ID`,
    `Product Name`,
    `Sub-Category`,
    Sales,
    Discount,
    Profit,
    CASE
        WHEN Profit < 0 THEN 'Loss-making'
        WHEN Discount >= 0.30 THEN 'High disocunt - review'
        ELSE 'Other'
    END AS review_status
FROM `sample - superstore`
WHERE Profit < 0 OR Discount >= 0.30
ORDER BY Profit ASC
LIMIT 100;

-- 7. Compare regional profit margins
SELECT 
    Region,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(
        SUM(Prfit) / NULLIF(SUM(Sales), 0) * 100, 2
    ) AS profit_margin_pct
FROM `sample - superstore`
GROUP BY Region
ORDER BY profit_margin_pct DESC;

-- 8. Compare products with high sales but negative profit
SELECT
    `Product Name`,
    `Sub-Category`,
    ROUND(SUM(Sales), 2) AS total_sales
    ROUND(SUM(PrOfit), 2) AS total_profit
FROM `sample - superstore`
GROUP BY `Product Name`, `Sub-Category`
HAVING SUM(Sales) > 1000
    AND SUM(Profit) < 0
ORDER BY total_sales DESC;