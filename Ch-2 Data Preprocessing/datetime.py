import pandas as pd
data = {'Date':['2022-01-15','2022-02-20','2022-03-25'],
        'Event':['Event A','Event B','Event C']}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
print(f"Original Dataframe: {df}")

df['Year'] = df['Date'].dt.year
df['Month'] = df['Month'].dt.month
df['Day'] = df['Date'].dt.day

referenced_date = pd.to_datetime('2022-01-01')
df['Days since Reference'] = (df['Date'] - referenced_date).dt.days
print(f"\nDataFrame after separation: \n{referenced_date}")