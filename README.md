# 📡 Telco Customer Churn Prediction 

![Project Status](https://img.shields.io/badge/Status-Completed-success) ![Python](https://img.shields.io/badge/Python-3.10+-blue)

## 📊 Project Overview
In the competitive telecom sector, retaining customers is critical. This project analyzes **7,043 real customer records** to predict churn risks.
* **Goal:** Identify factors that drive customer attrition and recommend retention strategies.
* **Data Source:** [Telco Customer Churn Dataset (Kaggle)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) - *Data included in `data/` folder.*

## 🔍 Key Business Insights
1.  **Contract Trap:** Customers on **Month-to-Month contracts** are **15x more likely to churn** than those on 2-year contracts.
2.  **Senior Citizens:** Despite lower usage, senior citizens have a higher churn rate, suggesting a need for simplified support services.
3.  **Payment Friction:** "Electronic Check" users have the highest churn, indicating potential UX issues with that payment gateway.

## 📉 Visual Analysis

### Contract Type vs. Churn Risk
*Month-to-month contracts are the single biggest predictor of churn.*

![Churn by Contract](images/contract_risk_analysis.png)
*(Note: If the image doesn't load, ensure the folder name is 'images' and file is 'contract_risk_analysis.png')*

## 🛠 Technical Implementation
* **Language:** Python 3.10
* **Libraries:** `Pandas` (Data Manipulation), `Matplotlib/Seaborn` (Visualization).
* **File Structure:**
    * `data/`: Raw CSV dataset.
    * `notebooks/`: Jupyter notebooks for exploratory analysis.
    * `images/`: Generated charts for reporting.

## 🚀 How to Run
1. Clone the repository.
2. Install dependencies: `pip install pandas matplotlib seaborn`
3. Run the script: `python churn_analysis.py`
