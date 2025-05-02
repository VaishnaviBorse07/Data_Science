# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 08:15:51 2025

@author: vaish
"""

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r"E:\Vaishu coding\Data Science\2-Python\Salary_Data.csv")
df.columns = ['Age','Gender','Education','Job','Exp','Salary']

#histogram
plt.hist(df.Age,bins =10,edgecolor = 'black',alpha = 0.7)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
#here we have observed that there are more people
#working in office who has the age in between
#25-29

#histogram for work of experience
plt.hist(df['Exp'],bins = 20,color = 'lightgreen',
         edgecolor = 'black')
plt.title('Exp Distribution')
plt.xlabel('Exp')
plt.ylabel('distinquision')
plt.show()

#scatter
plt.scatter(df['Exp'],df['Salary'],color='purple',edgecolor='purple',alpha = 0.6)
plt.title('Exp vs Salary')
plt.xlabel('Exp')
plt.ylabel('Salary')
plt.show()

#correlation
corr = df.corr(numeric_only = True)
plt.imshow(corr, cmap = 'coolwarm', interpolation = 'none')
plt.colorbar()
plt.xticks(range(len(corr)),corr.columns,rotation = 30)
plt.yticks[range(len(corr)),corr.columns]
plt.title('Correaltion Matrix')
plt.show()

#boxplot
plt.boxplot(df['Salary'])
plt.title('Boxplot - Salary')
plt.show()

plt.boxplot(df['Age'])
plt.title('Boxplot - Age')
plt.show() 

#bargraph
df['Age'].value_counts().plot(kind = 'bar',color = 'orange')
plt.title('Age wise Salary')
plt.xlabel('Salary')
plt.ylabel('Age')
plt.show()

#7.Count of Gender
df['Gender'].value_counts().plot(kind = 'bar',color ='lightblue')
plt.title('Count by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

#piechart
df['Gender'].value_counts().plot(kind = 'pie',autopct = '%1.1f%%')
plt.title('Gender Distribution')
plt.ylabel('')
plt.show()

########################################################
import matplotlib.pyplot as plt
import pandas as pd

df= pd.read_csv(r'E:\Vaishu coding\Data Science\2-Python\Mall_Customers.csv')
df.columns=['cust_id','Genre','Age','Annual_Income','Spend_Score']

#histogram
plt.hist(df.Age,bins =10,edgecolor = 'black',alpha = 0.7)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()#20-25,35-40,50-55 age people are more

#histogram for annual income
plt.hist(df['Annual_Income'],bins = 10,alpha=0.7,color = 'skyblue',
         edgecolor = 'black')
plt.title('Annual Income Distribution')
plt.xlabel('Annual Income')
plt.ylabel('Frequency')
plt.show()

plt.hist(df['Spend_Score'],bins = 10,alpha=0.7,color = 'purple',
         edgecolor = 'black')
plt.title('Spend Score Distribution')
plt.xlabel('Spend Score')
plt.ylabel('Frequency')
plt.show()

#scatter plot(replacing jointplots)
plt.scatter(df['Age'],df['Annual_Income'],color='purple',edgecolor='purple',alpha = 0.6)
plt.title('Age vs Annual_Income')
plt.xlabel('Age')
plt.ylabel('Annual_Income')
plt.show()

plt.scatter(df['Age'],df['Spend_Score'],color='purple',edgecolor='purple',alpha = 0.6)
plt.title('Age vs Spend_Score')
plt.xlabel('Age')
plt.ylabel('Spend_Score')
plt.show()
corr = df.corr(numeric_only = True)
#correlation
corr = df.corr(numeric_only = True)
plt.imshow(corr, cmap = 'coolwarm', interpolation = 'none')
plt.colorbar()
plt.xticks(range(len(corr)),corr.columns,rotation = 30)
plt.yticks[range(len(corr)),corr.columns]
plt.title('Correaltion Matrix')
plt.show()

#boxplot
plt.boxplot(df['Spend_Score'])
plt.title('Boxplot - Spend_Score')
plt.show()

plt.boxplot(df['Age'])
plt.title('Boxplot - Age')
plt.show() 

#bargraph
df['Age'].value_counts().plot(kind = 'bar',color = 'red')
plt.title('Age wise Annual_Income')
plt.xlabel('Annual_Income')
plt.ylabel('Age')
plt.show()

#7.Count of Gender
df['Genre'].value_counts().plot(kind = 'bar',color ='lightblue')
plt.title('Count by Genre')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.show()

#piechart
df['Genre'].value_counts().plot(kind = 'pie',autopct = '%1.1f%%')
plt.title('Genre Distribution')
plt.ylabel('')
plt.show()

#Scatter plot ith regression line
from numpy.polynomial.polynomial import polyfit
x=df.Age
y=df.Spend_Score
b,m=polyfit(x,y,1)
plt.scatter(x,y,alpha=0.5)
plt.plot(x,m*x+b,color='red')
plt.title('Age vs Spend Score with trend line')
plt.xlabel('Age')
plt.ylabel('Spend Score')
plt.show()

#Pairwise scatter matrix (subset of features)
pd.plotting.scatter_matrix(df[['Age','Annual_Income','Spend_Score']],figsize=(8,8))
plt.suptitle('Pairwise Scatter Matrix')
plt.show()

#Gender distribution
gender_counts=df.Genre.value_counts()

#Pie Chart
gender_counts.plot(kind='pie',autopct='%1.1f%%',startangle=90)
plt.ylabel()
plt.title('')
plt.show()#female customer are more than male

#Bar chart
gender_counts.plot(kind='bar',color=['skyblue','salmon'])
plt.title('Gender Count')
plt.ylabel('Count')
plt.show()

#correlation heatmap
corr =df[['Age','Annual_Income','Spend_Score']].corr()
plt.imshow(corr,cmap='coolwarm',interpolation='none')
plt.colorbar()
plt.xticks(range(len(corr)),corr.columns,rotation=45)
plt.yticks(range(len(corr)),corr.columns)
plt.title('Correlation Heatmap')
plt.show()# spending score and annual income slightly correlated
# spending score and age negatively slightly correlated
# age score and annual income slightly correlated