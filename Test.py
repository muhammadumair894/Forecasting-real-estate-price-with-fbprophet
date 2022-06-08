from sklearn.linear_model import LinearRegression
reg_model = LinearRegression()
import joblib
import numpy as np

Location =  (input("Enter Location 2: "))
var_1 = int (input("Enter Variable 1: "))
var_2 = float (input("Enter Var 2 RATIO Close Price By List Price: "))
var_3 = float (input("Enter Var 3 RATIO Close Price By Original List Price: "))
var_4 = int (input("Enter Var 4 Seller Contributions: "))
var_5 = int (input("Enter Var 5 MO: "))

model_name = 'model_' + Location + '.pkl'

model_load = joblib.load(model_name)
# Use the loaded model to make predictions
print("The Predicted Value: ")
print(model_load.predict(np.array([[var_1, var_2, var_3, var_4,	var_5]])))

#Install module as instructed
#Setting >> project >> project interpretor