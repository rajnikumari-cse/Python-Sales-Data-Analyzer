
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load Sales Data
# -----------------------------

df = pd.read_csv("sales_data.csv")

# Check required columns
required_columns = [
    "Order_ID", "Order_Date", "Product",
    "Category", "Region", "Quantity", "Unit_Price"
]

missing_columns = [
    col for col in required_columns if col not in df.columns
]

if missing_columns:
    raise ValueError(f"Missing columns in CSV: {missing_columns}")

# Convert columns into correct data types
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Unit_Price"] = pd.to_numeric(df["Unit_Price"], errors="coerce")

# -----------------------------
# 2. Data Quality Checks
# -----------------------------

print("\n========== DATA QUALITY REPORT ==========")

print("\nMissing values before cleaning:")
print(df.isnull().sum())

duplicate_rows = df.duplicated().sum()
print(f"\nDuplicate rows: {duplicate_rows}")

invalid_quantity = (df["Quantity"] <= 0).sum()
invalid_price = (df["Unit_Price"] < 0).sum()
invalid_dates = df["Order_Date"].isnull().sum()

print(f"Rows with zero/negative quantity: {invalid_quantity}")
print(f"Rows with negative price: {invalid_price}")
print(f"Rows with invalid dates: {invalid_dates}")

# Remove exact duplicate rows
df = df.drop_duplicates()

# Remove rows missing essential analysis fields
df = df.dropna(subset=[
    "Order_ID", "Order_Date", "Product",
    "Category", "Region", "Quantity", "Unit_Price"
])

# Keep only positive quantities and non-negative prices
df = df[
    (df["Quantity"] > 0) &
    (df["Unit_Price"] >= 0)
].copy()

if df.empty:
    raise ValueError("No valid sales records remain after cleaning.")

# Calculate sales amount
df["Sales_Amount"] = df["Quantity"] * df["Unit_Price"]

# -----------------------------
# 3. Key Performance Indicators
# -----------------------------

total_sales = df["Sales_Amount"].sum()
total_orders = df["Order_ID"].nunique()

average_order_value = (
    total_sales / total_orders if total_orders else 0
)

total_units_sold = df["Quantity"].sum()

print("\n========== SALES SUMMARY ==========")
print(f"Total Sales: Rs. {total_sales:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value: Rs. {average_order_value:,.2f}")
print(f"Total Units Sold: {total_units_sold:,.0f}")

# -----------------------------
# 4. Product Analysis
# -----------------------------

product_sales = (
    df.groupby("Product")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
)

top_product = product_sales.index[0]
low_performing_products = product_sales.sort_values().head(3)

print("\n========== PRODUCT ANALYSIS ==========")
print(f"Top-Selling Product: {top_product}")

print("\nProduct-wise Sales:")
print(product_sales.round(2))

print("\nLowest-Selling Products:")
print(low_performing_products.round(2))

# -----------------------------
# 5. Category Analysis
# -----------------------------

category_sales = (
    df.groupby("Category")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
)

top_category = category_sales.index[0]

print("\n========== CATEGORY ANALYSIS ==========")
print(f"Best-Performing Category: {top_category}")
print(category_sales.round(2))

# -----------------------------
# 6. Region Analysis
# -----------------------------

region_sales = (
    df.groupby("Region")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
)

top_region = region_sales.index[0]

print("\n========== REGION ANALYSIS ==========")
print(f"Highest-Sales Region: {top_region}")
print(region_sales.round(2))

# -----------------------------
# 7. Monthly Sales Analysis
# -----------------------------

df["Month"] = df["Order_Date"].dt.to_period("M")

monthly_sales = (
    df.groupby("Month")["Sales_Amount"]
    .sum()
    .sort_index()
)

best_month = monthly_sales.idxmax()
best_month_sales = monthly_sales.max()

print("\n========== MONTHLY ANALYSIS ==========")
print("Monthly Sales:")
print(monthly_sales.round(2))

print(f"\nBest Sales Month: {best_month}")
print(f"Sales in Best Month: Rs. {best_month_sales:,.2f}")

# -----------------------------
# 8. Highest-Value Order
# -----------------------------

# Add all product rows belonging to each order
order_sales = (
    df.groupby("Order_ID")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
)

highest_order_id = order_sales.index[0]
highest_order_amount = order_sales.iloc[0]

print("\n========== HIGHEST-VALUE ORDER ==========")
print(f"Order ID: {highest_order_id}")
print(f"Order Total: Rs. {highest_order_amount:,.2f}")

# -----------------------------
# 9. Business Insights
# -----------------------------

print("\n========== BUSINESS INSIGHTS ==========")

print(
    f"1. {top_product} generated the highest sales "
    f"among individual products."
)

print(
    f"2. {top_category} was the highest-revenue category."
)

print(
    f"3. {top_region} generated the highest regional sales."
)

print(
    f"4. {best_month} was the best month by total sales."
)

print(
    f"5. The highest-value order was {highest_order_id}, "
    f"worth Rs. {highest_order_amount:,.2f}."
)

# -----------------------------
# 10. Charts
# -----------------------------

# Monthly Sales Chart
plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="bar", rot=45)
plt.title("Monthly Sales Performance")
plt.xlabel("Month")
plt.ylabel("Sales (Rs.)")
plt.tight_layout()
plt.savefig("monthly_sales.png", dpi=300)
plt.show()

# Product Sales Chart
plt.figure(figsize=(10, 5))
product_sales.sort_values(ascending=False).plot(kind="bar", rot=45)
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales (Rs.)")
plt.tight_layout()
plt.savefig("product_sales.png", dpi=300)
plt.show()

# Category Sales Chart
plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar", rot=0)
plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales (Rs.)")
plt.tight_layout()
plt.savefig("category_sales.png", dpi=300)
plt.show()

# Region Sales Chart
plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar", rot=0)
plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales (Rs.)")
plt.tight_layout()
plt.savefig("region_sales.png", dpi=300)
plt.show()

print("\nAnalysis completed successfully!")
print("Charts have been saved in your project folder.")
