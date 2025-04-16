
-- Task 6: Monthly Sales Trend Analysis Using SQL (MySQL)

-- 1. Creation of Table
CREATE TABLE online_sales (
    Invoice VARCHAR(20),
    StockCode VARCHAR(20),
    Description TEXT,
    Quantity INT,
    InvoiceDate DATETIME,
    Price DECIMAL(10, 2),
    CustomerID INT,
    Country VARCHAR(100)
);



-- 2. Query for Monthly Revenue and Order Volume
SELECT
    YEAR(InvoiceDate) AS Year,
    MONTH(InvoiceDate) AS Month,
    SUM(Quantity * Price) AS Monthly_Revenue,
    COUNT(DISTINCT Invoice) AS Order_Volume
FROM
    online_sales
GROUP BY
    YEAR(InvoiceDate), MONTH(InvoiceDate)
ORDER BY
    Year, Month;
