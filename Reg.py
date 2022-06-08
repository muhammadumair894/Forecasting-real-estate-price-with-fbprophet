import numpy
import pandas as pd

from sklearn.linear_model import LinearRegression
reg_model = LinearRegression()
import joblib

df = pd.read_csv("reducedList.csv")
df = df.fillna(0)

temp_Loc_2 = list(df['Location 2'].values)
mylist = list(dict.fromkeys(temp_Loc_2 ))

x = 1
for i in mylist:
  #var = 'is_' + i
  #print(i)
  var =  df['Location 2'] == i
  #df_ = 'df_' + i
  df_ = df[var]
  X = df_[['Var_1','Var_2','Var_3','Var_4','Var_5']].values
  y = df_['Value'].values
  reg_model.fit(X,y)
  # Save the model as a pickle in a file
  model_ = 'model_' + str(i) + '.pkl'
  joblib.dump(reg_model, model_)
  print(x)
  x = x + 1

print("Done")

