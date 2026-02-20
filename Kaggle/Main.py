import streamlit as st
import pickle
import numpy as np

#Load model
with open("CATbest_model0.pkl", "rb") as f:
    model = pickle.load(f)

#Feature options
gender_map = {'Female': 0, 'Male': 1}
location_map = {"Illinois": 0, "California": 1, "Florida": 2, "New York": 3, "Texas": 4}
sub_type_map = {"Basic": 0, "Premium": 1, "Enterprise": 2}
last_interaction_map = {"Neutral": 0, "Negative": 1, "Positive": 2}

st.title("Customer Churn Prediction")

st.header("Enter Customer Details")

#Inputs with min/max as per your specs ---
age = st.number_input("Age", min_value=18, max_value=69, value=30)
gender = st.selectbox("Gender", list(gender_map.keys()))
location = st.selectbox("Location", list(location_map.keys()))
subscription_type = st.selectbox("Subscription Type", list(sub_type_map.keys()))
account_age_months = st.number_input("Account Age (Months)", min_value=1, max_value=59, value=12)
monthly_spending = st.number_input("Monthly Spending", min_value=10.09, max_value=199.94, value=50.0)
total_usage_hours = st.number_input("Total Usage Hours", min_value=10, max_value=499, value=100)
support_calls = st.number_input("Support Calls", min_value=0, max_value=9, value=1)
late_payments = st.number_input("Late Payments", min_value=0, max_value=4, value=0)
streaming_usage = st.number_input("Streaming Usage", min_value=0, max_value=99, value=0)
discount_used = st.number_input("Discount Used", min_value=0, max_value=99, value=0)
satisfaction_score = st.number_input("Satisfaction Score", min_value=1, max_value=10, value=5)
last_interaction_type = st.selectbox("Last Interaction Type", list(last_interaction_map.keys()))
complaint_tickets = st.number_input("Complaint Tickets", min_value=0, max_value=4, value=0)
promo_opted_in = st.number_input("Promo Opted In", min_value=0, max_value=1, value=0)

#Prediction
if st.button("Predict Churn"):
    # Encode categorical features
    input_row = [
        age,
        gender_map[gender],
        location_map[location],
        sub_type_map[subscription_type],
        account_age_months,
        monthly_spending,
        total_usage_hours,
        support_calls,
        late_payments,
        streaming_usage,
        discount_used,
        satisfaction_score,
        last_interaction_map[last_interaction_type],
        complaint_tickets,
        promo_opted_in
    ]

    # Predict (0 = Not Churn, 1 = Churn)
    pred = model.predict(np.array([input_row]))[0]

    if pred == 1:
        st.error("Churn")
    else:
        st.success("Not Churn")