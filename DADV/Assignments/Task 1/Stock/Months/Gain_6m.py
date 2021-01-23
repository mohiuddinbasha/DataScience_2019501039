import pandas as pd

df = pd.read_csv('Output_Months.csv')

df['Close Jul 20'] = df['Close Jul 20'].str.replace(',', '').astype(float)
df['Close Jan 21'] = df['Close Jan 21'].str.replace(',', '').astype(float)

df['Gain'] = (df['Close Jan 21']/df['Close Jul 20'])-1

df.sort_values(['Gain'], inplace=True, ascending=False)

print(df.head(10))