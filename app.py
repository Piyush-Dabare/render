import numpy as np
import pandas as pd
from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to My Flask API!"})

@app.route('/get-data', methods=['GET'])
def get_data():
    n_records = 50
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)
    dates = pd.date_range(start=start_date, end=end_date).tolist()
    name = ["a",'b','df','wr','wert','24']
    # Sample Data
    data = {
    'Date': np.random.choice(dates, n_records),
    'name':np.random.choice(name, n_records),
    'phone': 0,
    }
    df = pd.DataFrame(data)
    json_obj = df.to_json(orient="records")
    return json_obj

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
