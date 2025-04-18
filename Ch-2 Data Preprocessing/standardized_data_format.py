import pandas as pd
data = {'Date':['2021-01-15','2021-02-20','2021-03-25'],
        'Amount':['$100.50','200.75 USD','300.00'],
        'Quantity':['5','3','7.5 kg']}
df = pd.DataFrame(data)
print("Original DataFrame: ")
print(df)

# Standardized data formats
# Converting 'Date' Column to datetime format
df['Date'] = pd.to_datetime(df['Date'])
df['Amount'] = df['Amount'].replace('[\$,]','',regex=True)
df['Quantity'] = df['Quantity'].replace('[a-zA-Z\,]','',regex=True).astype(float)
print("\nDataFrame after standardizing data formats:")
print(df)