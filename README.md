# Python Sales Data Analyzer

A Python-based data analysis project that analyzes retail sales data and generates useful business insights through data cleaning, summary statistics, product analysis, category analysis, regional analysis, and monthly sales trends.

## Project Overview

This project uses Python, Pandas, and Matplotlib to analyze retail sales data, check data quality, identify sales trends, and visualize business performance.

## Features

- Data quality checks for missing values and duplicate rows
- Validation of dates, quantities, and prices
- Calculation of total sales, total orders, average order value, and units sold
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
- CSV dataset

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

## Business Insights

- Laptop generated the highest sales among individual products.
- Electronics was the highest-revenue category.
- North was the highest-sales region.
- May 2026 recorded the highest monthly sales.
- Order 1001 had the highest order value at ₹1,10,000.

## Sales Charts

### Monthly Sales

![Monthly Sales Chart](monthly_sales.png)

### Product-Wise Sales

![Product Sales Chart](product_sales.png)

### Category-Wise Sales

![Category Sales Chart](category_sales.png)

### Region-Wise Sales

![Region Sales Chart](region_sales.png)

## Project Files

- `sales_analyzer.py` — Python analysis script
- `sales_data.csv` — Retail sales dataset
- `monthly_sales.png` — Monthly sales chart
- `product_sales.png` — Product-wise sales chart
- `category_sales.png` — Category-wise sales chart
- `region_sales.png` — Region-wise sales chart

## How to Run

1. Install Python on your computer.

2. Install the required libraries:

   ```bash
   pip install pandas matplotlib
