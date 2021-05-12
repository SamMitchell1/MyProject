import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('threedigitcomp_01.xpd', comment='#')

print(data.groupby('block').describe())

sns.catplot(x='block', y='RT', kind="box", data=data)


data = pd.read_csv('fourdigitcomp_01.xpd', comment='#')

print(data.groupby('block').describe())

sns.catplot(x='block', y='RT', kind="box", data=data)
plt.show()