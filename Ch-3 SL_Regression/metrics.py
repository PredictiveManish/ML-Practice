import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

actual_values = np.array([5,10,15,20,25])
predicted_values = np.array([6,12,14,18,24])

# Mean Absolute error (MAE)
mae = mean_absolute_error(actual_values, predicted_values)
print("Mean Absolute error: ", mae)

# Mean Square Error
mse = mean_squared_error(actual_values, predicted_values)
print("Mean Squared Error: ", mse)

# Root Mean Squared Error
rmse = np.sqrt(mse)
print("Root Mean Squared Error: ", rmse)

# R-Squared Score (R2-score)
r_squared = r2_score(actual_values, predicted_values)
print("R2 Score: ", r_squared)

# Mean Absolute Percentage Error (MAPE)
mape = np.mean(np.abs((actual_values - predicted_values) / actual_values)) * 100
print("Mean Absolute Percentage Error", mape)