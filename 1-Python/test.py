# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 08:17:07 2025

@author: vaish
"""

#1.even number
for i in range(23,58):
    if i%2==0:
        print(i)

#2.prime number
def is_prime(start,end):
    for num in range(start,end+1):
      if num>1:
         for i in range(2,int(start**0.5)+1):      
            if num % i==0:
               break
         else:
            print(num)
is_prime(10,100)   


#3.palindrome
def is_palindrome(num): 
    temp=num
    reverse=0
    while temp!=0:
        reverse=(reverse*10)+(temp%10)
        temp//=10
    return num==reverse
num=int(input("Enter number:"))
if is_palindrome(num):
    print("Palindrome")
else:
    print("Not palindrome")


    