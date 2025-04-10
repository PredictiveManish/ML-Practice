import pandas as pd
data = {'Category':['A','B','A','C','B','A']}
df = pd.DataFrame(data)
print(f"Original DataFrame: {df}")
# One Hot Encoding (love it is)
one_hot_encoded_df = pd.get_dummies(df, columns=['Category'],prefix=['Category'])
label_encoded_df = df.copy()
label_encoded_df['Category'] = df['Category'].astype('category').cat.codes

# Binary Encoding (using category codes to binary)

binary_encoded_df = df.copy()
binary_encoded_df['Category'] = df['Category'].astype('category').cat.codes.apply(lambda x:bin(x)[2:].zfill(2))

print(f"\nDataFrame after One-Hot Encoding: {one_hot_encoded_df}")
print(f"\nDataFrame after Label Encoding: {label_encoded_df}")
print(f"DataFrame after Binary Encoding: {binary_encoded_df}")