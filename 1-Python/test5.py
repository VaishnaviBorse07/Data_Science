# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 08:20:23 2025

@author: vaish
"""
#1.	Create a heatmap of a correlation matrix for a dataset with numerical features.
#•	Use the iris dataset from Seaborn.
#•	Display the correlation matrix as a heatmap with annotations.
import seaborn as sns
import matplotlib.pyplot as plt

iris=sns.load_dataset("iris")
corr=iris.corr(numeric_only=True)
plt.figure(figsize=(8,6))
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.title("Correlation matrix")
plt.show()

#2.	Visualize the distribution of test scores for students
#   from three different schools.
#•	Data includes score and school columns.
#•	Use a box plot to compare distributions.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({'school': ['ABC', 'ABC','BAC', 'BAC','CAB', 'CAB'],'score': [20,25,25,30,30,35]})
plt.figure(figsize=(8, 6))
sns.boxplot(x='school', y='score', data=data)
plt.title('Test Score Distribution by School')
plt.xlabel('School')
plt.ylabel('Score')
plt.show()

#3.	Plot a bar chart showing the number of products sold by a 
#   store across five different categories.
#•	Categories: Electronics, Clothing, Groceries, Furniture, Toys
#•	Add color to each bar.
#•	Rotate x-axis labels and annotate the bars with their values.
#Note: Use below data
#categories = ['Electronics', 'Clothing', 'Groceries', 'Furniture', 'Toys']
#sales = [150, 200, 300, 120, 90]
#colors = ['blue', 'green', 'orange', 'red', 'purple']
categories = ['Electronics', 'Clothing', 'Groceries', 'Furniture', 'Toys']
sales = [150, 200, 300, 120, 90]
colors = ['blue', 'green', 'orange', 'red', 'purple']
plt.figure(figsize=(10, 6))
bars = plt.bar(categories, sales, color=colors)
plt.title('Products Sold by Category')
plt.xlabel('Category')
plt.ylabel('Number of Products Sold')
plt.xticks(rotation=45)
for bar in bars:
    height = bar.get_height()
    plt.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),xytext=(0, 2), textcoords="offset points", ha='center', va='bottom')

plt.show()


#4.	Create a line chart showing the monthly average temperature of a city over a year.
#•	x-axis: Months (January to December)
#•	y-axis: Temperature (in Celsius)
#•	Add a title, axis labels, and gridlines.
#•	Customize the line style (e.g., dashed, color, markers)

months = ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December']
temperature = [25,30,35,38,40,39,34,32,30,28,26,24]
plt.figure(figsize=(8, 6))
plt.plot(months, temperature, linestyle='dashed', color='purple', marker='o')
plt.title('Average Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

#5.	Using the tips dataset from Seaborn:
#•	Create a scatter plot showing the relationship between total_bill and tip.
#•	Color the points by sex and vary the size by size (number of people at the table).
#•	Add titles and axis labels.

tips = sns.load_dataset('tips')
plt.figure(figsize=(8, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex', size='size', alpha=0.5)
plt.title('Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.legend()
plt.show()





