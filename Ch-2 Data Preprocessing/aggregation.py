import pandas as pd
data = {'Date':['2021-01-01','2021-01-01','2021-01-02','2021-01-02'],
        'Sales':[1000,1200,800,900]}
df = pd.DataFrame(data)
print(f"Original Dataframe: {df}")
aggregated_df = df.groupby('Date')['Sales'].sum().reset_index()
print("\nAggregatedDataFrame (Sum og Sales By Date):")
print(aggregated_df)