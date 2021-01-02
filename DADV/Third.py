import pandas as pd

csvd = pd.read_csv('Daily.csv')

csvd.sort_values(['Gain or Loss'],inplace=True)

top25d = csvd.head(25)
print(top25d.corr())

bottom25d = csvd.tail(25)
print(bottom25d.corr())

csvw = pd.read_csv('Weekly.csv')

csvw.sort_values(['Gain or Loss'],inplace=True)

top25w = csvw.head(25)
print(top25w.corr())

bottom25w = csvw.tail(25)
print(bottom25w.corr())

csvm = pd.read_csv('Monthly.csv')

csvm.sort_values(['Gain or Loss'],inplace=True)

top25m = csvm.head(25)
print(top25m.corr())

bottom25m = csvm.tail(25)
print(bottom25m.corr())
