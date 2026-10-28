
# Python Sales Data Analyzer

A Python-based data analysis project that analyzes retail sales data and generates useful business insights through summary statistics, product analysis, category analysis, regional analysis, and monthly sales trends.

## Project Overview

This project uses Python, Pandas, and Matplotlib to analyze retail sales data, check data quality, identify sales trends, and visualize business performance.

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

## Project Files

- `python_sales_analysis.py` — Python analysis script
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
   ```

3. Keep `python_sales_analysis.py` and `sales_data.csv` in the same folder.
4. Run the script:

   ```bash
   python python_sales_analysis.py
   ```

5. View the sales summary in the terminal and the generated charts in the project folder.

## Conclusion

This project demonstrates basic data cleaning, exploratory data analysis, sales reporting, and data visualization using Python.
