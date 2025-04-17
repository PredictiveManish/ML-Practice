import pandas as pd
data_source1 = {'ID': [1,2,3],
                'Name':['Alice','Bob','Carol']}
data_source2 = {'ID': [4,5,6],
                'Name':['Manish','Om','Gautam']}
df1 = pd.DataFrame(data_source1)
df2 = pd.DataFrame(data_source2)

df = pd.concat([df1,df2],ignore_index=True)
print(df)