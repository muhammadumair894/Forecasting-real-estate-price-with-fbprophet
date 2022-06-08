import pandas as pd

df = pd.read_csv('reducedList.csv', parse_dates=['Date'])
df.head()