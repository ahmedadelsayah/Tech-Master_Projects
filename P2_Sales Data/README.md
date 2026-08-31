# Superstore Sales Dashboard

An interactive data visualization dashboard built with **Python**, **Matplotlib**, and **Pandas**. This application analyzes retail sales data, providing real-time filtering, key business performance metrics, and data-driven insights.

---

## Features

* **Dynamic Filtering:** Filter data seamlessly by **Year**, **Region**, **Category**, **Segment**, and **Ship Mode** using embedded interactive radio buttons.
* **KPI Metrics Summary:** Real-time display of total Sales, Profit, Profit Margin (%), Total Orders, Average Order Value, and Units Sold.
* **Sales Trend Analysis:** Line chart visualizing monthly sales performance across recorded years.
* **Categorical & Regional Breakdown:** Pie charts and bar charts for Region, Ship Mode, Customer Segment, Product Category, and Sub-Category distributions.
* **Geographical Insights:** Horizontal bar chart highlighting the Top 10 States by total revenue.
* **Business Insights:** Automated analysis identifying the most profitable Category and Region, the relationship between Discount and Profit, and the Top/Bottom performing products by profitability.

---

## Data Cleaning & Validation

Before analysis, the raw dataset goes through:

* **Correct processing order:** dates are converted first (`pd.to_datetime(..., errors="coerce")`), then missing/invalid rows are dropped — ensuring unparsable dates are properly caught.
* **Duplicate detection** and removal.
* **Missing value checks** across all columns, not just Sales and Order Date.
* **Invalid numeric value checks:** negative Sales, negative Profit (flagged for review), and Discount values outside the [0, 1] range.
* **Final validation summary:** dataset shape, column dtypes, and remaining nulls/duplicates printed after cleaning.

---

## Business Insights

The dashboard's analysis layer surfaces clear, actionable findings rather than relying on charts alone:

* Which **Category** drives the most Sales and Profit.
* Which **Region** is the most (and least) profitable.
* Whether higher **Discounts** are correlated with lower **Profit**.
* The **Top and Bottom products** by profitability, including a count of products currently generating a net loss.

---

## Visual Overview

| Component | Description |
| :--- | :--- |
| **Header KPIs** | High-level summary of financial and volume performance. |
| **Sidebar Controls** | Interactive radio buttons for customized data slicing (Year, Region, Category, Segment, Ship Mode). |
| **Main Layout** | Multi-panel grid displaying trends, category splits, and state rankings. |

---

## Tech Stack

* **Language:** Python
* **Data Manipulation:** `pandas`, `numpy`
* **Visualization:** `matplotlib` (using `GridSpec` and `RadioButtons` for layout and interactivity)

---

## Getting Started

### Prerequisites

Ensure you have Python installed, then install the required dependencies:

```bash
pip install pandas numpy matplotlib
```

### Running the Dashboard

Place your dataset as `sales_data.csv` in the project directory, then run:

```bash
python main.py
```
