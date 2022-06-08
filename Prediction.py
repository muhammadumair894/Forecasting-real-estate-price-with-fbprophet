import numpy
import pandas as pd

from sklearn.linear_model import LinearRegression
reg_model = LinearRegression()
import joblib

# Load the model from the file
Value = joblib.load('Value.pkl')

for i in Value:

    file = "model_" + str(i) + ".pkl"
    print(i)

# Use the loaded model to make predictions
#knn_from_joblib.predict(X_test)