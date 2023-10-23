from flask import Flask, request, jsonify
from joblib import load

app = Flask(__name__)
model = load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    prediction = model.predict([list(data.values())])
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)
