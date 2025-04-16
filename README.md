# Task 6 - Sales Trend Analysis Using Aggregations

# Objective
Analyze monthly revenue and order volume using SQL (MySQL) and pandas.

# Dataset
- Source: https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci
- Columns used: `InvoiceDate`, `Quantity`, `Price`, `Invoice`

# Methodology
- Parsed date into `Year` and `Month`.
- Calculated `Revenue = Quantity * Price`.
- Aggregated using `SUM` for revenue and `COUNT(DISTINCT Invoice)` for order volume.

# SQL Code
See `task6_sales_analysis.sql`.

# Tools
- MySQL
- Python (pandas, matplotlib)

# Visualization
Line chart comparing monthly revenue vs order volume trends.
Bar charts highlight the periods with the highest earnings and the busiest months in terms of customer transactions.

