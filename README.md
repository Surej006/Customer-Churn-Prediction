# Customer Churn Prediction Using Machine Learning

## Project Overview
This project predicts whether a telecom customer is likely to churn using machine learning.

## Dataset
Telecom Customer Churn dataset from Kaggle.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

## Project Workflow
1. Data collection
2. Exploratory data analysis
3. Data preprocessing
4. Feature engineering
5. Model building
6. Model evaluation
7. Model saving using Pickle
8. Streamlit web application

## Model Used
Random Forest Classifier

## Features
- Predicts customer churn

## Model Performance

- Logistic Regression Accuracy: approximately 79%
- Logistic Regression ROC-AUC: approximately 0.83
- Random Forest Accuracy: approximately 82%
- Random Forest ROC-AUC: approximately 0.86

Random Forest was selected as the final model because it provided stronger overall performance.

## AI Integration

The application sends selected customer details, the machine-learning prediction,
and churn probability to Google Gemini through an API.

Gemini generates a personalized explanation and customer-retention recommendation.

The Random Forest model performs the churn prediction.
Gemini is used only for explanation and recommendations.

## Security

The Gemini API key is stored locally in `API.env`.

The file is excluded from GitHub through `.gitignore`,
preventing the secret key from being publicly exposed.

## Installation

```bash
pip install -r requirements.txt
- Displays churn probability
- Shows risk level
- Provides business recommendation

## How to Run
```bash
streamlit run app.py
