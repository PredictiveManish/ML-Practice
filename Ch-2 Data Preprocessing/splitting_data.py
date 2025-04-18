import numpy as np
from sklearn.model_selection import train_test_split
X = np.random.rand(100,2)
y = np.random.randint(0,2,100)
print(X,y)
X_train, X_temp, y_train, y_temp = train_test_split(X,y,test_size=0.4,random_state=42)

X_valid, X_test,y_valid,y_test = train_test_split(X_temp, y_temp,test_size=0.4,random_state=42)
print("Training set size:",X_train.shape[0])
print("Validation set size:", X_valid.shape[0])
print("Test set size:",X_test.shape[0])