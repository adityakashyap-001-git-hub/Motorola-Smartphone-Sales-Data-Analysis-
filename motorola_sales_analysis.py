
# Motorola Smartphone Sales Data Analysis
# Author: Aditya Kashyap
# Description: Data cleaning and analysis for Motorola smartphone sales dataset (Jan–Dec 2025)

import pandas as pd
import numpy as np

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv("motorola_sales.csv")

# -----------------------------
# Data Cleaning
# -----------------------------

# Remove duplicate records
df.drop_duplicates(inplace=True)

# Check missing values
print("Missing values in dataset:")
print(df.isnull().sum())

# Convert Month column to datetime
df['Month'] = pd.to_datetime(df['Month'])

# Extract Month Name and Day Name
df['Month_Name'] = df['Month'].dt.month_name()
df['Day_Name'] = df['Month'].dt.day_name()

print("\nPreview of cleaned dataset:")
print(df.head())

# -----------------------------
# Data Analysis
# -----------------------------

# Brand-wise Sales
brand_sales = df.groupby('Brand')['Total Sales'].sum().sort_values(ascending=False)
print("\nBrand-wise Sales:")
print(brand_sales)

# Monthly Quantity Sold
monthly_quantity = df.groupby('Month_Name')['Quantity'].sum()
print("\nMonthly Quantity Sold:")
print(monthly_quantity)

# Payment Method Distribution
payment_distribution = df['Payment Method'].value_counts()
print("\nPayment Method Distribution:")
print(payment_distribution)

# Top Selling Mobile Models
top_models = df.groupby('Mobile Model')['Total Sales'].sum().sort_values(ascending=False)
print("\nTop Selling Mobile Models:")
print(top_models)

# -----------------------------
# Key Metrics
# -----------------------------

total_sales = df['Total Sales'].sum()
total_quantity = df['Quantity'].sum()
total_transactions = df['Transaction'].nunique()

avg_sales = total_sales / total_transactions

print("\nKey Metrics")
print("Total Sales:", total_sales)
print("Total Quantity:", total_quantity)
print("Total Transactions:", total_transactions)
print("Average Sales per Transaction:", avg_sales)

# -----------------------------
# Save Cleaned Dataset
# -----------------------------

df.to_csv("cleaned_motorola_sales.csv", index=False)

print("\nCleaned dataset saved as 'cleaned_motorola_sales.csv'")
