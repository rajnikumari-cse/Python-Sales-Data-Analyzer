import pandas as pd
import matplotlib.pyplot as plt


# Load sales data
df = pd.read_csv("sales_data.csv")

# Convert date column
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Calculate sales amount
df["Sales_Amount"] = df["Quantity"] * df["Unit_Price"]


# -----------------------------
# Key Performance Indicators
# -----------------------------

total_sales = df["Sales_Amount"].sum()
total_orders = df["Order_ID"].nunique()
average_order_value = total_sales / total_orders


# -----------------------------
# Product Analysis
# -----------------------------

product_sales = (
    df.groupby("Product")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
)

top_product = product_sales.index[0]


# -----------------------------
# Category Analysis
# -----------------------------

category_sales = (
    df.groupby("Category")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
)

top_category = category_sales.index[0]


# -----------------------------
# Region Analysis
# -----------------------------

region_sales = (
    df.groupby("Region")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
)


# -----------------------------
# Monthly Sales Analysis
# -----------------------------

df["Month"] = df["Order_Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales_Amount"].sum()


# -----------------------------
# Highest Value Order
# -----------------------------

highest_order = df.loc[df["Sales_Amount"].idxmax()]


# -----------------------------
# Low Performing Products
# -----------------------------

low_performing_products = product_sales.sort_values().head(3)


# -----------------------------
# Data Quality Check
# -----------------------------

missing_values = df.isnull().sum()


# -----------------------------
# Final Sales Summary
# -----------------------------

print("\n" + "=" * 45)
print("           SALES ANALYSIS SUMMARY")
print("=" * 45)

print(f"Total Sales: ₹{total_sales:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value: ₹{average_order_value:,.2f}")
print(f"Top-Selling Product: {top_product}")
print(f"Best-Performing Category: {top_category}")

print("\nSales by Region:")
print(region_sales)

print("\nSales by Category:")
print(category_sales)

print("\nLow-Performing Products:")
print(low_performing_products)

print("\nHighest Value Order:")
print(highest_order)

print("\nMissing Values:")
print(missing_values)


# -----------------------------
# Monthly Sales Chart
# -----------------------------

plt.figure(figsize=(10, 5))

monthly_sales.plot(kind="bar")

plt.title("Monthly Sales Performance")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# -----------------------------
# Product Sales Chart
# -----------------------------

plt.figure(figsize=(10, 5))

product_sales.plot(kind="bar")

plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# -----------------------------
# Category Sales Chart
# -----------------------------

plt.figure(figsize=(8, 5))

category_sales.plot(kind="bar")

plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales Amount")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()