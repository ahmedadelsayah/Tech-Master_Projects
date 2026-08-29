# Superstore Sales Dashboard

An interactive data visualization dashboard built with **Python**, **Matplotlib**, and **Pandas**. This application analyzes retail sales data, providing real-time filtering and key business performance metrics.

---

## Features

* **Dynamic Filtering:** Filter data seamlessly by **Year**, **Region**, and **Category** using embedded interactive radio buttons.
* **KPI Metrics Summary:** Real-time display of total Sales, Profit, Profit Margin (%), Total Orders, Average Order Value, and Units Sold.
* **Sales Trend Analysis:** Line chart visualizing monthly sales performance across recorded years.
* **Categorical & Regional Breakdown:** Pie charts and bar charts for Region, Ship Mode, Customer Segment, Product Category, and Sub-Category distributions.
* **Geographical Insights:** Horizontal bar chart highlighting the Top 10 States by total revenue.

---

## Visual Overview

| Component | Description |
| :--- | :--- |
| **Header KPIs** | High-level summary of financial and volume performance. |
| **Sidebar Controls** | Interactive radio buttons for customized data slicing. |
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