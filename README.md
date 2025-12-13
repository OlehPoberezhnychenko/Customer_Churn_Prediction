# 📡 Telco Customer Churn Prediction

![Project Status](https://img.shields.io/badge/Status-Completed-success) ![Python](https://img.shields.io/badge/Python-3.10+-blue) ![Libraries](https://img.shields.io/badge/Library-Pandas%20|%20Seaborn-red)

## 📊 Project Overview
In the competitive telecom sector, acquiring a new customer is 5x more expensive than retaining an existing one. This project analyzes **7,043 real customer records** to identify exactly why customers are leaving.

* **Goal:** Predict churn behavior and calculate the financial impact of customer attrition.
* **Data Source:** [Telco Customer Churn Dataset (Kaggle)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) - *Data included in `data/` folder.*

## 🔍 Key Business Insights
*Generated automatically by `churn_analysis.py`*

1.  **Contract Trap:** Customers on **Month-to-Month contracts** have a **42.7% churn rate**, while those on Two-Year contracts have only a **2.8% churn rate**.
2.  **Fiber Optic Issue:** There is a technical or pricing issue with Fiber Optic Internet, as these users churn **significantly more** than DSL users.
3.  **Revenue Impact:** The analysis identifies exactly how much revenue is being lost annually due to churn, helping stakeholders prioritize retention budgets.

## 📉 Visual Analysis

### 1. Contract Type Risk
*Month-to-month contracts are the single biggest predictor of churn.*
![Contract Risk](images/01_contract_risk.png)

### 2. Tenure Distribution (When do they leave?)
*Red area shows churned customers leaving early (0-12 months). Green area shows loyal customers.*
![Tenure Distribution](images/02_tenure_distribution.png)

### 3. Payment Method Impact
*Electronic check users churn at a significantly higher rate than automatic payment users.*
![Payment Method](images/03_payment_method.png)


## 🛠 Technical Implementation
* **Language:** Python 3.10
* **Analysis:** `Pandas` for data cleaning and aggregation.
* **Visualization:** `Seaborn` for statistical graphics and heatmaps.
* **Automated Reporting:** The script calculates and prints exact financial loss numbers to the console.

* ## 🚀 How to Run
1. Clone the repository.
2. Install dependencies: `pip install pandas matplotlib seaborn`
3. Run the script: `python churn_analysis.py`


### 5. Predictive Modeling (Logistic Regression)
*We trained a Machine Learning model to predict churn with ~80% accuracy. The Confusion Matrix below shows the model's performance on test data.*
![Confusion Matrix](images/05_confusion_matrix.png)

**Model Metrics:**
* **Accuracy:** ~80% (Baseline)
* **Precision:** High precision for "No Churn" predictions.
* **Key Drivers:** Contract Type (Month-to-Month), Tenure, and Internet Service (Fiber Optic).
