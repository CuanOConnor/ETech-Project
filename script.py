from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from tensorflow.keras import backend
from tensorflow.keras.models import load_model

app = Flask(__name__)

# route the user to the index html file
@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

# get our model data and get the json the perform a model.predict() 
# and return the values as a list
@app.route('/predict', methods=['POST'])
def predict():
    data = float(request.get_json()["speed"])
    model = tf.keras.models.load_model("model.h5")

    predict = model.predict([data])
    predictions = predict.toList()

    return {'predict': predictions[0]}

def main():
    app.run(port=9099, debug=True)

if __name__ == '__main__':
    main()
