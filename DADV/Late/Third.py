import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

csvd = pd.read_csv('Daily.csv')
csvd.drop(csvd.columns[[0,10,11,12]], axis = 1, inplace = True)
csvd.dropna(how='any', axis=0, inplace=True)
csvd.sort_values(['Gain or Loss'],inplace=True,ascending=False)

top25d = csvd.head(25)
print(top25d.corr())
sn.heatmap(top25d.corr(), annot=True, cmap='coolwarm_r', vmin=0.0, vmax=1.0)
plt.show()

bottom25d = csvd.tail(25)
print(bottom25d.corr())
sn.heatmap(bottom25d.corr(), annot=True, cmap='coolwarm_r', vmin=0.0, vmax=1.0)
plt.show()

csvw = pd.read_csv('Weekly.csv')
csvw.drop(csvw.columns[[0,1,11,12,13]], axis = 1, inplace = True)
csvw.dropna(how='any', axis=0, inplace=True)
csvw.sort_values(['Gain or Loss'],inplace=True,ascending=False)

top25w = csvw.head(25)
print(top25w.corr())
sn.heatmap(top25w.corr(), annot=True, cmap='coolwarm_r', vmin=0.0, vmax=1.0)
plt.show()

bottom25w = csvw.tail(25)
print(bottom25w.corr())
sn.heatmap(bottom25w.corr(), annot=True, cmap='coolwarm_r', vmin=0.0, vmax=1.0)
plt.show()

csvm = pd.read_csv('Monthly.csv')
csvm.drop(csvm.columns[[0,1,11,12,13]], axis = 1, inplace = True)
csvm.dropna(how='any', axis=0, inplace=True)
csvm.sort_values(['Gain or Loss'],inplace=True,ascending=False)

top25m = csvm.head(25)
print(top25m.corr())
sn.heatmap(top25m.corr(), annot=True, cmap='coolwarm_r', vmin=0.0, vmax=1.0)
plt.show()

bottom25m = csvm.tail(25)
print(bottom25m.corr())
sn.heatmap(bottom25m.corr(), annot=True, cmap='coolwarm_r', vmin=0.0, vmax=1.0)
plt.show()