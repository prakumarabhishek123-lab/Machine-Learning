# Cost function To implement  linear regresion using mean square error

# import Lib
import  numpy as np

# Actual data Input
actual_data=np.array([2,4,6,7,8,10,12,45])

# Predicted data 
predicted_data=np.array([1.1,1.2,2.3,4.5,6.1,2.1,2.15,5.3])

# calculate The square Error
square_error=(actual_data-predicted_data)**2

# calculate The mean Square Error
MSE=np.mean(square_error)

# print Error
print("Mean Square Error :",MSE)
