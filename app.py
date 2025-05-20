from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the trained Linear Regression model
with open("Artifacts/linear_regression_model.pkl", "rb") as file:
    model = pickle.load(file)

# Initialize Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get JSON input
    study_hours = np.array([data['Hours']]).reshape(-1, 1)

    # Make prediction
    prediction = model.predict(study_hours)[0]
    
    return jsonify({'Predicted Exam Score': round(prediction, 2)})

if __name__ == '__main__':
    app.run(debug=True)