import numpy as np
import pandas as pd
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

# Sample Data
data = [
    {"id": 1, "name": "John Doe", "age": 30, "city": "New York"},
    {"id": 2, "name": "Jane Smith", "age": 25, "city": "Los Angeles"},
    {"id": 3, "name": "Alice Johnson", "age": 28, "city": "Chicago"}
]

@app.route('/')
def home():
    return jsonify({"message": "Welcome to My Flask API!"})

@app.route('/get-data', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
