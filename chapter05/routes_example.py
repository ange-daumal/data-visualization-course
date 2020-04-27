from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/predict', methods=["POST"])
def pred():
    data = request.get_json()
    print(data)
    return jsonify({
        "msg": "Oui, c'est par ici la prédiction",
        "data": data
    })


if __name__ == "__main__":
    app.run(port=8053)
