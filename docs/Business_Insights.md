# Customer Profitability & Revenue Leakage Intelligence

**Project type:** Data Analyst portfolio project  
**Tools:** Python, Pandas, MySQL, Power BI  
**Dataset:** Sample Superstore sales data

## 1. Business Objective

This project analyzes sales, profit, customer performance, product performance, regional results, and discount patterns to identify areas that may be reducing profitability and recommend actions for further investigation.

## 2. Key Performance Indicators

The current Power BI dashboard displays the following approximate values. Recheck them against the final CSV and SQL results before publishing.

| KPI | Current dashboard value |
|---|---:|
| Total Sales | Approximately $2.30M |
| Total Profit | Approximately $286.40K |
| Profit Margin | Approximately 12.47% |
| Total Orders | Approximately 5K |

- **Total Sales:** Sum of sales for records included in the analysis.
- **Total Profit:** Sum of profit for those records.
- **Profit Margin:** Total Profit divided by Total Sales, multiplied by 100.
- **Total Orders:** Number of distinct order IDs, not the number of product rows.

> **Data validation note:** Earlier checks showed differences between row counts and KPI totals in different versions of the data. Reconcile the CSV, SQL table, and Power BI model using the same source data and filters. Do not delete rows just to match a benchmark total.

## 3. Key Findings

### 3.1 Product profitability

The current analysis indicates that **Tables** and **Bookcases** are loss-making sub-categories. **Supplies** also appears to generate a smaller loss, while **Fasteners** is profitable.

**Business implication:** High sales do not automatically mean high profit. Product costs, discount levels, shipping costs, returns, and pricing may affect profitability.

**Recommended action:** Review Tables, Bookcases, and Supplies by discount, region, and shipping mode before changing prices or discontinuing products.

### 3.2 Regional performance

The current dashboard indicates that the **West** region generates the highest profit, while **Central** has the lowest profit among the four regions.

**Business implication:** Regional performance may vary because of product mix, customer mix, discounting, shipping costs, or sales volume.

**Recommended action:** Compare Central and West by category, sub-category, discount, and shipping mode. Identify which differences explain the profit gap before recommending changes.

### 3.3 Discount patterns

The current analysis shows that the **70% discount band** has substantial negative total profit, while the **0% discount band** contributes strong positive profit.

**Business implication:** Deep discounts may be associated with lower profitability for some products or orders. This is an association in the observed data, not proof that discounts alone caused the losses.

**Recommended action:** Review high-discount orders and calculate profit margin by discount band, product, and region. Consider approval rules or minimum-margin checks for large discounts, then evaluate their impact using order-level data.

### 3.4 Customer profitability

The dashboard compares customers by total profit. A Top 10 customer view helps decision-makers focus on customers contributing the most profit.

**Recommended action:** Review both high-profit and loss-making customers. For customers with negative profit, inspect order mix, discount levels, product mix, and shipping costs before changing account strategy.

### 3.5 Monthly sales and profit trend

The monthly trend should be sorted by a real date column (such as the first day of each month), not alphabetically by a text label. Investigate any unusually large spike by checking the underlying orders for that month.

**Recommended action:** Validate date sorting and inspect the month with the largest spike before describing it as a business trend.

## 4. Recommended Business Actions

1. **Investigate loss-making sub-categories:** Start with Tables, Bookcases, and Supplies.
2. **Review deep discounts:** Inspect high-discount orders with negative profit; do not assume every discount is harmful.
3. **Compare regional drivers:** Use West and Central as a starting point for product-mix and discount comparisons.
4. **Monitor customer profitability:** Track profit and margin by customer, not sales alone.
5. **Validate unusual monthly results:** Check order dates and transaction-level records behind spikes.
6. **Set up recurring monitoring:** Refresh the dashboard regularly and track sales, profit, margin, and loss-making orders.

## 5. Limitations

- This is a descriptive analysis of the supplied Sample Superstore dataset.
- Patterns and correlations do not, by themselves, establish causation.
- Findings depend on the exact dataset version, cleaning steps, and Power BI filters.
- Reconcile dashboard KPIs and findings with final CSV and SQL outputs before publishing.

## 6. Conclusion

The analysis provides a starting point for improving profitability by investigating loss-making product groups, regional differences, discount patterns, and customer-level profit. The next step is to validate these patterns at order level and test targeted actions while monitoring their impact on profit margin.

## Reproducibility

Run from the project root:

```bash
python python/data_quality_check.py
python python/analyze_superstore.py
```

Expected input file: `data/raw/Sample - Superstore.csv`

If your CSV has a different filename, pass its path as an argument:

```bash
python python/data_quality_check.py "data/raw/your_file.csv"
python python/analyze_superstore.py "data/raw/your_file.csv"
```
