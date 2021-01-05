# ETech-Project
***

## Goal/Functionality of this project

This project contains a python file "script.py" that makes a HTTP request based on a model that uses machine learning to train and predict based on the data set powerproduction. 

The jupyter notebook contains the data management portion of the project. It takes in the dataset and trains the model, displaying 100 epochs and their associated loss values.

The script.py file is our webservice file. It contains some simple http post requests, which sends the data to the browser and contains some html and css to be more user friendly with the GUI.

A Docker file is available the program.

The html files are for the script.py file to display some data via the webservice.

A requirements.txt file is also included containing the technologies needed and is included in the Docker file as a parameter.

The model.h5 is our saved model from the jupyter notebook.

## Procedure for running the program

- The notebook should be run in its entirety first, allowing the model.h5 to be generated.
- once the model is made, the script.py can be run in the terminal using "python script.py"
- Alternatively the Docker file can be used as a platform for the program.

**Note**

As of the current version there is a known issue in sending the post to the browser:
- The page is displayed and the functionality is all there, however the HTML does not update with the predicted speed value.
- time constraints with other deadlines prevented me being able to spend time fixing it.
***

### *References*

[1] Some inspiration for web service was taken from here; https://www.datacamp.com/community/tutorials/machine-learning-models-api-python

[2] info on async functions; https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function

[3] info on keras methods and functions adapted for the project; https://www.tensorflow.org/api_docs/python/tf/keras/Model
