# ETech-Project
***

## Goal/Functionality of this project

This project contains a python file "script.py" that makes a HTTP request based on a model that uses machine learning to train and predict based on the data set powerproduction. 

The jupyter notebook contains the data management portion of the project. It takes in the dataset and splits it into two sets X and Y. This is for comparison purposes so that the notebook can train and evaluate the data for making predictions in our webservice.

The script.py file is our webservice file. It contains some simple http post requests, which sends the data to the browser and contains some html and css to be more user friendly with the GUI.

A Docker file is available for distributing the program.

The html and css files are for the script.py file to display some data via the webservice.

A requirements.txt file is also included containing the technologies needed and is included in the Docker file as a parameter.

The model.h5 is our saved model from the jupyter notebook.

## Procedure for running the program

- The notebook should be run in its entirety first, allowing the model.h5 to be generated.
- once the model is made, the script.py can be run in the terminal using "python script.py"
- Alternatively the Docker file can be used as a platform for the program.

**Note to anyone correcting this project**

As of the current version there is an issue in sending the post to the browser:
- a 405 error is displayed or something does not want to work
- I've tried numerous fixes but none have worked.
- I decided due to time constraints with other deadlines that this would have to do and i apologize for the state I left it in.
- I hope that you will consider the work I put into the program sufficent to obtain some marks at least, I acknowledge that this submission is less than ideal, but i tried my best.

***

Some references for code and inspirations can be found in the jupyter notebook.
