import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

csvd = pd.read_csv('Daily.csv')

csvd.sort_values(['Gain or Loss'],inplace=True)

top25d = csvd.head(25)
print(top25d.corr())
sn.heatmap(top25d.corr(), annot=True)
plt.show()

bottom25d = csvd.tail(25)
print(bottom25d.corr())
sn.heatmap(bottom25d.corr(), annot=True)
plt.show()
csvw = pd.read_csv('Weekly.csv')

csvw.sort_values(['Gain or Loss'],inplace=True)

top25w = csvw.head(25)
print(top25w.corr())
sn.heatmap(top25w.corr(), annot=True)
plt.show()
bottom25w = csvw.tail(25)
print(bottom25w.corr())
sn.heatmap(bottom25w.corr(), annot=True)
plt.show()
csvm = pd.read_csv('Monthly.csv')

csvm.sort_values(['Gain or Loss'],inplace=True)

top25m = csvm.head(25)
print(top25m.corr())
sn.heatmap(top25m.corr(), annot=True)
plt.show()
bottom25m = csvm.tail(25)
print(bottom25m.corr())
sn.heatmap(bottom25m.corr(), annot=True)
plt.show()