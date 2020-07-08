import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  #libraries and dependencies
import seaborn as sns
df = pd.read_csv("customer.csv")
#plotting age frequency from dataset
plt.figure(figsize=(12,10))
plt.title("frequency of ages")
sns.boxplot(y=df["Age"])  #using box plot to view differences
plt.show()
#plotting annual income and spending
plt.figure(figsize=(12,10))
plt.subplot(1,3,1)
sns.boxplot(y=df["The spending Score (1-200)"])  #Creating Y axis
plt.subplot(1,3,3)
sns.boxplot(y=df["The Annual Income $"])     #Y axis for both Box Plots
plt.show()
#checking difference between gender in dataset
Genders = df.Genders.value_counts()
plt.figure(figsize=(12,10))
sns.barplot(x=genders.index, y=genders.values)
plt.show()

#plotting number of customers using different Age groups to see differences
age18to27 = df.Age[(df.Age <= 27) & (df.Age >= 18)]
age28to37 = df.Age[(df.Age <= 37) & (df.Age >= 28)]
age38to47 = df.Age[(df.Age <= 47) & (df.Age >= 38)]
age48to57 = df.Age[(df.Age <= 57) & (df.Age >= 48)]
age58above = df.Age[df.Age >= 58]
x = ["18-27","28-37","38-47","48-57","58+"]
y = [len(age18to27.values),len(age28to37.values),len(age38to47.values),len(age48to57.values),len(aage58above.values)]
#graphing values
plt.figure(figsize=(20,20))
sns.barplot(x=x, y=y,)
plt.title("Customer ages and numbers")   #naming graph axis
plt.xlabel("Ages")
plt.ylabel("Customers")
plt.show()
#plotting spending scores for customers
spending1to30 = df["Spending Score "][(df["Spending Score "] >= 1) & (df["Spending Score "] <= 30)]
spending31to60 = df["Spending Score "][(df["Spending Score "] >= 31) & (df["Spending Score "] <= 60)]
spending61to100 = df["Spending Score "][(df["Spending Score "] >= 61) & (df["Spending Score "] <= 100)]
spendingX = ["1-30", "31-60", "61-100"]
spendingY = [len(spending1to30.values), len(spending31to60.values), len(spending61to100.values)]
plt.figure(figsize=(20,20))
sns.barplot(x=spendingX, y=spendingY)
plt.title("scores for spending")
plt.xlabel("Score")
plt.ylabel("customers with score")
plt.show()
#bar plot for customers according to annual income

annualIncome0to40 = df["Annual Income "][(df["Annual Income "] >= 0) & (df["Annual Income "] <= 40)]
annualIncome41to80 = df["Annual Income "][(df["Annual Income "] >= 41) & (df["Annual Income "] <= 80)]
annualIncome81to120 = df["Annual Income "][(df["Annual Income "] >= 81) & (df["Annual Income "] <= 120)]
annualIncome121to160 = df["Annual Income "][(df["Annual Income "] >= 121) & (df["Annual Income "] <= 160)]


annualIncomeX = ["$ 0 - 40,000", "$ 40,001 - 80,000", "$ 81,001 - 120,000", "$ 121,00 - 160,000"]
annualIncomeY = [len(annualIncome0to40.values), len(annualIncome41to80.values), len(annualIncome81to120.values), len(annualIncome121to160.values)]
plt.figure(figsize=(20,20))
sns.barplot(x=annualIncomeX, y=annualIncomeY, palette="Set2")
plt.title("Incomes")
plt.xlabel("Income range")
plt.ylabel("customers")
plt.show()
#plot to compare WCSS against clusters numbers for K Value get the clusters value
from sklearn.cluster import KMeans
withinClusterSum=[]
for k in range (1,10):
    kMeans = KMeans(n_clusters=k, init="k-means++")
    withinClusterSum.append(kmeans.inertia_) #maximing number of clusters
plt.figure(figsize=(12, 6))
plt.grid()
plt.plot(range(1,10))  #plotting grid
plt.xlabel("K Value")
plt.ylabel("Within Cluster Sum of Squares")
plt.show()
#elbow method for different values of K

knn = KMeans(n_clusters=5)  #chose 5 to be the k value to use for elbow method
cluster = knn.fit_predict(df.iloc[:,2:])  #scalar integers
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig = plt.figure(figsize=(20,20))

ax = fig.add_subplot(132, projection='3d')  #made a 3d plot for a better visual of spending score relating to annual income
ax.scatter(df.Age[df.label == 0], df["Annual Income "][df.label == 0], df["Spending Score "][df.label == 0], s=30)
ax.scatter(df.Age[df.label == 1], df["Annual Income "][df.label == 1], df["Spending Score "][df.label == 1], s=40)
ax.scatter(df.Age[df.label == 2], df["Annual Income "][df.label == 2], df["Spending Score "][df.label == 2], s=50)
ax.scatter(df.Age[df.label == 3], df["Annual Income "][df.label == 3], df["Spending Score "][df.label == 3], s=60)
ax.scatter(df.Age[df.label == 4], df["Annual Income "][df.label == 4], df["Spending Score "][df.label == 4], s=70)
ax.view_init(40, 180)
plt.xlabel("Ages")
plt.ylabel("Annual Income")
ax.set_zlabel('Spending Score')

plt.show()






































