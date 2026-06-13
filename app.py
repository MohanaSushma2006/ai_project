from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS

# Create app
app = Flask(__name__)
CORS(app)  # Allow frontend requests

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Home route (optional)
@app.route('/')
def home():
    return "Placement Predictor API Running 🚀"

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    cgpa = data['cgpa']
    skills = data['skills']
    projects = data['projects']

    # Model prediction
    prediction = model.predict([[cgpa, skills, projects]])

    return jsonify({
        "result": int(prediction[0])
    })

# Run server
if __name__ == '__main__':
    app.run(debug=True)