from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
vec, clf = joblib.load("model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    text = request.json['text']
    X = vec.transform([text])
    pred = clf.predict(X)[0]
    result = "positive" if pred == 1 else "negative"
    return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
