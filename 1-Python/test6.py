# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 08:15:35 2025

@author: vaish
"""
#1. Write a function that takes a list of integers and
#returns a new list with only the even numbers, sorted
#in descending order.
def desc_order(numbers):
    return sorted([num for num in numbers if num % 2 == 0], reverse=True)
numbers=[1,2,3,4,6,7]
print(desc_order(numbers))

#2. Write a program that takes a user's full name as 
#input and outputs their initials in uppercase (e.g., Virat Kohli → V.K.).
name = input("Enter Full Name(Name & Surname): ")
initials = '.'.join([fullname[0].upper() for fullname in name.split()]) + '.'
print(initials)

#3. Write a function to generate the first n 
#Fibonacci numbers using a loop.
def Fibonacci(n):
     fibonacci = [0, 1]
     for _ in range(2,n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
     return fibonacci[:n]
n=int(input("Enter the value of n:"))
print(Fibonacci(n))

#4. Write a script that reads a .txt file and 
#counts the number of lines, words, and characters.
def count_file(filename):
    with open(filename,'r')as file:
        text = file.read()
    lines = text.splitlines()
    words = text.split()
    return len(lines), len(words), len(text)
filename="E:/Vaishu coding/Data Science/1-Python/programming.txt"
print(count_file(filename))


#5. Create a decorator named timer_decorator that times 
#how long a function takes to execute.


#6. Given a list of dictionaries with student info
# ({'name': ..., 'score': ...}), return names of students 
#with score > 75.
def top_students(students):
    return [s['name'] for s in students if s['score'] > 75]
n = int(input("Enter the number of students: "))
students = []
for _ in range(n):
    name = input("Enter student name: ")
    score = int(input("Enter student score: "))
    students.append({'name': name, 'score': score})
result = top_students(students)
print("Students with score > 75:", result)

#7. Given a list of tuples (name, age), sort them by 
#age using a lambda function.
data = [("lisa", 90), ("Bobbi", 35), ("Charles", 65)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)

#8. Write a generator function that yields prime numbers 
#less than n.
def prime_generator(n):
    for num in range(2, n):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            yield num
n = int(input("Enter the number: "))
for prime in prime_generator(n):
    print(prime)

#9. Load a employee.csv file, filter rows where column 
#"salary" is above the median, and show the top 5.
import pandas as pd
df =pd.read_csv(r"E:\Vaishu coding\Data Science\1-Python\employees.csv")
median_salary = df['salary'].median()
filtered = df[df['salary'] > median_salary]
print(filtered.head(5))

#10. Load a data.csv file with missing values. 
#Show how to fill missing numerical values with the column mean.
import pandas as pd
df = pd.read_csv(r"E:\Vaishu coding\Data Science\1-Python\data.csv")
df.fillna(df.mean(numeric_only=True), inplace=True)
print(df)

#11. Plot a bar chart showing average scores of students per subject
# from a given DataFrame.
# data = {'Math': [90, 85, 88], 'Science': [80, 82, 84], 'English': [78, 75, 80]}
import matplotlib.pyplot as plt
import pandas as pd
data = {'Math': [90, 85, 88], 'Science': [80, 82, 84], 'English': [78, 75, 80]}
df = pd.DataFrame(data)
df.mean().plot(kind='bar')
plt.xlabel('subject')
plt.ylabel('Average')
plt.show()

#12. Compute and visualize the correlation matrix using seaborn.
# Note : Use the dataframe from Qu.11.
import seaborn as sns
data = {'Math': [90, 85, 88], 'Science': [80, 82, 84], 'English': [78, 75, 80]}
df = pd.DataFrame(data)
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()


#13. Given a text, extract all valid email addresses using regex.
#text = "For more details, Please contact us at support@sanjivani.com or admin-info@sanjivani.co.ind."
import re
text = "For more details, Please contact us at support@sanjivani.com or admin-info@sanjivani.co.ind."
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print(emails)

#14. Write a function that checks if a given string is 
#a valid phone number (format: XXX-XXX-XXXX).
#Check for these numbers:  987-654-3210 & 12-3456-7890
def is_valid_phone(number):
    return bool(re.match(r'^\d{3}-\d{3}-\d{4}$', number))

print(is_valid_phone("12-3456-7890"))
print(is_valid_phone("987-654-3210"))

#15. Replace all digits in a string with #.
#text = "My phone number is 1234567890."
text = "My phone number is 1234567890."
new_text = re.sub(r'\d', '#', text)
print(new_text)


