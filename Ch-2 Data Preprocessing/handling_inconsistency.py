import pandas as pd
data = {'Category':['Electronics','Electronics','electronics','Clothing','clothing'],
       'Price':[500,600, 550, 40, 45]}
df = pd.DataFrame(data)
print(f"Original DataFrame: {df}")

df['Category'] =df['Category'].str.lower()
print(f"\nDataFrame after standardizing data \n{df}")
