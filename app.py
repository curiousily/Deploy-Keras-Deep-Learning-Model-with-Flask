from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    content = request.json
    return jsonify(content)
