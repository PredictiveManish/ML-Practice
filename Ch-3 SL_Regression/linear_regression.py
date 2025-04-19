import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
X = np.array([1,2,3,4,5])
Y = np.array([2,4,5,4,5])

# Reshape X to a 2D array (required for scikit-learn)

X = X.reshape(-1,1)

# Create a linear regression model
model = LinearRegression()
model.fit(X,Y)
Y_pred = model.predict(X)

# Plotting
plt.scatter(X,Y,label='Data')
plt.plot(X,Y_pred,color='red',label='Regression Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Regression coefficients (intercepts and slope)
intercept = model.intercept_
slope = model.coef_
print(f'Intercept: {intercept}')
print(f'Slope: {slope}')