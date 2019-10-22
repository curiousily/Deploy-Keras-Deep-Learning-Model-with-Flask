import joblib
import pandas as pd
from flask import Flask, jsonify, request
from tensorflow import keras

app = Flask(__name__)
model = keras.models.load_model("assets/price_prediction_model.h5")
transformer = joblib.load("assets/data_transformer.joblib")


@app.route("/", methods=["POST"])
def index():
    data = request.json
    df = pd.DataFrame(data, index=[0])
    prediction = model.predict(transformer.transform(df))
    predicted_price = prediction.flatten()[0]
    return jsonify({"price": str(predicted_price)})
