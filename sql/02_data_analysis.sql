USE customer_profitability;

-- 1. Overall business KIPs
SELECT 
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(
        SUM(Profit) / NULLIF(SUM(Sales, 0) * 100, 2
    ) AS profit_margin_pct;
    COUNT(DISTINCT `Order ID`) AS total_orders,
    COUNT(DISTINCT 'Customer ID') AS unique_customers
FROM `sample - superstore`;

-- 2. Sales and profit by category
SELECT 
    Category,
    ROUND(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(
        SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2
    ) AS profIt_margin_pct
FROM `sample - superstore`
GROUP BY Category
ORDER BY total_profit DESC;

-- 3. Sub-categories with losses
SELECT 
    `Sub-Category`,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Proft), 2) AS total_profit
FROM `sample - superstore`
GROUP BY 'Sub-Category'
HAVING SUM(Profit) < 0
ORDER BY total_profit ASC;

-- 4. Regional performance
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(
        SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2 
    ) AS profit_margin_pct
FROM `sample - superstore`
GROUP BY Region
ORDER BY total_profit DESC;

-- 5. Profitability by discount level
SELECT 
    Discount,
    COUNT(*) AS order_lines,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(
        SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2
    ) AS profit_margin_pct
FROM `sample - superstore`
GROUP BY Discount
ORDER BY Discount

-- 6. Top 10 customers by profit
SELECT 
    `Customer ID`,
    `Customer Name`,
    COUNT(DISTINCT 'Order ID') AS total_orders,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM `sample - superstore`
GROUP BY `Customer ID`, `Customer Name`
ORDER BY total_profit DESC
LIMIT 10;

-- 7. Top 10 products by sales
SELECT
    `Product Name`,
    SUM(Quantity) AS units_sold,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM `sample - superstore`
GROUP BY `Product Name`
ORDER BY total_sales DESC
LIMIT 10;

-- 8. Profitability by shipping mode
SELECT 
    `Ship Mode`,
    COUNT(DISTINCT `Order ID`) AS total_orders,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM `sample - superstore`
GROUP BY `Ship Mode`
ORDER BY total_profit DESC;

-- 9. Monthly sales and profit trend
SELECT
    DATE_FORMAT(`Order Date`, '%Y-%m') AS order_month,
    ROUND(SUM(Sales), 2) AS monthly_sales,
    ROUND(SUM(Profit), 2) AS monthly_profit
FROM `sample - superstore`
GROUP BY DATE_FORMAT(`Order Date`, '%Y-%m')
ORDER BY order_month;
