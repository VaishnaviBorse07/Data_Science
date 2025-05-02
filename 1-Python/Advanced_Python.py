# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 21:51:48 2025

@author: vaish
"""
#pre- requisite to decorators

def plus_one(number):
    number1 = number + 1 
    return number1
plus_one(5) #output : 6

#############################################
#Defining Functions Inside other function

def plus_one(number):
    
    def add_one(number):
        number1=number + 1
        return number1
    
    result = add_one(number)
    return result

plus_one(5)
#############################################
#Passing function as Argument
#to other function

def plus_one(number):
    result1 = number + 1
    return result1

def function_call(function):
    result = function(5)
    return result

function_call(plus_one)

##############################################
#Function Returning other function

def hello_function():
    def say_hi():
        return "Hi"
    return say_hi 
#hello_function()
hello = hello_function()
hello()
#Always remember when you call hello_function()
#directly then it will display object not hi
#therefore you need to assign it to hello first
#then call hello() function

###############################################
#Need for decorators
import time
def calc_square(num):
    start=time.time()
    result=[]
    for i in num:
        result.append(i*i)
    end=time.time()
    total_time=(end-start)*1000
    print(f"total time for execution square is {total_time}")
    return result

def calc_cube(num):
    start=time.time()
    result=[]
    for i in num:
        result.append(i*i*i)
    end=time.time()
    total_time=(end-start)*1000
    print(f"total time for executin of cube is {total_time}")
    return result
array=range(1,100000)
out_sqaure=calc_square(array)
out_cube=calc_cube(array) 
#########################################
#that takes in a function and
#return it by adding some functionality
def say_hi():
    return 'Hello There'

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper 

decorate = uppercase_decorator(say_hi)
decorate()

###########################################
# However Python provides a much easier way
# for us to apply decorators.
# We simply use the @ symbol before
# the function we'd like to decorate
###########################################
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper 

@uppercase_decorator
def say_hi():
    return 'Hello There'
say_hi()

###########################################
# Applying Multiple Decorators
# that we've called them

def split_string(function):
    def wrapper():
        func = function()
        spliting_string = func.split()
        return spliting_string 
    return wrapper

def uppercase(function):
    def wrapper():
        func = function()
        uppercase_str= func.upper()
        return uppercase_str
    return wrapper

@split_string 
@uppercase
@uppercase
def say_hi():
    return 'Hello There'
say_hi()

##############################################################
import time
def time_it(func):
    #this is a decorator function that takes another function as argument
    
    def wrapper(*args, **kwargs):
        #*args and **kwargs allow wrapper
        #to accept any number of positional and keyword
        start = time.time()
        result = func(*args, **kwargs)
        
        #Calls the orignal function (func)
        #with the provided arguments
        
        end = time.time()
        print(func.name+"took"+str((end-start)*1000) + "mil sec")
        return result
    return wrapper

@time_it 
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it 
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,100000)

out_square = calc_square(array)
out_cube = calc_cube(array)

def say_hi():
    return 'Hello There'

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper 

decorate = uppercase_decorator(say_hi)
decorate()

###########################################
# However Python provides a much easier way
# for us to apply decorators.
# We simply use the @ symbol before
# the function we'd like to decorate
###########################################
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper 

@uppercase_decorator
def say_hi():
    return 'Hello There'
say_hi()

###########################################
# Applying Multiple Decorators
# that we've called them

def split_string(function):
    def wrapper():
        func = function()
        spliting_string = func.split()
        return spliting_string 
    return wrapper

def uppercase(function):
    def wrapper():
        func = function()
        uppercase_str= func.upper()
        return uppercase_str
    return wrapper

@split_string 
@uppercase
@uppercase
def say_hi():
    return 'Hello There'
say_hi()

##############################################################
import time
def time_it(func):
    #this is a decorator function that takes another function as argument
    
    def wrapper(*args, **kwargs):
        #*args and **kwargs allow wrapper
        #to accept any number of positional and keyword
        start = time.time()
        result = func(*args, **kwargs)
        
        #Calls the orignal function (func)
        #with the provided arguments
        
        end = time.time()
        print(func.name+"took"+str((end-start)*1000) + "mil sec")
        return result
    return wrapper

@time_it 
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it 
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,100000)

out_square = calc_square(array)
out_cube = calc_cube(array)
#################################
#Automatically logs function calls and their arguments
def log_decorator(func):
    def wrapper(args,*kwargs):
        print(f"calling{func.name}with{args}{kwargs}")
    return wrapper 
@log_decorator
def add(a,b):
    return a+b
print(add(3,4))
##########################################
#access control
def auth_required(func):
    def wrapper(user):
        if not user.get("authenticated",False):
            print("Access Denied")
            return
        return func(user)
    return wrapper

@auth_required
def dashboard(user):
    print(f"Welcome {user['name']}!")
    
user1 = {"name":"Alice","authenticated":True}
user2 = {"name":"Bob","authenticated":False}

dashboard(user1)
dashboard(user2)
############################################
#input validation
def validate_positive(func):
    def wrapper(x):
        if x < 0:
            raise ValueError("Negative values are not allowed")
        return func(x)
    return wrapper

@validate_positive
def square_root(x):
    return x ** 0.5

print(square_root(4))
print(square_root(-4))
#############################################
import time
def rate_limiter(max_calls,time_frame):
    calls = []
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            now = time.time()
            while calls and now - calls[0] > time_frame:
                calls.pop(0)
            if len(calls) >= max_calls:
                print("Rate limit exceed.Try again later")
                return
            
            calls.append(now)
            return func(*args , **kwargs)
        return wrapper
    return decorator
@rate_limiter(3,10)
def say_hello():
    print("hello!")
    
say_hello()
say_hello()
say_hello()
say_hello()

lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)

lst=[num for num in range(0,20)]
print(lst)

names=["dada","mama","kaka"]
lst=[name.capitalize()for name in names]
print(lst)

def is_even(num):
   return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)

lst=[f"{x}{y}"for x in range(3) for y in range(3)]
print(lst)

#set-comprehension
set_one={x for x in range(3)}
print(set_one)

#Dictionary-comprehension
dict={x:x*x for x in range(3)}
print(dict)

#Generator
#It is Another way of creating iterators
#in a simple way where
#it uses the keyword "yeild"
#instead of returning it in a defined funcitons
#Generators are implemented using a function
#Generators are implemented using a function
gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)

gen=(x
     for x in range(3)
    )
next(gen)#next is keyword

gen=(x for x in range(3))
next(gen)
next(gen)

#Function which returns multiple values
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)

#now instead of using for loop we can write our own generator
gen=range_even(6)
next(gen)
next(gen)

#let us hide password entered on screen
#chaining Generators
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
'''ele* appears to be a placeholder for an element
from an iterable.The asterisk(*) is likely just a character used to represent
a placeholder or a wildcard.
for instance if you are iterating over a list of elements,
"ele*" could symbolize any element in that list.
Its a generic representation that doesn't correspond to any specific syntax
in python or itertools.
'''
password=["not-good","give'm-pass","00100=100"]
for password in hide(lengths(password)):
    print(password)

#Enumerate -Printing list with index
lst=['milk','Egg','Bread']
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}')
    
#using enumerate
lst=['milk','Egg','Bread']
for index,item in enumerate(lst,start=1):
    print(f'{index} {item}')
    
#use zip function
name=['dada','mama','kaka']
info=[9850,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)

#zip-function
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9850,6032,9785]
for nm,inf in zip_longest(name,info):
    print(nm,inf)

#use fill value
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9850,6032,9785]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)
    
lst=[2,3,-6,8,9]#all values must be zero,negative or positive
if all(lst):
    print('all values are true')
else:
    print('There are null values')
    
lst=[2,3,0,8,9]
if all(lst):
    print('all values are true')
else:
    print('There are null values')

#use of any if any non zero value
lst=[0,0,0,-8,0]
if any(lst):
    print("It has some non zero value")
else:
    print("useless")

lst=[0,0,0,0,0]
if any(lst):
    print("It has some non zero value")
else:
    print("all values are null")

#count()
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))

from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))

#cycle
#suppose you have repeated tasks to be done
import itertools
instructions=("Eat","code","sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)