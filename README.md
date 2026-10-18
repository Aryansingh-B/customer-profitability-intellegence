# Customer Profitability & Revenue Leakage Intelligence

An Excel-based business analytics project using the Sample Superstore dataset to explore sales performance, profitability, discount impact, and loss-making product areas.

## Dashboard features
- KPI cards: Total Sales, Total Profit, Profit Margin, Unique Orders
- Monthly sales and profit trend
- Profit by product category
- Profit by region# Customer Profitability & Revenue Leakage Intelligence

A business-focused data analytics portfolio project built with the Sample Superstore dataset. It examines sales, profit, margins, product and regional performance, customer profitability, and discount patterns to identify areas that merit further investigation.

> **Project focus:** descriptive analytics and decision support. Findings highlight associations and investigation priorities; they do not establish causation or prove realized business savings.

## 1. Project Overview

The project brings together spreadsheet analysis, SQL querying, Python-based data checks and summaries, Jupyter notebooks, and dashboard reporting. The goal is to help a business user look beyond revenue and understand where profit is being earned or lost.

## 2. Business Problem Statement

Sales totals alone do not show whether orders, products, customers, or regions are profitable. The business needs a consistent view of sales and profit, plus a way to investigate loss-making sub-categories and discount patterns before changing pricing or sales policies.

## 3. Dataset Overview & Source

- **Dataset:** Sample Superstore CSV supplied for this project (`Sample - Superstore.csv`).
- **Observed shape:** 9,994 rows and 21 columns in the reviewed CSV.
- **Date coverage:** January 3, 2014 – December 30, 2017.
- **Main fields:** Order ID, Order Date, Ship Date, Customer ID/Name, Segment, Region, Category, Sub-Category, Product Name, Sales, Quantity, Discount, and Profit.
- **Source/licensing:** the exact original public source and redistribution terms were not verified from the supplied file. Check the dataset's license and terms before redistributing it. The raw CSV is intentionally excluded from this repository; place your authorized copy in `data/raw/`.

## 4. Project Objectives

- Measure total sales, total profit, profit margin, and distinct orders.
- Compare profitability across categories, sub-categories, regions, and customers.
- Examine the relationship between discount levels and profit.
- Review monthly sales and profit trends.
- Produce repeatable data-quality checks and summary outputs.
- Translate descriptive findings into specific questions and actions for business review.

## 5. Business Questions

1. What are total sales, total profit, profit margin, and distinct orders?
2. Which categories and sub-categories contribute most and least to profit?
3. Which regions generate the highest and lowest profit?
4. Which discount levels coincide with negative aggregate profit?
5. How does profitability vary by customer and product?
6. Are there unusual monthly results that should be validated against the underlying orders?

## 6. Tools & Technologies

| Tool | Use in the project |
|---|---|
| Microsoft Excel | KPI summary and dashboard workbook |
| SQL / MySQL | Relational querying and business analysis (`sql/`) |
| Python | Data-quality checks and repeatable summary generation |
| Pandas | CSV loading, grouping, aggregation, and data checks |
| Jupyter Notebook | Cleaning, exploratory analysis, and customer-profitability analysis |
| Power BI | Interactive executive overview and visual analysis |
| Git / GitHub | Version control and portfolio presentation |

## 7. Methodology / Workflow

1. **Load and validate:** inspect row/column counts, missing values, duplicate rows, date parsing, numeric fields, and key identifiers.
2. **Prepare and explore:** review sales and profit distributions and group results by product, category, region, customer, and discount.
3. **Analyze in SQL:** use the SQL scripts for schema setup and business-focused queries.
4. **Generate Python outputs:** create profitability summaries and a Markdown summary report from the selected CSV.
5. **Visualize:** review KPI cards, category and regional comparisons, customer profitability, and time trends in Excel and Power BI.
6. **Recommend:** use observed patterns to prioritize further investigation, while validating results against the same source rows and filters.

## 8. Key Performance Indicators (KPIs)

The figures below were recalculated from the reviewed 9,994-row CSV using Pandas. They describe that exact file and may differ if another version or different filters are used.

| KPI | Result | Definition |
|---|---:|---|
| Total Sales | **$2,297,200.86** | Sum of Sales |
| Total Profit | **$286,397.02** | Sum of Profit |
| Profit Margin | **12.47%** | Total Profit ÷ Total Sales × 100 |
| Distinct Orders | **5,009** | Unique Order ID count |
| Distinct Customers | **793** | Unique Customer ID count |
| Loss-making rows | **1,871** | Rows with Profit below zero; not the same as distinct loss-making orders |

**Validation note:** use the same CSV, date range, filters, and row-level definitions when comparing these figures with Excel, SQL, and Power BI. Do not delete rows simply to match a benchmark.

## 9. Key Insights & Findings

These findings are calculated from the reviewed CSV, not inferred from dashboard appearance alone.

### Category and sub-category profitability

| Finding | Profit |
|---|---:|
| Technology — highest category profit | $145,454.95 |
| Office Supplies | $122,490.80 |
| Furniture — lowest category profit | $18,451.27 |
| Tables — lowest sub-category profit | -$17,725.48 |
| Bookcases | -$3,472.56 |
| Supplies | -$1,189.10 |
| Fasteners | $949.52 |

### Regional performance

| Region | Profit |
|---|---:|
| West — highest | $108,418.45 |
| East | $91,522.78 |
| South | $46,749.43 |
| Central — lowest | $39,706.36 |

### Discount pattern

- The **70% discount level** recorded **-$40,075.36** in aggregate profit.
- The **80% discount level** recorded **-$30,539.04** in aggregate profit.
- The **0% discount level** recorded **$320,987.60** in aggregate profit.

These are descriptive comparisons. Discount level may be related to product mix, order characteristics, or other factors; the totals do not prove that discounting alone caused losses.

## 10. Actionable Business Recommendations

1. **Investigate Tables, Bookcases, and Supplies first.** Break down their orders by discount, region, shipping mode, sales, and profit before considering price or assortment changes.
2. **Review deep-discount orders.** Check whether negative-profit orders are concentrated in specific products or regions. Consider margin guardrails only after validating order-level drivers.
3. **Compare Central with West.** Compare category mix, sub-category performance, discounting, and shipping patterns to identify testable explanations for the profit gap.
4. **Monitor profit, not sales alone.** Use profit and margin alongside revenue when reviewing customers and products.
5. **Validate unusual monthly movements.** Check the underlying orders and ensure months are sorted by date rather than alphabetically by text labels.
6. **Reconcile before publishing.** Match the CSV, SQL results, Excel formulas, and Power BI filters before treating dashboard values as final.

## 11. Dashboard Preview / Screenshots

### Power BI Executive Overview

![Power BI Executive Overview](reports/dashboard_screenshots/powerbi_executive_overview.png)

[Open the full-size dashboard screenshot](reports/dashboard_screenshots/powerbi_executive_overview.png)

The Excel workbook is available at [`excel/Customer_Profitability_Dashboard.xlsx`](excel/Customer_Profitability_Dashboard.xlsx). The theme JSON is available at [`powerbi/theme/Customer_Profitability_Theme.json`](powerbi/theme/Customer_Profitability_Theme.json). Add fresh screenshots after confirming that all KPI formulas and charts display correctly.

## 12. Repository Structure

```text
Customer-profitability-intelligence/
├── data/
│   ├── raw/                         
│   └── processed/                  
├── docs/
│   └── Business_Insights.md
├── excel/
│   └── Customer_Profitability_Dashboard.xlsx
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   └── 03_customer_profitability_analysis.ipynb
├── powerbi/
│   ├── theme/Customer_Profitability_Theme.json
│   └── Customer_Profitability_Dashboard.pbix  
├── reports/
│   ├── dashboard_screenshots/
│   │   └── powerbi_executive_overview.png
│   └── automated_analysis_summary.md          
├── sql/
│   ├── 01_schema.sql
│   ├── 02_data_analysis.sql
│   └── 03_business_analysis.sql
├── analyze_superstore.py
├── data_quality_check.py
├── requirements.txt
├── .gitignore
└── README.md
```

The PBIX, SQL scripts, and `requirements.txt` were not available in the files inspected for this README, so their presence and exact contents should be verified in the repository before publishing. The paths above reflect the project structure shown in the supplied workspace screenshot.

## 13. Limitations & Future Improvements

- This is a descriptive analysis of the supplied dataset; it does not prove causation or quantify realized savings.
- The exact original dataset license/source was not verified from the supplied CSV.
- KPI totals can differ across tools if data versions, filters, or order-count definitions differ.
- Validate all dashboard formulas and interactions after refreshing or replacing source data.
- Add automated tests for metric calculations and a repeatable cross-tool reconciliation checklist.
- Improve the dashboard with clearly formatted KPI cards, date/category/region slicers, and refreshed screenshots.
- Investigate negative-profit orders at transaction level before proposing discount or pricing changes.

## 14. Author & Contact

**Aryan Singh Bais** — Aspiring Data Analyst

- GitHub: [Aryansingh-B](https://github.com/Aryansingh-B)
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/aryansinghbais8/)

---

*Portfolio project for demonstrating data cleaning, exploratory analysis, SQL, KPI design, dashboarding, and business recommendation skills.*