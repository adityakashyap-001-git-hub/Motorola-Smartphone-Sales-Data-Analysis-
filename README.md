# Motorola-Smartphone-Sales-Data-Analysis-

### 📌 Project Overview

This project analyzes smartphone sales data across different brands and models to identify revenue trends, customer behavior, and payment preferences using **Python, SQL, and Power BI**.

---

# 📁 Dataset Information

Columns included:

* Month
* Brand
* Mobile Model
* Customer Name
* Payment Method
* Transaction
* Quantity
* Total Sales
* Rating

Dataset Size:

* **4,000 transactions**
* **19,000 units sold**

Time Period: **Jan – Dec 2025**

---

# 🛠 Tools Used

* Python (Pandas, NumPy)
* SQL
* Power BI
* Excel

---

# 🧹 Data Cleaning (Python)

Steps performed:

• Removed duplicate records
• Handled missing values
• Converted date columns to datetime
• Extracted month and weekday features

Example Python code:

```python
import pandas as pd

df = pd.read_csv("motorola_sales.csv")

df.drop_duplicates(inplace=True)

df.isnull().sum()

df['Month'] = pd.to_datetime(df['Month'])

df['Month_Name'] = df['Month'].dt.month_name()
df['Day_Name'] = df['Month'].dt.day_name()
```

---

# 📊 Python Analysis

### Brand-wise Sales

```python
df.groupby('Brand')['Total Sales'].sum().sort_values(ascending=False)
```

### Monthly Quantity Sold

```python
df.groupby('Month_Name')['Quantity'].sum()
```

### Payment Method Distribution

```python
df['Payment Method'].value_counts()
```

### Top Selling Models

```python
df.groupby('Mobile Model')['Total Sales'].sum().sort_values(ascending=False)
```

---

# 🗄 SQL Queries Used

### Total Sales

```sql
SELECT SUM(Total_Sales) AS Total_Sales
FROM motorola_sales;
```

### Sales by Brand

```sql
SELECT Brand,
SUM(Total_Sales) AS Brand_Sales
FROM motorola_sales
GROUP BY Brand
ORDER BY Brand_Sales DESC;
```

### Monthly Sales Trend

```sql
SELECT Month,
SUM(Quantity) AS Units_Sold
FROM motorola_sales
GROUP BY Month
ORDER BY Month;
```

### Payment Method Distribution

```sql
SELECT Payment_Method,
COUNT(*) AS Transactions
FROM motorola_sales
GROUP BY Payment_Method;
```

### Top Selling Models

```sql
SELECT Mobile_Model,
SUM(Total_Sales) AS Sales
FROM motorola_sales
GROUP BY Mobile_Model
ORDER BY Sales DESC;
```

---

# 📈 Power BI Dashboard

![IMG-20250530-WA0007(1) jpg](https://github.com/user-attachments/assets/b281159a-f89d-4dfb-8ba7-caa4cab6f645)


### KPIs

* Total Sales → **₹769.20M**
* Total Quantity → **19K**
* Transactions → **4K**
* Avg Sales → **₹40.11K**

---

# 📊 Dashboard Visuals

• KPI Cards – Sales, Quantity, Transactions
• Bar Chart – Sales by Brand
• Line Chart – Monthly Quantity Sold
• Funnel Chart – Customer Ratings
• Pie Chart – Payment Methods
• Bar Chart – Sales by Mobile Model
• Column Chart – Sales by Day
• Table – Brand Sales Summary

---

# 📌 Key Insights

1️⃣ **Apple, Samsung and Vivo dominate total smartphone sales.**

2️⃣ **Saturday is the highest sales day**, showing strong weekend demand.

3️⃣ **UPI and Debit Card account for more than 50% of transactions**, indicating digital payment dominance.

4️⃣ **Customer satisfaction is high**, with majority of ratings being **4★ and 5★**.

5️⃣ Sales dip in **September**, possibly due to seasonal buying patterns.

---

# 3️⃣ Power BI DAX Measures

### Total Sales

```DAX
Total Sales = SUM('Sales'[TotalAmount])
```

### Total Quantity

```DAX
Total Quantity = SUM('Sales'[Quantity])
```

### Average Sales

```DAX
Avg Sales = AVERAGE('Sales'[TotalAmount])
```

### High Rating %

```DAX
Rating % =
DIVIDE(
COUNTROWS(FILTER(Sales, Sales[Rating] >= 4)),
COUNTROWS(Sales)
)
```

---

# ⭐ Skills Demonstrated

• Data Cleaning
• Exploratory Data Analysis
• SQL Querying
• Dashboard Development
• Business Insights

---




