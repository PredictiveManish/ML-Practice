import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
X = 2* np.random.rand(100,1)
y = 2 + 3 * X + 0.5 * X**2 + np.random.randn(100, 1)
degree = 2
X_poly = np.c_[X, X**2]
X_poly_with_bias = np.c_[np.ones((100,1)), X_poly]
theta_best = np.linalg.inv(X_poly_with_bias.T.dot(X_poly_with_bias)).dot(X_poly_with_bias.T).dot(y)

# Calculating resulting slope and intercept
slope = theta_best[1][0]
intercept = theta_best[0][0]

# Calculating the error
y_predict = X_poly_with_bias.dot(theta_best)
error = np.mean((y_predict - y)**2)

# Creating a range of X Values for prediction
X_new = np.linspace(0,2,100).reshape(-1,1)
X_new_poly = np.c_[np.ones((100,1)),X_new,X_new**2]

# Predict y values using the polynomial regression model
y_predict_new = X_new_poly.dot(theta_best)

# Plotting the original data points and the polynomial regression curve
plt.scatter(X, y, label='Data points')
plt.plot(X_new,y_predict_new, 'r-',label=f'Polynomial Regression (Degree {degree})')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Slope, intercept and error in the plot

plt.text(1.5, 8, f'Slope: {slope:.2f}\nIntercept: {intercept:.2f}\nError: {error:.2f}',fontsize=10,bbox=dict(facecolor='white',alpha=0.8))
plt.title('Polynomial Regression with slope, Intercept and Error')
plt.show()