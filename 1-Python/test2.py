# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 08:16:23 2025

@author: vaish
"""
#1.	Write a program to print numbers from 1 to 10 with single row with one tab space
for i in range(1,11):
    print(i,end=" ")

#2.	Write program to create dictionary where the keys are from 1 to 15 and values are from square of the numbers
def dict():
    return {i:i**2 for i in range(1,16)}
print(dict())

#3.Find out number is prime or not
def isprime():
    num=int(input("Enter num:"))
    if num > 1:  
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print("Number is not prime")
                break
        else:
            print("Number is prime")
isprime()

#4.Write the functions which will measure no. of vowels in sentence
def count_vowels(sentence):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    count = sum(1 for char in sentence if char in vowels)
    return count
sentence = input("Enter a sentence: ")
print(f"Number of vowels in the sentence: {count_vowels(sentence)}")

#5.	Find out gcd of two number 
def gcd(a,b):
    while b:
         a,b=b,a%b
    return a
a=int(input("Enter a:"))
b=int(input("Enter b:"))
gcd(a,b)

def isprime():
   for num in range(10,100):
      if num > 1:  
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print("Number is not prime:",num)
                break
        else:
            print("Number is prime:",num)
isprime()
