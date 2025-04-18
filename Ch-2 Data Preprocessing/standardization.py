import numpy as np
from sklearn.preprocessing import StandardScaler
data =np.array([[10,20],
                 [15,30],
                 [5,10],
                 [25,40]])
scaler = StandardScaler()
standardized_data = scaler.fit_transform(data)
print("Standardized data: ")
print(standardized_data)