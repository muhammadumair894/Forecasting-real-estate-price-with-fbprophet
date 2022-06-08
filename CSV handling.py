import pandas as pd
import joblib
filterlist = joblib.load('Filter_List.pkl')
#C:\Users\muham\PycharmProjects\Adeel_Regression_19_1_21\csvdata\75022.csv
for i in filterlist:
    df = pd.read_csv(str(int(i)) + '.csv')
    df.rename(columns={'ds': 'Date', 'yhat': 'Average Price', 'yhat_lower': 'Lower Price','yhat_upper':'Upper Price'}, inplace=True)
    df.to_csv(str(int(i)) + 'Updated' + '.csv', index= False)