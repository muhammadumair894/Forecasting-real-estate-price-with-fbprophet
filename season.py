import matplotlib as mpl
import matplotlib.pyplot as plt
#import seaborn as sns
import numpy as np
import pandas as pd

fig, axes = plt.subplots(1,3, figsize=(20,4), dpi=100)
pd.read_csv('reducedList.csv', parse_dates=['Date'], index_col='Date').plot(title='Trend Only', legend=False, ax=axes[0])

pd.read_csv('reducedList.csv', parse_dates=['Date'], index_col='Date').plot(title='Seasonality Only', legend=False, ax=axes[1])

pd.read_csv('reducedList.csv', parse_dates=['Date'], index_col='Date').plot(title='Trend and Seasonality', legend=False, ax=axes[2])