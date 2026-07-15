import streamlit as st
import pickle
import pandas as pd

from ai_helper import get_ai_recommendation

# Page setup
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# Load model
model = pickle.load(open("model/churn_model.pkl", "rb"))
feature_names = pickle.load(open("model/feature_names.pkl", "rb"))

# App title
st.title("📊 Customer Churn Prediction Dashboard")
st.markdown("Predict customer churn using a trained Machine Learning model.")

st.divider()

# Sidebar inputs
st.sidebar.header("Customer Information")

gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.sidebar.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.sidebar.selectbox("Partner", ["No", "Yes"])
dependents = st.sidebar.selectbox("Dependents", ["No", "Yes"])

st.sidebar.header("Service Information")

phone_service = st.sidebar.selectbox("Phone Service", ["No", "Yes"])
multiple_lines = st.sidebar.selectbox("Multiple Lines", ["No", "Yes"])
internet_service = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.sidebar.selectbox("Online Security", ["No", "Yes"])
online_backup = st.sidebar.selectbox("Online Backup", ["No", "Yes"])
device_protection = st.sidebar.selectbox("Device Protection", ["No", "Yes"])
tech_support = st.sidebar.selectbox("Tech Support", ["No", "Yes"])
streaming_tv = st.sidebar.selectbox("Streaming TV", ["No", "Yes"])
streaming_movies = st.sidebar.selectbox("Streaming Movies", ["No", "Yes"])

st.sidebar.header("Billing Information")

tenure = st.sidebar.number_input("Tenure (Months)", min_value=0, max_value=100, value=12)
monthly_charges = st.sidebar.number_input("Monthly Charges", min_value=0.0, value=70.0)
total_charges = st.sidebar.number_input("Total Charges", min_value=0.0, value=800.0)
contract = st.sidebar.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.sidebar.selectbox("Paperless Billing", ["No", "Yes"])
payment_method = st.sidebar.selectbox(
    "Payment Method",
    ["Bank transfer (automatic)", "Credit card (automatic)", "Electronic check", "Mailed check"]
)

# Main layout
col1, col2, col3 = st.columns(3)

with col1:
    st.info("👤 Customer Profile")
    st.write(f"**Gender:** {gender}")
    st.write(f"**Senior Citizen:** {senior_citizen}")
    st.write(f"**Partner:** {partner}")
    st.write(f"**Dependents:** {dependents}")

with col2:
    st.info("📞 Service Details")
    st.write(f"**Internet Service:** {internet_service}")
    st.write(f"**Tech Support:** {tech_support}")
    st.write(f"**Online Security:** {online_security}")

with col3:
    st.info("💳 Billing Details")
    st.write(f"**Contract:** {contract}")
    st.write(f"**Monthly Charges:** ₹{monthly_charges}")
    st.write(f"**Payment Method:** {payment_method}")

st.divider()

# Predict button
if st.sidebar.button("Predict Churn"):

    input_df = pd.DataFrame(columns=feature_names)
    input_df.loc[0] = 0

    input_df.loc[0, "gender"] = 1 if gender == "Male" else 0
    input_df.loc[0, "SeniorCitizen"] = 1 if senior_citizen == "Yes" else 0
    input_df.loc[0, "Partner"] = 1 if partner == "Yes" else 0
    input_df.loc[0, "Dependents"] = 1 if dependents == "Yes" else 0
    input_df.loc[0, "tenure"] = tenure
    input_df.loc[0, "PhoneService"] = 1 if phone_service == "Yes" else 0
    input_df.loc[0, "MultipleLines"] = 1 if multiple_lines == "Yes" else 0
    input_df.loc[0, "OnlineSecurity"] = 1 if online_security == "Yes" else 0
    input_df.loc[0, "OnlineBackup"] = 1 if online_backup == "Yes" else 0
    input_df.loc[0, "DeviceProtection"] = 1 if device_protection == "Yes" else 0
    input_df.loc[0, "TechSupport"] = 1 if tech_support == "Yes" else 0
    input_df.loc[0, "StreamingTV"] = 1 if streaming_tv == "Yes" else 0
    input_df.loc[0, "StreamingMovies"] = 1 if streaming_movies == "Yes" else 0
    input_df.loc[0, "PaperlessBilling"] = 1 if paperless_billing == "Yes" else 0
    input_df.loc[0, "MonthlyCharges"] = monthly_charges
    input_df.loc[0, "TotalCharges"] = total_charges

    if internet_service == "Fiber optic":
        input_df.loc[0, "InternetService_Fiber optic"] = 1
    elif internet_service == "No":
        input_df.loc[0, "InternetService_No"] = 1

    if contract == "One year":
        input_df.loc[0, "Contract_One year"] = 1
    elif contract == "Two year":
        input_df.loc[0, "Contract_Two year"] = 1

    if payment_method == "Credit card (automatic)":
        input_df.loc[0, "PaymentMethod_Credit card (automatic)"] = 1
    elif payment_method == "Electronic check":
        input_df.loc[0, "PaymentMethod_Electronic check"] = 1
    elif payment_method == "Mailed check":
        input_df.loc[0, "PaymentMethod_Mailed check"] = 1

    prediction = model.predict(input_df)
    churn_probability = model.predict_proba(input_df)[0][1]

    st.subheader("🔍 Prediction Result")

    result_col1, result_col2, result_col3 = st.columns(3)

    with result_col1:
        if prediction[0] == 1:
            st.error("⚠️ Likely to Churn")
        else:
            st.success("✅ Likely to Stay")

    with result_col2:
        st.metric("Churn Probability", f"{churn_probability:.2%}")

    with result_col3:
        if churn_probability < 0.30:
            st.success("🟢 Low Risk")
        elif churn_probability < 0.70:
            st.warning("🟡 Medium Risk")
        else:
            st.error("🔴 High Risk")
            
    
    st.subheader("💡 Business Recommendation")

    reasons = []

    if tenure <= 6:
        reasons.append("new customer with low tenure")

    if monthly_charges >= 80:
        reasons.append("high monthly charges")

    if contract == "Month-to-month":
        reasons.append("month-to-month contract")

    if internet_service == "Fiber optic":
        reasons.append("fiber optic service")

    if tech_support == "No":
        reasons.append("no tech support")

    if payment_method == "Electronic check":
        reasons.append("electronic check payment method")

    if churn_probability >= 0.70:
        st.warning("High Risk Customer")
    elif churn_probability >= 0.30:
        st.info("Medium Risk Customer")
    else:
        st.success("Low Risk Customer")

    if reasons:
       st.write("Main risk factors identified:")
       for reason in reasons:
            st.write(f"- {reason}")
    else:
       st.write("No major risk factors identified from the entered details.")

    if churn_probability >= 0.70:
        st.write("Recommended action: Contact the customer immediately, offer a retention discount, and encourage switching to a       longer-term contract.")
    elif churn_probability >= 0.30:
        st.write("Recommended action: Monitor the customer closely and provide personalized offers or service support.")
    else:
        st.write("Recommended action: Continue loyalty engagement and maintain good customer experience.")

    # AI recommendation section
    st.subheader("🤖 AI-Powered Recommendation")

    prediction_text = (
        "Likely to Churn"
        if prediction[0] == 1
        else "Likely to Stay"
    )

    prompt = f"""
    You are a telecom customer-retention analyst.

    Customer details:
    - Tenure: {tenure} months
    - Monthly charges: {monthly_charges}
    - Contract: {contract}
    - Internet service: {internet_service}
    - Online security: {online_security}
    - Tech support: {tech_support}
    - Payment method: {payment_method}

    Machine-learning result:
    - Prediction: {prediction_text}
    - Churn probability: {churn_probability:.2%}

    Explain the main churn risk factors briefly.
    Provide three practical retention recommendations.
    Keep the answer clear and under 150 words.
    Do not claim that Gemini made the churn prediction.
    """

    with st.spinner("Generating AI recommendation..."):
        ai_recommendation = get_ai_recommendation(prompt)

    if ai_recommendation:
        st.write(ai_recommendation)
    else:
        st.info(
            "Gemini is temporarily unavailable. "
            "The rule-based recommendation above is still available."
        )