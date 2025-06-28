from flask import Flask, request, render_template
import joblib
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    model = joblib.load('model.pkl')
    prediction = model.predict([features])
    color_class = 'yes' if prediction == 1 else 'no'
    result = "High Risk of Heart Failure" if prediction == 1 else "Low Risk of Heart Failure"
    return render_template('result.html', prediction_text=result, color_class=color_class)

if __name__ == '__main__':
    app.run(debug=True)