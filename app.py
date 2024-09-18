from flask import Flask, jsonify
from ml_model.model import train_model

app = Flask(__name__)

@app.route('/')
def index():
    accuracy = train_model()
    return jsonify({"message": f"Model Accuracy: {accuracy:.2f}"}), 200

if __name__ == '__main__':
    app.run(debug=True)
