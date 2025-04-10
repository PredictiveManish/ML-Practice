import numpy as np
import pandas as pd

data = {'A':[1,2,np.nan, 4, 5],
        'B':[np.nan, 2, 3, np.nan, 5],
        'C':[1,2,3,4,5]}
df = pd.DataFrame(data)
print(f"Original DataFrame: {df}")
df['A']= df['A'].fillna(df['A'].mean())
df['B']=df['B'].fillna(df['B'].mean())

print(f"\nDataFrame after imputation: {df}")

