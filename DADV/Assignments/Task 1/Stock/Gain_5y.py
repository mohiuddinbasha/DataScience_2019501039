import pandas as pd

df = pd.read_csv('Output.csv')

df['Close 2016'] = df['Close 2016'].str.replace(',', '').astype(float)
df['Close 2021'] = df['Close 2021'].str.replace(',', '').astype(float)

df['Gain'] = (df['Close 2021']/df['Close 2016'])-1

df.sort_values(['Gain'], inplace=True, ascending=False)

print(df.head(10))


