from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib

# Load trained pipeline
model = joblib.load("xgb_churn_pipeline.joblib")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = {
            'gender': request.form['gender'],
            'SeniorCitizen': float(request.form['SeniorCitizen']),
            'Partner': request.form['Partner'],
            'Dependents': request.form['Dependents'],
            'tenure': float(request.form['tenure']),
            'Contract': request.form['Contract'],
            'PaymentMethod': request.form['PaymentMethod'],
            'InternetService': request.form['InternetService'],
            'AvgMonthlyCost': float(request.form['AvgMonthlyCost']),
            'NumServices': float(request.form['NumServices']),
            'PaperlessBilling': request.form['PaperlessBilling']
        }

        df = pd.DataFrame([input_data])  # 1 row = request

        prediction = model.predict(df)[0]

        result = "The customer is likely to CHURN ❌" if prediction == 1 else "The customer will STAY ✔️"

        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
