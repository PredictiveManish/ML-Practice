import numpy as np
data = np.array([1,2,5,10,20,50,100])
transformed_data = np.log(data)

print(f"Original Data: {data}")

print(f"\nTransformed Data (Log Transformation): {transformed_data}")
