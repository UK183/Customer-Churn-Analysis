# 📊  Customer Churn Prediction — Telco Dataset

An end-to-end Machine Learning solution acieving 82% accuracy to predict customer churn for a telecom company.  
This project covers data cleaning, feature engineering, model development, performance evaluation, and a deployment-ready ML pipeline.

---

## 🔍 Project Overview

- **Objective:** Predict whether a customer will churn (0/1) based on demographics, billing patterns, and service usage.
- **Dataset:** Telco Customer Churn dataset.
- **Outcome:**
  
✔️Achieved strong churn prediction accuracy using XGBoost (~82%).

✔️Identified key churn drivers such as contract type, monthly charges, tenure, and number of services.

✔️Built a fully automated ML pipeline (preprocessing + model) ready for real-world deployment.

✔️Reduced model preprocessing errors by implementing One-Hot Encoding and scaling inside a unified pipeline.

✔️Deployed a functional Flask web app allowing users to input customer details and get real-time churn predictions.

✔️Improved data quality by handling missing values and converting inconsistent fields like TotalCharges.

✔️Enabled business decisions by highlighting high-risk customers and improving retention strategies.

---

### 📊 Dashboard Insights (Power BI)

✔️Total customers analyzed: 7,030 with an average monthly cost of $64.80.

✔️73.42% customers stayed, while 26.58% churned — showing moderate churn risk.

✔️Fiber Optic users show the highest churn, indicating dissatisfaction with internet quality or cost.

✔️Customers without Tech Support churn significantly more, proving support availability impacts retention.

✔️Month-to-month contract customers churn the most, confirming contract length strongly influences loyalty.

✔️Security features (OnlineSecurity & OnlineBackup) show a clear trend: customers lacking these services churn at a much higher rate.

✔️Churn is comparatively higher across both genders, roughly similar between male and female customers.

---

## 🧠 Key Steps in the Project

### ✔️ 1. Data Cleaning & Preparation
- Handled missing or incorrect values (e.g., `TotalCharges`).
- Converted data types appropriately.
- Selected important features:
  - `gender`, `SeniorCitizen`, `Partner`, `Dependents`, `tenure`
  - `Contract`, `PaymentMethod`, `InternetService`
  - `AvgMonthlyCost`, `NumServices`, `PaperlessBilling`

### ✔️ 2. Feature Engineering
- Created domain-relevant features (`AvgMonthlyCost`, `NumServices`).
- Encoded categorical variables using **One-Hot Encoding**.
- Scaled numerical features using **StandardScaler**.

### ✔️ 3. Model Training
- Tested multiple models: Logistic Regression,KNN,Decision Trees, Random Forest, XGBoost.
- Selected **XGBoost** as the final model due to best accuracy and balance between precision/recall.
- Used a full **Scikit-Learn Pipeline** combining preprocessing + model.

### ✔️ 4. Evaluation
- Evaluated using Accuracy, Precision, Recall, F1-Score, Confusion Matrix, ROC-AUC.
- Final model shows strong churn prediction performance.

### ✔️ 5. Deployment-Ready Pipeline
- Saved model as:  
  **`xgb_churn_pipeline.joblib`**
- Fully compatible with Flask API for production deployment.

---

## 📦 Project Structure

Customer-Churn-Analysis/

                       ├── Analysis using PowerBI/PowerBi file

                       ├── outputs/

                                  └── output1.png

                                  └── output2.png


                       ├── app/

                              └── app.py

                              └── templates/

                                           └── index.html

                              └── static/

                                        └── style.css

                              └── requirements.txt

                       ├──Customer Churn Analysis.ipynb

                       ├── README.md

                       └── telco_customer_churn.csv

---

## ⚙️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/UK183/Customer-Churn-Analysis.git
cd Customer-Churn-Analysis
```
### 2. Create a virtual environment 
```bash
python -m venv venv
```
### 3. Activate the environment 

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

### 4. Install Dependencies 
```bash
pip install -r requirements.txt
```

### 5. Run the flask app 
```bash
cd app
python app.py
```

Open in browser:
```bash
http://127.0.0.1:5000/
```

📈 Model Performance
Model	Result
XGBoost (Final Model)	≈ High accuracy (replace with your score)

See the notebook for full evaluation metrics: Precision, Recall, F1-score, Confusion Matrix, ROC-AUC.

### 🧰 Tools & Technologies

- Python, Pandas, NumPy

- Scikit-Learn (Pipeline, Preprocessing)

- XGBoost

- Matplotlib, Seaborn

- Flask (for deployment)

- Jupyter Notebook

### 💼 Business Value

This project helps telecom companies:

- Identify customers likely to churn

- Reduce revenue loss

- Improve customer retention strategies

- Target high-risk customers with personalized offers

- Build automated churn prediction systems and dashboards

### 🚀 Future Enhancements

- Add SMS/Call usage patterns

- Implement advanced hyperparameter tuning

- Deploy using Docker / AWS / Azure


---
### 👤 Author
[**Kazi Umar**](https://github.com/UK183)<br>
Linkedin profile: https://www.linkedin.com/in/umar-kazi18  
💼 Data Analyst | ML Engineer | Data Science & AI Enthusiast | Power BI | Python | SQL

