import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load only required columns from the CSV
df = pd.read_csv(
    'Dataset/Sample - Superstore.csv',
    encoding='ISO-8859-1',
    usecols=['Row ID', 'Order ID', 'Order Date', 'Product ID', 'Sales']
)

# Convert 'Order Date' to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=False)

# Connect to MySQL using env vars
conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DB")
)

cursor = conn.cursor()

# Insert each row
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO orders (row_id, order_id, order_date, product_id, sales)
        VALUES (%s, %s, %s, %s, %s)
    """, (int(row['Row ID']), row['Order ID'], row['Order Date'].date(), row['Product ID'], float(row['Sales'])))

conn.commit()
cursor.close()
conn.close()

print("Data inserted successfully.")
