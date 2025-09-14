from sklearn import linear_model
import numpy as np

# Simple input data
X=np.array([[1],[2],[3],[4],[5]])

# crossponding Output data
y=np.array([2,4,5,4,5])

# create a linear regression model
model=linear_model.LinearRegression()

# fit data in The Model
model.fit(X,y)

# Make Predidction for new data 
X_new=np.array([[6]])

prediction=model.predict(X_new)

# Print Prididction
print("Prididction for X new :",prediction)