import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Connect to the MySQL database using env variables
conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DB")
)

query = """
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
"""

# Run query and export to CSV
df = pd.read_sql(query, conn)
df.to_csv("results/monthly_sales_summary.csv", index=False)

conn.close()
print("✅ Results exported to results/monthly_sales_summary.csv")
