import pandas as pd
data = {'Age':[25,30,35,40,45,50,55,60,65,70],
        'Income':[50000,60000,75000,80000,90000,10000,110000,120000,130000,140000]}
df = pd.DataFrame(data)
print("Original DataFrame: ")
print(df)

# Binning and Discretization for age
age_bins = [20,40,60,80]
age_labels = ['Young','Mid-Age','Old']
df['Age Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)

# Binnning and Discretization for 'Income'
income_bins = [40000,80000,120000,160000]
income_labels = ['Low','Mid-level','High']
df['Income Level'] = pd.cut(df['Income'], bins=income_bins,labels=income_labels)

print("\nDataFrame after Binning & Discretization")
print(df)