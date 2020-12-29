import os
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from tensorflow.keras import backend
from tensorflow.keras.models import load_model

app = Flask(__name__)
port = int(os.getenv("PORT", 9099))


@app.before_first_request
def load_model_to_app():
    app.predictor = load_model(os.path.join("model.h5"))
	#print(model) #debug

@app.route("/")
def index():
    return render_template('index.html', pred = 0)

@app.route('/predict', methods=['POST'])
def predict():
    data = [request.form['speed'],
            request.form['power']]

    data = np.array([np.asarray(data, dtype=float)])

    predictions = app.predictor.predict(data)
    print('INFO Predictions: {}'.format(predictions))

    class_ = np.where(predictions == np.amax(predictions, axis=1))[1][0]

    return render_template('index.html', pred=class_)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port, debug=False)
