# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 08:09:43 2025

@author: vaish
"""
'''
Write a Python function named collect_employee_details() that collects details of a 
specified number of employees. The function should: 
1. Prompt the user to enter the number of employees (residents). 
2. For each employee, collect: 
o Name 
o Age 
o Designation 
o Band (should be one of 'A', 'B', 'C', or 'D'; case-insensitive input but stored in 
uppercase) 
3. Validate the following: 
o Number of residents must be greater than 0. 
o Age must be between 21 and 58 (both inclusive). 
o Band must be one of 'A', 'B', 'C', or 'D'. 
If any validation fails, print "Invalid" and terminate the function immediately.
'''
def collect_employee_details(n):
    if n <= 0:
        print("Invalid")
        return

    for i in range(n):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        if age < 21 or age > 58:
            print("Invalid")
            return

        designation = input("Enter designation: ")
        band = input("Enter band (A/B/C/D): ").upper()
        if band not in ['A', 'B', 'C', 'D']:
            print("Invalid")
            return

    print("Employee details collected successfully.")

num = int(input("Number of residents: "))
collect_employee_details(num)


'''Write a Python function longest_negative_sum(input1, input2) that takes two 
parameters: 
 input1: A list of integers. 
 input2: (length of list) 
Your task is to identify all contiguous negative number sequences in the list input1, and: 
1. Find the longest such sequence(s) (i.e., the ones with the most consecutive negative 
numbers). 
2. If multiple sequences share the same maximum length, include all of them. 
3. Calculate and return the sum of the individual sums of these longest sequences. 
4. If there are no negative numbers, return -1.
'''
lst=[1, 2, 3, 4] 
lst=[-1, -2, -3, 4, -1, -2] 
lst=[4, -1, -2, 3, -4, 5] 
lst=[4, -1, -2, 0, -3, -4] 
lst=[-5] 
lst=[-1, -2, 0, 1, -2, 0, -1, -2] 
lst=[] 
lst=[-1, -2, -3, 4, -5] 
lst=[1, -1, -2, 3, -3, -4, 5, -5, -6]
curr_len=0
curr_sum=0
max_len=0
longest_sums=0
for num in lst:
    if num<0:
        curr_len+=1
        curr_sum+=num
    else:
        if curr_len >0:
            if curr_len>max_len:
                max_len=curr_len
                longest_sums=[curr_sum]
            elif curr_len==max_len:
                longest_sums.append(curr_sum)
            curr_len=0
            curr_sum=0
if curr_len>0:
    if curr_len>max_len:
        max_len=curr_len
        longest_sums=[curr_sum]
    elif curr_len==max_len:
        longest_sums.append(curr_sum)
print(sum(longest_sums)if longest_sums else -1)