import pandas as pd 
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

salariesData = pd.read_csv('Salary_Data.csv') #importing data from the CSV file

#splitting the data in to training and testing
X = salariesData.iloc[:, :-1].values 
Y= salariesData.iloc[:, 1].values

#splitting 1/3 of the data 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)

# Fitting Simple Linear Regression to the training set
reg = LinearRegression()
reg.fit(X_train, Y_train)

# Predicting the Test set result 
pred = reg.predict(X_test)

# Calculating the Mean_squared_error
mse = mean_squared_error(Y_test, pred)
print(mse)

#Visualising the Training set results and Test set results
plt.scatter(X_train, Y_train, color = 'blue')
plt.scatter(X_test, Y_test, color = 'red')
plt.title('Salary Data')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary')
plt.show()
