# Retail Sales Forecasting with Prophet

This project performs **end-to-end time series forecasting** on retail sales data using **Python**, **Facebook Prophet**, and **Matplotlib**. It covers data preprocessing, daily aggregation, visualization, forecasting, and exporting results for further analysis or dashboarding.

---

## 📌 Project Overview

The goal of this project is to:

* Clean and preprocess raw retail sales data
* Aggregate sales on a daily basis
* Visualize historical sales trends
* Forecast future sales for the next **90 days**
* Analyze trend and seasonality components
* Export forecast results for reporting or dashboards

This is a **portfolio-ready project** suitable for Data Science and AI Engineer roles.

---

## 🛠️ Tools & Libraries

* **Python**
* **Pandas** – data manipulation
* **Matplotlib** – data visualization
* **Seaborn** – plot styling
* **Prophet** – time series forecasting

---

## 📂 Dataset

**Input File:** `retail_sales_data.csv`

Required columns:

* `Purchase_Date` – date of transaction
* `Total_Amount` – sales amount

---

## 🔄 Workflow

### 1. Data Preprocessing

* Convert `Purchase_Date` to datetime
* Group data by date
* Calculate total daily sales

### 2. Daily Sales Output

* Save aggregated data as:

  * `daily_sales.csv`

### 3. Exploratory Visualization

* Line chart of historical daily sales

### 4. Forecasting with Prophet

* Prepare Prophet-compatible dataset (`ds`, `y`)
* Train model with 95% confidence interval
* Forecast next **90 days**

### 5. Forecast Visualization

* Actual vs predicted sales
* Confidence interval (uncertainty range)
* Forecast start marker

### 6. Components Analysis

* Trend
* Weekly seasonality
* Yearly seasonality

### 7. Export Forecast Results

* Save forecast as:

  * `forecast_output.csv`

---

## 📈 Output Files

| File Name             | Description                                |
| --------------------- | ------------------------------------------ |
| `daily_sales.csv`     | Aggregated daily sales data                |
| `forecast_output.csv` | Forecasted sales with confidence intervals |

---

## 📊 Visual Outputs

* Historical sales trend
* 90-day future forecast
* Confidence interval shading
* Prophet component plots (trend & seasonality)

---

## 🚀 How to Run

1. Clone the repository
2. Install dependencies:

   ```bash
   pip install pandas matplotlib seaborn prophet
   ```
3. Place `retail_sales_data.csv` in the project directory
4. Run the Python script

---

## 📌 Use Cases

* Retail sales planning
* Inventory forecasting
* Business decision support
* Dashboard integration (Power BI / Plotly Dash)

---

## 👤 Author

**Khubaib**
Aspiring AI Engineer | Data Science & Forecasting Projects

---

## ⭐ Notes

* Prophet works best with continuous date data
* Forecast accuracy depends on historical data quality
* Confidence intervals represent uncertainty, not exact limits

---

If you like this project, feel free to ⭐ the repository and use it as a reference in your own forecasting workflows.
