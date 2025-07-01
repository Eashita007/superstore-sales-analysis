# 📊 Superstore Sales Analysis using SQL (Task 6)

This project performs a time-based trend analysis on the Superstore sales dataset using **MySQL**. It identifies monthly **revenue** and **order volume** patterns using SQL aggregation functions, and exports results for reporting or dashboarding.

---

## 📁 Project Structure

```bash
superstore-sales-analysis/
├── Dataset/
│ └── Sample - Superstore.csv # Original dataset from Kaggle
├── SQL/
│ └── sales_trend_analysis.sql # SQL query for trend analysis
├── results/
│ └── monthly_sales_summary.csv # Output result: revenue + order count
├── load_superstore.py # Loads cleaned CSV into MySQL
├── export_results.py # Exports monthly summary to CSV
├── .env # Stores DB credentials (not tracked)
├── example.env # Stores DB credentials (example file for user to put their credentials)
├── .gitignore # Ignores sensitive and unnecessary files
├──  requirements.txt # Requirements for the setup
└── README.md # Project overview (this file)
```

---

## 🧾 Dataset

- **Source**: [Superstore Dataset (Final) by Vivek468 on Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **File**: `Sample - Superstore.csv`
- **Relevant Fields Used**:
  - `Order ID` → Order Identifier
  - `Order Date` → Date of Order
  - `Product ID` → Item purchased
  - `Sales` → Revenue per row

---

## 🧠 Objectives

- Group sales data **monthly** and **yearly**
- Calculate:
  - 🧾 `Total Revenue` (via `SUM(sales)`)
  - 📦 `Order Volume` (via `COUNT(DISTINCT order_id)`)
- Identify sales trends and seasonality

---

## 🛠️ Tools & Technologies

- MySQL 8
- Python 3.12
- `pandas`, `mysql-connector-python`, `python-dotenv`

---

## ⚙️ How to Use

### 🔧 Setup MySQL & Python Environment

1. Clone this repo
2. Set up a virtual environment and install dependencies:
```bash
 pip install -r requirements.txt
```
3. Create a .env file with your DB credentials:
```bash
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=superstore_db
```
## 🚀 Run the Pipeline

1. Load the CSV to MySQL
```bash
python load_superstore.py
```

2. Run the SQL Analysis
```bash
mysql -u root -p superstore_db < sql/sales_trend_analysis.sql
```
3.  Export results to CSV
```bash
python export_results.py
```

## 📊 Sample Output

| order_year | order_month | total_revenue | total_orders |
|------------|-------------|----------------|---------------|
| 2014       | 1           | 28,473.80       | 32            |
| 2014       | 2           | 9,039.84        | 28            |
| ...        | ...         | ...             | ...           |

---

## ✅ Outcome

- Mastered SQL aggregations and grouping functions  
- Created a secure and reproducible analysis pipeline  
- Exported structured results for reporting or visualization  

---

## ✨ Future Improvements

- Build a Streamlit dashboard for interactive exploration  
- Add category-wise or region-wise breakdowns  
- Integrate with Power BI or Tableau  
