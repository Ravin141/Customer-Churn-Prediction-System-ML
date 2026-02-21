# Customer Churn Prediction System

A Machine Learning web application built using **Streamlit** that predicts whether a customer is likely to churn based on customer data.

---

## About the Project

This is a machine learning project that demonstrates:

- Data preprocessing
- Model training in Jupyter Notebook
- Saving trained model using Pickle
- Deploying ML model using Streamlit
- Building an interactive web interface

The model predicts:

- **0 → Not Churn**
- **1 → Churn**

---

## Technologies Used

- Python
- Streamlit
- NumPy
- Pickle
- Jupyter Notebook

---

## Project Structure

```
├── Main.py
├── best.ipynb
├── CATbest_model0.pkl
├── README.md
```

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Ravin141/Customer-Churn-Prediction-System-ML.git
cd Customer-Churn-Prediction-System-ML
```

### 2. Install dependencies

```bash
pip install streamlit numpy
```

### 3. Run the app

```bash
streamlit run Main.py
```

---

## Features

User inputs:

- Age
- Gender
- Location
- Subscription Type
- Account Age (Months)
- Monthly Spending
- Total Usage Hours
- Support Calls
- Late Payments
- Streaming Usage
- Discount Used
- Satisfaction Score
- Last Interaction Type
- Complaint Tickets
- Promo Opted In

Click **Predict Churn** to see the result.

---

## Future Improvements

- Add probability score
- Show model evaluation metrics
- Improve UI design
- Deploy online

---

## Author

Ravin Perera <br>
Undergraduate – BSc (Hons) Software Engineering 
