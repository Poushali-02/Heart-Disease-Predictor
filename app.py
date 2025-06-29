from flask import Flask, request, render_template
import joblib
import pandas as pd
app = Flask(__name__)


required_fields = [
        'age',	'anaemia',	'creatinine_phosphokinase',	'diabetes',	'ejection_fraction',	'high_blood_pressure',  'platelets',	'serum_creatinine',	'serum_sodium',	'sex',	'smoking',	'time'
    ]

@app.route('/')
def main():
    return render_template('index.html', required_fields=required_fields)

model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = []
        for field in required_fields:
            value = request.form.get(field)
            if value is None or value.strip() == '':
                return render_template('result.html', prediction_text=f"Missing value for {field}", color_class='error')
            try:
                features.append(float(value))
            except ValueError as e:
                return render_template('result.html', prediction_text=f"Invalid value for {field}\nError:{e}", color_class='error')
        input_data = pd.DataFrame([features], columns=required_fields)
        prediction = model.predict(input_data)[0]
        print(prediction)
        color_class = 'yes' if prediction == 1 else 'no'
        result = "High Risk of Heart Failure" if prediction == 1 else "Low Risk of Heart Failure"
        return render_template('result.html', prediction_text=result, color_class=color_class)

    except Exception as e:
        return render_template('result.html', prediction_text=f"Error: {e}", color_class='error')


if __name__ == '__main__':
    app.run(debug=True)