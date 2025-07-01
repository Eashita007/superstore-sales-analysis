-- sales_trend_analysis.sql
-- Monthly Revenue and Order Volume Analysis for Superstore Dataset

SELECT
    YEAR(order_date) AS order_year,
    MONTH(order_date) AS order_month,
    SUM(sales) AS total_revenue,
    COUNT(DISTINCT order_id) AS total_orders
FROM
    orders
GROUP BY
    order_year,
    order_month
ORDER BY
    order_year,
    order_month;
