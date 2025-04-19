import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
# from mpl_toolkits.mpplot3d import Axes3d
X = np.array([[1,2,3],[2,3,4],[3,4,5],[4,5,6],[5,6,7]])
Y = np.array([5,8,11,14,17])

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

model = LinearRegression()

model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)
mse = mean_squared_error(Y_test,Y_pred)

intercept = model.intercept_
coefficients = model.coef_
print("Intercept",intercept)
print("Coefficients", coefficients)
print("Mean Squared Error",mse)