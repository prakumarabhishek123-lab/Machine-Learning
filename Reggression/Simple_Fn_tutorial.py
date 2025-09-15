
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model

# Read CSV Data
Exel_data=pd.read_csv('C:\\Users\\praku\\OneDrive\\Desktop\\MAchine Learning Algo\\Reggression\\Salary_dataset.csv')

#Part Wise Distribution Like YearsExp And salary
plt.scatter(Exel_data['YearsExperience'],Exel_data['Salary'])
plt.xlabel('YearsExperience')
plt.ylabel('Salary')

# Find X and Y Because  CSv ME EXp,And Salary hai
X=Exel_data.iloc[:,1:2]
y=Exel_data.iloc[:,-1]

# Train To Data IN Split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=2) 

#Linear regression access To linear_model
model=linear_model.LinearRegression()

# fit Means Train data
model.fit(X_train,y_train)

# prediction data
model.predict(X_test.iloc[2].values.reshape(1,1))


