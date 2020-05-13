from flask import Flask, request, jsonify

from chapter05_solutions.stage02_model import train_model, get_model, predict

app = Flask(__name__)


@app.route('/model/train', methods=['GET'])
def api_train():
    train_model(get_model())
    return "Success"


@app.route('/model/predict', methods=['POST'])
def api_predict():
    data = request.json
    pred = predict([data['description']])[0]
    return jsonify({"result": pred})


if __name__ == '__main__':
    app.run(port=8053, debug=True)
