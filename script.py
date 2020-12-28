import os
from tensorflow.keras.models import load_model
import numpy as np
import flask

app = flask.Flask(__name__)
port = int(os.getenv("PORT", 9099))

model = load_model(os.path.join("model.h5"))

@app.route('/predict', methods=['POST'])
def predict():
	features = flask.request.get_json(force=True)['features']
	prediction = model.predict([features])[0,0]
	response = {'prediction': prediction}

	return flask.jsonify(response)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port)
