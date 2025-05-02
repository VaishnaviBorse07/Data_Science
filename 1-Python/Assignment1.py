# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 2025

@author: vaish
"""

#write a program to check number is positive or negative or zero
num=int(input("Enter the number: "))
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")
    
    
#Write a program to check number is odd or even
num=int(input("Enter the number: "))
if num%2==0:
    print("Even.")
else:
    print("Odd.")    

#Given two non negative values print true if they have same last digits
num=int(input("Enter first number: "))
num1=int(input("Enter second number: "))
a=num%10
b=num1%10
if num>0 and num1>0:
    print(a==b)
else:
    print("negative number")
    
    
#Write a program to print numbers from 1 to 10 with single row with one tab space
for i in range(1,11):
    print(i,end=' ')

#write a program to print even numbers between 23 to 57.Each number should be printed in seperate row
for i in range(23,58):
    if i%2==0:
        print(i)
        
#write program to get prime numbers
def print_prime_numbers(start, end):
    for num in range(start, end + 1):
        if num > 1:  # Prime numbers are greater than 1
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                print(num)
start = int(input("Enter starting number for prime numbers: "))
end = int(input("Enter ending number for prime numbers: "))
print_prime_numbers(start, end)


# Print prime numbers between 10 and 99
print("Prime numbers between 10 and 99:")
print_prime_numbers(10, 99)

        
#write program to calculate sum of all digits
num = int(input("Enter the number: "))
total = 0
temp=num
while temp != 0:
    total += temp % 10 
    temp //= 10
print(f'Sum of digits is {total}')

    
#Write program to reverse the number
num = int(input("Enter the number: "))
reverse = 0
temp = num
while temp != 0:
    reverse = (reverse * 10) + (temp % 10)
    temp //= 10
print(f"Reversed number: {reverse}")


#Write program to check number is palindrome
def is_palindrome(num):
    temp = num
    reverse = 0    
    while temp != 0:
        reverse = (reverse * 10) + (temp % 10)
        temp //= 10
    return num == reverse
num = int(input("Enter the number: "))
if is_palindrome(num):
    print(f"{num} is a Palindrome")
else:
    print(f"{num} is not a Palindrome")
