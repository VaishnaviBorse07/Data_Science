# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 16:37:59 2025

@author: vaish
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

Salary_Data = pd.read_csv(r'E:\Vaishu coding\Data Science\2-Python\Salary_Data.csv')
Salary_Data.head()
sns.displot(Salary_Data.Salary,kde=True)  #here the kde is used to show the line of ditribution 
sns.jointplot(x=Salary_Data.Age,kde=True)
sns.pairplot(Salary_Data,kind='reg')
sns.displot(Salary_Data.Gender,kde=True)
sns.jointplot(x=Salary_Data.Age,y=Salary_Data.Salary,kind='hex')
Salary_Data.Age.value_counts()
sns.pairplot(Salary_Data,hue="Age")
sns.heatmap(Salary_Data.corr(numeric_only=True),annot=True)
sns.boxplot(Salary_Data.Salary)#their are outliers in total bill
sns.boxplot(Salary_Data.Age)
sns.countplot(x = 'Age' , data = Salary_Data)#highest number of customer are on saturday
sns.countplot(y = 'Gender' , data = Salary_Data)#male customer are more than female
Salary_Data.Gender.value_counts().plot(kind='pie')
Salary_Data.Gender.value_counts().plot(kind='bar')




import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df= pd.read_csv(r'E:\Vaishu coding\Data Science\2-Python\Mall_Customers.csv')
df.columns=['cust_id','Genre','Age','Annual_Income','Spend_Score']
df.head()
sns.displot(df.Age,kde=True)#20-25,30-35,50-55 are more
sns.displot(df.Annual_Income,kde=True)#middle-class 20-80 are more
sns.displot(df.Spend_Score,kde=True)#40-60 is more
sns.displot(df.Genre,kde=True)#female products more
df.dtypes
sns.pairplot(df,kind='reg')
sns.jointplot(x=df.Age,y=df.Annual_Income,kind='hex')
df.Age.value_counts()
sns.pairplot(df,hue="Age")
sns.heatmap(df.corr(numeric_only=True),annot=True)
sns.boxplot(df.Annual_Income)
sns.boxplot(df.Age)
sns.countplot(x = 'Age' , data = df)
sns.countplot(y = 'Genre' , data = df)
df.Genre.value_counts().plot(kind='pie')
df.Genre.value_counts().plot(kind='bar')




