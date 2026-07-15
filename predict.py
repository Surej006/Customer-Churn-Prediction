import pickle
import pandas as pd

print("Loading model and feature names...")

# Load trained model
model = pickle.load(open('model/churn_model.pkl', 'rb'))

# Load feature names
feature_names = pickle.load(open('model/feature_names.pkl', 'rb'))

print("Model and features loaded successfully!")

# Create empty dataframe with correct columns
input_df = pd.DataFrame(columns=feature_names)

# Initialize all values with 0
input_df.loc[0] = 0

# ---- Fill customer details (example customer) ----

input_df.loc[0, 'gender'] = 1                 # 1 = Male, 0 = Female
input_df.loc[0, 'SeniorCitizen'] = 0
input_df.loc[0, 'Partner'] = 1
input_df.loc[0, 'Dependents'] = 0
input_df.loc[0, 'tenure'] = 2
input_df.loc[0, 'PhoneService'] = 1
input_df.loc[0, 'MultipleLines'] = 1
input_df.loc[0, 'OnlineSecurity'] = 0
input_df.loc[0, 'OnlineBackup'] = 1
input_df.loc[0, 'DeviceProtection'] = 0
input_df.loc[0, 'TechSupport'] = 0
input_df.loc[0, 'StreamingTV'] = 1
input_df.loc[0, 'StreamingMovies'] = 1
input_df.loc[0, 'PaperlessBilling'] = 1
input_df.loc[0, 'MonthlyCharges'] = 120
input_df.loc[0, 'TotalCharges'] = 250

# One-hot encoded columns
input_df.loc[0, 'InternetService_Fiber optic'] = 1
input_df.loc[0, 'Contract_One year'] = 1
input_df.loc[0, 'PaymentMethod_Electronic check'] = 1

print("Making prediction...")

prediction = model.predict(input_df)

if prediction[0] == 1:
    print("RESULT: Customer is likely to CHURN")
else:
    print("RESULT: Customer is likely to STAY")
    