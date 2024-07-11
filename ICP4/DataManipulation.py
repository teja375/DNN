import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv') # reading CSV file 
df.head()
print(df.describe()) # describing the Statistical data 
df.fillna(df.mean(), inplace=True) # replacing the NULL values with mean
df[['Calories', 'Maxpulse']].agg(['min', 'max', 'count', 'mean']) # selecting two columns and aggregating the data
df[(df['Calories'] >= 500) & (df['Calories'] <= 1000)] # selecting rows between 500 and 1000
df[(df['Calories'] > 500) & (df['Pulse'] < 100)] # selecting rows greater than 500 and less than 1000
df_modified = df.drop('Maxpulse', axis=1) #contains all columns except Maxpulse
df = df.drop('Maxpulse', axis=1) #deleting 'Maxpulse Column from main dataframe
print(df)
df['Calories'] = df['Calories'].astype(int) # converting calories to int datatype
plt.scatter(df['Duration'], df['Calories']) #plotting the data using the matplot lib 
plt.xlabel("Duration") #xaxis
plt.ylabel("Calories") #yaxis
plt.show() # displaying the Scatter Plot