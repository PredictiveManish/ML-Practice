import pandas as pd
import numpy as np
data = {'Age':[25,30,35,40,45],
        'Income':[50000,60000,75000,80000,90000],
        'Education':['High School','Bachelor','Master','PhD','Bachelor']}
df = pd.DataFrame(data)
print(f"Original DataFrame: \n{df}")
# Creating new features
# 1. Age Group

df['Age_Group'] = pd.cut(df['Age'], bins = [0,30,40, np.inf],
                         labels = ['Young','Mid-Age','Old'])
# 2. Income Level
df['Income_level'] = pd.cut(df['Income'], bins = [0, 60000, 80000, np.inf],
                            labels=['Low','Medium','High'])

# Binary Education Indicator (bachelor or higher)
df['Bachelor or Higher'] = (df['Education'] !='High School').astype(int)
print(f"\nDataFrame after feature engineering: \n{df}")