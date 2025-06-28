# 🩸 Heart Disease Risk Prediction - Logistic Regression

A simple and lightweight web application built with **Flask** and **Logistic Regression** that predicts the risk of heart disease based on patient medical data. This project is ideal for learning the integration of machine learning models with web development.

---

## 🔍 Description

This app takes clinical features such as age, diabetes status, blood pressure, and more as inputs, and returns a prediction of whether the patient is at risk of heart failure.

The model is trained using a **logistic regression algorithm** and saved using `joblib`. It is wrapped in a clean user interface using HTML and CSS.

---

## 📚 Dataset

* **Name**: Heart Failure Clinical Records Dataset
* **Source**: [Kaggle - by andrewmvd](https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data)

The dataset contains 12 features and a binary target variable (`DEATH_EVENT`), representing whether the patient experienced heart failure during follow-up.

---

## 🚀 How to Run on Your System

### 1. Clone the repository

```bash
git clone https://github.com/your-username/heart-disease-predictor.git
cd heart-disease-predictor
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask app

```bash
python app.py
```

Then, open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔎 Model Info

* **Model Type**: Logistic Regression (from `scikit-learn`)
* **Preprocessing**: StandardScaler
* **Serialized with**: `joblib`

If you wish to retrain the model, use the provided dataset and follow a similar pipeline. You can replace the `.pkl` file as needed.

---

## 💼 Credits

* Dataset by [andrewmvd on Kaggle](https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data)
* Developed and maintained by **Poushali**
* For educational and demo purposes only

---
