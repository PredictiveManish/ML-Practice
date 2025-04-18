import numpy as np
from sklearn.preprocessing import MinMaxScaler
data = np.array([[10,20],
                 [15,30],
                 [5,10],
                 [25,40]])
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data)

print("Normalized data: ")
print(normalized_data)