
# Python Sales Data Analyzer

A Python-based data analysis project that analyzes retail sales data, evaluates data quality, and generates meaningful business insights using Pandas and Matplotlib.

## Project Overview

This project analyzes retail sales data to understand product performance, category revenue, regional sales, and monthly sales trends. It also performs basic data quality checks and generates visual charts to support business decision-making.

## Features

- Data quality checks for missing values and duplicate rows
- Validation of dates, quantities, and prices
- Total sales, total orders, average order value, and units sold
- Product-wise sales analysis
- Category-wise sales analysis
- Region-wise sales analysis
- Monthly sales trend analysis
- Identification of the highest-value order
- Automatic generation of sales charts

## Technologies Used

- Python
- Pandas
- Matplotlib
- CSV

## Key Results

| Metric | Result |
|---|---:|
| Total Sales | ₹5,15,100 |
| Total Orders | 20 |
| Average Order Value | ₹25,755 |
| Total Units Sold | 241 |
| Top-Selling Product | Laptop |
| Best-Performing Category | Electronics |
| Highest-Sales Region | North |
| Best Sales Month | May 2026 |
| Highest-Value Order | ₹1,10,000 |

## Business Insights

- Laptop generated the highest sales among individual products.
- Electronics was the highest-revenue category.
- North recorded the highest regional sales.
- May 2026 was the best month by total sales.
- Order ID 1001 had the highest order value of ₹1,10,000.

## Sales Charts

### 1. Monthly Sales

![Monthly Sales Chart](monthly_sales.png)

### 2. Product-Wise Sales

![Product Sales Chart](product_sales.png)

### 3. Category-Wise Sales

![Category Sales Chart](category_sales.png)

### 4. Region-Wise Sales

![Region Sales Chart](region_sales.png)

## Project Files

- `sales_analyzer.py` — Python analysis script
- `sales_data.csv` — Retail sales dataset
- `monthly_sales.png` — Monthly sales chart
- `product_sales.png` — Product-wise sales chart
- `category_sales.png` — Category-wise sales chart
- `region_sales.png` — Region-wise sales chart

## How to Run

### 1. Install Python

Install Python on your computer if it is not already installed.

### 2. Install Required Libraries

```bash
pip install pandas matplotlib
```

### 3. Keep Project Files Together

Make sure `sales_analyzer.py` and `sales_data.csv` are in the same folder.

### 4. Run the Project

```bash
python sales_analyzer.py
```

The analysis summary will appear in the terminal, and the charts will be saved in the project folder.

## Conclusion

This project demonstrates basic data cleaning, exploratory data analysis, sales reporting, and data visualization using Python.

---
