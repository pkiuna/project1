import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from sklearn import datasets, linear_model
from sklearn.metrics import r2_score

#load file and read
data= pd.read_csv('weather.csv')
#provide first five elements
data.head()
#data information
data.info()
#switch shape
(6000, 12)
data.size
list(data.columns)
data.describe(include='all') #union of attributes of each type

#drop unnecessary columns that are not needed in the dataset
data= data.drop(col,axis=1)
#change date from object to dateTimeObject

data['Formatted Date'] = pd.to_datetime(data['Formatted Date'])

#guide according to the time and date

myData = data.sort_values(by=['Formatted Date'])
#set
myData = myData.set_index('Formatted Date')
myData.index
#getting rid of repeats

myData.index.drop_duplicates(keep='first')
data.head()
data.info()
#Exploratory Data Analysis
#start plotting data

myData.plot(y="Temperature (C)", figsize=(30,30))
#using days as a sample into data format
myData2 = myData.resample(rule='D').mean()
myData2.head()
myData2.plot(y="Temperature (C)",figsize=(30,30))
#using month of january data to plot
January06 = myData['2006-01-01':'2006-01-31']
January06.plot(y=['Apparent Temperature (C)', 'Temperature (C)'], figsize=(30,30))

#seasons
winter1 = myData2['2006-12-01': '2006-12-31']
winterTwo = myData2['2006-01-01': '2006-03-31']
springTime = myData2['2006-04-01': '2006-05-31']
summerTime = myData2['2006-06-01':  '2006-08-31']

#plotting both winters

winter1.plot(y=['Temperature (C)','Apparent Temperature (C)'],figsize=(30,30))
winterTwo.plot(y=['Temperature (C)','Apparent Temperature (C)'],figsize=(30,30))

#spring plot
springTime.plot(y=['Temperature (C)','Apparent Temperature (C)'],figsize=(30,30))

#summer plot
summerTimeTime.plot(y=['Temperature (C)','Apparent Temperature (C)'],figsize=(30,30))

#visual for interrelationship using heatmap
plt.figure(figsize=(30,30))
sns.heatmap(data.corr(),annot=True)
plt.show()

#Complete Visualization
sns.jointplot('Temperature (C)', 'Apparent Temperature (C)',kind="reg", data=data)
sns.jointplot(y=data['Humidity'],x=myData['Temperature (C)'])
sns.jointplot(y=data['Pressure (millibars)'],x=data['Temperature (C)'])
sns.jointplot(y=data['Wind Speed'],x=data['Temperature (C)'])
sns.jointplot('Apparent Temperature (C)','Humidity',kind="reg", data=data)
sns.jointplot(y=data['Humidity'],x=data['Pressure (millibars)'])
sns.jointplot('Apparent Temperature (C)','Wind Speed)',data=data)






























