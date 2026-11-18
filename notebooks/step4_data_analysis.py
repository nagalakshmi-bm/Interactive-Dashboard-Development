import pandas as pd

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_superstore.csv")

print("SALES DATA ANALYSIS")

# Key Performance Indicators
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
average_sales = df["Sales"].mean()

print("\nKEY PERFORMANCE INDICATORS")
print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Orders:", total_orders)
print("Average Sales:", round(average_sales, 2))

# Sales by Category
print("\nSALES BY CATEGORY")
print(df.groupby("Category")["Sales"].sum())

# Profit by Region
print("\nPROFIT BY REGION")
print(df.groupby("Region")["Profit"].sum())

# Top 10 Products
print("\nTOP 10 PRODUCTS")
print(df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10))

# Save analysis summary
summary = pd.DataFrame({
    "Metric": ["Total Sales", "Total Profit", "Total Orders", "Average Sales"],
    "Value": [total_sales, total_profit, total_orders, average_sales]
})

summary.to_csv("visualizations/sales_summary.csv", index=False)

print("\nSALES ANALYSIS COMPLETED")
print("Summary saved successfully!")
