import pickle
import xgboost as xgb
from flask import Flask
from flask import request
from flask import jsonify
import numpy as np

model_file = 'model_eta=0.07.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('loandefault-prediction')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    D = xgb.DMatrix(X)
    y_pred = model.predict(D)
    default = y_pred >= 0.5

    result = {
        'DefaultChances': float(y_pred),
        'Defaulted': bool(default)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9695)