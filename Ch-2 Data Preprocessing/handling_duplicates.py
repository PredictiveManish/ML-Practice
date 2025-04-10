import pandas as pd
data = {'A':[1,2,2,3,4],
        'B':['X','Y','Y','Z','Z']}
df = pd.DataFrame(data)
print(f"Original DataFrame: {df}")

duplicates = df[df.duplicated()]
print(f"\nDuplicate rows: \n{duplicates}")

df_no_duplicates = df.drop_duplicates()
print(f"\nDataFrame after removing duplicates! \n{df_no_duplicates}")