import pandas as pd
import numpy as np
import seaborn as sn
from itertools import combinations

csvm = pd.read_csv('Monthly.csv')
csvm.drop(csvm.columns[[0,1,11,12,13]], axis = 1, inplace = True)
csvm.dropna(how='any', axis=0, inplace=True)
csvm['Gain or Loss'] = csvm['Gain or Loss']/100
csvm.sort_values(['Gain or Loss'],inplace=True,ascending=False)

top25 = csvm.head(25)
bottom25 = csvm.tail(25)

top25_symbols = top25['Symbol'].tolist()
bottom25_symbols = bottom25['Symbol'].tolist()
symbols = []
for i in range(25):
    if top25_symbols[i] not in symbols:
        symbols.append(top25_symbols[i])
    if bottom25_symbols[i] not in symbols:
        symbols.append(bottom25_symbols[i])

dict_df = {}

for symbol in symbols:
    dataframe = csvm[csvm['Symbol'] == symbol]
    dict_df[symbol] = dataframe

samp = pd.DataFrame(columns=symbols,index=symbols)
for n1,n2 in combinations(symbols,2):
    df1 = dict_df[n1]
    df2 = dict_df[n2]
    l1 = df1['Gain or Loss'].tolist()
    l2 = df2['Gain or Loss'].tolist()
    samp.loc[n1,n2] = np.correlate(l1,l2)[0]
    samp.loc[n2,n1] = np.correlate(l2,l1)[0]
    samp.loc[n1,n1] = 1
    samp.loc[n2,n2] = 1
daily_samp = samp.astype({name:"float" for name in symbols})
def color(value):
  if value < 0:
    color = 'red'
  else:
    color = 'skyblue'
  return 'background-color: %s' % color
daily_samp = daily_samp.style.applymap(color)
print(samp)