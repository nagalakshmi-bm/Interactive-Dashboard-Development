import pandas as pd
import matplotlib.pyplot as plt
import os

# Create visualization folder
os.makedirs("visualizations", exist_ok=True)

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_superstore.csv")

# Convert Order Date
df["Order Date"] = pd.to_datetime(df["Order Date"])

# 1. Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualizations/sales_by_category.png")
plt.close()

# 2. Profit by Region
region_profit = df.groupby("Region")["Profit"].sum()

plt.figure(figsize=(8, 5))
region_profit.plot(kind="bar")
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.savefig("visualizations/profit_by_region.png")
plt.close()

# 3. Monthly Sales Trend
df["Month"] = df["Order Date"].dt.to_period("M").astype(str)
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(12, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/monthly_sales_trend.png")
plt.close()

# 4. Top 10 Products
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
top_products.sort_values().plot(kind="barh")
plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.tight_layout()
plt.savefig("visualizations/top_10_products.png")
plt.close()

print("ALL VISUALIZATIONS CREATED SUCCESSFULLY!")
print("Check the visualizations folder.")
