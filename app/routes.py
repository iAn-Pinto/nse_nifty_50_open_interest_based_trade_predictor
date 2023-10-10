from app import app
from flask import jsonify
import random

def fetch_option_chain_data():
    return {
        'call_open_interest': random.randint(1000, 5000),
        'put_open_interest': random.randint(1000, 5000)
    }

def predict_buy_or_sell(data):
    if data['call_open_interest'] > data['put_open_interest']:
        return 'SELL'
    else:
        return 'BUY'

@app.route('/predict', methods=['GET'])
def get_prediction():
    data = fetch_option_chain_data()
    prediction = predict_buy_or_sell(data)
    return jsonify({
        'data': data,
        'prediction': prediction
    })
