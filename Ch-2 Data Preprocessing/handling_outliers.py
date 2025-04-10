import pandas as pd
import numpy as np
data = {'A':[10,20,30,120,25,40,9,100,200,60,70]}
df = pd.DataFrame(data)
print(f"Original Dataframe: {df}")

Q1 = df['A'].quantile(0.25)
Q3 = df['A'].quantile(0.75)
IQR = Q3-Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print(Q1)
print(Q3)
print(upper_bound, lower_bound)
df['A'] = np.where(df['A'] < lower_bound, lower_bound, df['A'])
df['A'] = np.where(df['A'] > upper_bound, upper_bound, df['A'])

print(f"\nDataFrame after removing outliers: {df}")