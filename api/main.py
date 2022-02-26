from flask import Flask, jsonify, request
from flask_cors import CORS
from model_files.predict import predict_close


app = Flask("dogecoin-prediction-bot")
CORS(app)


@app.route('/', methods=['POST'])
def predict():
    key_dict = request.get_json()
    features = ['Open', 'High', 'Low', 'Close', 'Volume', '7day_open', '7day_close',
                '7day_high', '7day_low', '40day_open', '40day_close', '40day_high', '40day_low']
    inputs = []
    for feature in features:
        inputs.append(key_dict[feature])

    close = predict_close(inputs)
    response = {
        "close": close[0]
    }
    response = jsonify(response)
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
