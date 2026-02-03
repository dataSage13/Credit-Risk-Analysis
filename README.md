# Credit-Risk-Analysis
An analysis on customer credit risk. It analyzes customer credit history to predict future loan default risks.

# Credit Risk & Loan Default Prediction

## Project Overview
This project analyzes customer financial and credit history data to predict loan default risk.
The goal is to assist financial institutions in identifying high-risk applicants.

## Dataset
- application_record.csv: Customer demographic and financial information
- credit_record.csv: Monthly credit repayment history

## Methodology
- Data cleaning and preprocessing
- Feature engineering and target variable creation
- Class imbalance handling using SMOTE
- Model training and comparison
- Performance evaluation using ROC-AUC
- Interactive dashboard using Streamlit

## Models Used
- Logistic Regression
- Random Forest
- Gradient Boosting

## Results
Gradient Boosting achieved the highest ROC-AUC score, indicating strong predictive power
for identifying potential loan defaulters.

## Business Insight
Applicants with unstable employment, lower income, and poor credit history
demonstrate a significantly higher probability of default.

## Tools
Python, Pandas, Scikit-learn, Matplotlib, Seaborn, Streamlit
