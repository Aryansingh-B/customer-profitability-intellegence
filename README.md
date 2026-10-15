# Customer Profitability & Revenue Leakage Intelligence

An Excel-based business analytics project using the Sample Superstore dataset to explore sales performance, profitability, discount impact, and loss-making product areas.

## Dashboard features
- KPI cards: Total Sales, Total Profit, Profit Margin, Unique Orders
- Monthly sales and profit trend
- Profit by product category
- Profit by region
- Profit by discount level
- Supporting tables and calculated columns

## Workbook
Open `Excel/Customer_Profitability_Dashboard.xlsx` and start with the `Excel_Dashboard` sheet. The `Start_Here` sheet explains each worksheet.

## Tools
- Microsoft Excel
- Pivot-style business analysis and charts
- Data quality checks and derived business metrics

## Metrics
- **Profit Margin** = Total Profit / Total Sales
- **Implied Cost** = Sales − Profit (derived estimate; not a full accounting cost model)
- **Shipping Days** = Ship Date − Order Date
- **Profit Status** = Loss / Break-even / Profitable

## Dataset note
The workbook was generated from the Sample Superstore CSV supplied for this project. Review the dataset's license and terms before redistributing the source data or publishing it in a public repository. The raw dataset is intentionally not included in this project package.

## Limitations
The dashboard's charts use the summary tables in `Analysis_Data`. If you append or replace source rows, update the summary tables to keep charts aligned. The Unique Orders formula uses `UNIQUE`, supported by Excel 365 and Excel 2021 or later.
