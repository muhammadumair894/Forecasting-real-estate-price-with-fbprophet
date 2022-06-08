
import matplotlib as mpl
import matplotlib.pyplot as plt
#import seaborn as sns
import numpy as np
import pandas as pd
plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

# Import Data
df = pd.read_csv('reducedList.csv', parse_dates=['Date'], index_col='Date')
df.reset_index(inplace=True)
df=df.dropna()
# Prepare data
df['year'] = pd.to_datetime([d.year for d in df.Date])
df['month'] = [d.strftime('%b') for d in df.Date]
years = pd.to_datetime(df['year'].unique())

# Prep Colors
np.random.seed(100)
mycolors = np.random.choice(list(mpl.colors.XKCD_COLORS.keys()), len(years), replace=False)
print('one')
# Draw Plot
plt.figure(figsize=(16,12), frameon=False, dpi= 80)
print('2')
for i, y in enumerate(years):
    if i > 0:
        plt.plot('month', 'Value', data=df.loc[df.year==y, :], color=mycolors[i], label=y)
        plt.text(df.loc[df.year==y, :].shape[0]-.9, df.loc[df.year==y, 'Value'][-1:].values[0], y, fontsize=12, color=mycolors[i])
print('3')
# Decoration
plt.gca().set(xlim=(0, 12), ylim=(0, 350), ylabel='$Values$', xlabel='$Month$')
plt.yticks(fontsize=12, alpha=.7)
plt.title("Seasonal Plot real estate Time Series", fontsize=20)
print('4')
plt.show()