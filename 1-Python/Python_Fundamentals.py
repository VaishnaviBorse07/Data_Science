# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 09:26:28 2025

@author: vaish
"""

num1=10
num2=20
result=False
print(type(num1))
print(type(num2))
print(type(result))
x=1
print(x)
print(type(x))
x1=10000000000000000000000000000
print(type(x1))

age=int(input('Please Enter Your age:'))
print(type(age))
print(age)

age1=int(input('Please Enter Your age:'))
print(type(age1))
print(age1)
age=age+age1
print(age)


age=float(input('Please Enter Your age:'))
print(type(age))
print(age)

age1=float(input('Please Enter Your age:'))
print(type(age1))
print(age1)
age=age+age1
print(age)

int_val=12
str_val='23'
print(type(int_val))
print(type(str_val))
c=float(int_val)
d=float(str_val)
print(type(c))
print("int as float:",c)
print(type(d))
print("string as float:",d)

#Complex
c1=2
c2=2j
print("c1",c1,' c2',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

#Boolean
all_ok=True
print(all_ok)
all_ok=False
print(all_ok)
print(type(all_ok))

#if you will enter any value it will show true
#if you will not enter any value n just pressed enter it will show false 
status=bool(input("Ok it is confirmed:"))
print(status)
print(type(status))

#arithmetic
a=12
b=23
print(a+b)
print(type(a+b))
print(10*4)
print(type(10*4))
c=34
d=10
print(c-d)
print(type(c-d))

#division and flooring value
print(100/20)
print(type(100/2))
# // this operator is referred as integer divison operator 
print(100//20)
print(type(100//2))

#power operator
a=4
b=2
print(a**b)

#add and + operator
x=0
x+=1
print(x)

#None value
winner=None
print(winner is None)
print(winner is not None)
print(type(winner))#class-NoneType

#comparison operator if-else
num=int(input("Enter number:"))
if num > 0:
    print("Number is positive:",num)
else:
    print("Number is negative",num)

#if-elif-else
saving=int(input("Enter saving amount:"))
if saving > 1000:
    print("good saving")
elif 500<saving<1000:
    print("Well done")
elif 100<saving<500:
    print("Try harder")
else:
    print("Do some savings")
    
#iteration-looping
#while-loop
count=1
print("Start")
while count<=10:
    print(count)
    count+=1
print("End")

#for loop
for i in range(2,10):
    print(i)
    #print("Done")
print("Done")  
#mario-pyramid
#'Anonymous' loop variables displaying output horizontly
for _ in range(0,10):
    print(".",end=' ')
    #print()

#break statement
num=int(input("Enter number to check:"))
for i in range(0,6):
    if i==num:
        break;
    print(i,'',end='')
    print("Done")

#Odd number
start,end=4,20
for i in range(start,end+1):
    if i%2!=0:
        print(i,end=" ")

#even number
start,end=4,20
for i in range(start,end+1):
    if i%2==0:
        print(i,end=" ")
        
start,end=4,19
step=2
for i in range(start,end+1,step):
    if i%2==0:
      print(i,end=" ")
      
x,y,z=2,3,4
print(x)
print(y)
print(z)
x,y,z=2
print(x)
print(y)
print(z)

#20-02-25
#global variable
x="awesome"
def my_function():
    print("Python is "+x)
my_function()

#global and local variable
x="awesome"
def my_function():
    x="fantastic"
    print("Python is "+x)
my_function()
print("Python is "+x)

x=range(6)
print(x)
print(type(x))

#dictionary
x={"Name":"Ram","Age":20}
print(x)
print(type(x))

#assigning value
x=1
y=23j
z=1.56
print(type(x))
print(type(y))
print(type(z))

#typecast
x=int(23.6)
print(x)
y=float(23)
print(y)

#stringconcatenate
str1="hello"
str2=2
#str3=str1+str2--string+string only
print(f"hello{str2}")

#multiple strings
x="""hello.This is python.It is string function"""
print(x)

#string slicing
x="""hello.This is python.It is string function"""
print(x[0:10])

#slice from start
print(x[:6])

y="I am staying in jay colony"
print(y[16:27])

#slice from end
print(x[6:])

#negative index
print(x[-5:-1])
s="Python"
print(s[-1])
print(s[-6:-2])#'Pyth' is the output
print(s[-2:-6])#''empty string becoz slicing moves in forward
print(s[1:-1])#mix indexing is possible
print(s[::-1])#reversing the string

#modify string
print(x.upper())
x=x.upper()
print(x.lower())

#remove white space initial to end
x=" this is python "
print(x.strip())

x="this is python "
print(x.rstrip())

#replacing string
x="Hello world"
print(x.replace("Hello","Sello"))

#split which replaces white spaces
#word tokenization(separating word) &  sentence tokenization(separation of sentence)
x="Hello World"
print(x)
print(x.split(" "))
y="hi_hello_bye"
print(y.split("_"))
x="red~green~blue"
print(x.split("~"))
x="""This is python.Simple to understand.Difficult to implement"""
print(x.split("."))


'''
write a python function that accepts a hypen-separated
sequence of colors as input and returns the colors in a 
hyphen-separated sequence after sorting them alphabetically.
'''
input_colors="red-blue-green-white"
def sorted_color(input_colors):
    string_split=input_colors.split("-")
    print(string_split)
    string_sort=sorted(string_split)
    print(string_sort)
    x='-'.join(string_sort)
    return x
z=sorted_color(input_colors)
print(x)   


#21-02-25
#Negative index
s="Python"
print(s[-1])
print(s[-6:-2])#'Pyth' is the output
print(s[-2:-6])#''empty string becoz slicing moves in forward
print(s[1:-1])#mix indexing is possible
print(s[::-1])#reversing the string

#write program to find the string is palindrome or not
def is_palindrome(input):
    if input=="":
        return "You returned wrong input"
    else:
        string=input[::-1]
        if string==input:
            return True
    return False

#searching any string
x="This is python and it is very powerful"
print(x.find("and"))

#string concat
x="hello"
y="world"
print(x+y)

#string concat with whitespace
print(x+" "+y)

#to concatenate string with int
quantity=3
item_no=54
price=100
print(f"I want {quantity} pieces and item number is {item_no},it's price is {price}")
my_order="I want {} pieces and item number is {},it's price is {}"
print(my_order.format(quantity,item_no,price))
my_order="I want {0} pieces and item number is {1},it's price is {2}"
print(my_order.format(quantity,item_no,price))

#escape character  allows to use double quotes
text="this is fun fair and it has got big \"round rigo\""
print(text)

#boolean
print(10>9)
print(2<9)
print(10==10)

a=10
b=9
if(a>b):
    print("a is greater than b")
else:
    print("b is greater than a")


#mathematical operations
"""rules for mathematical operations
PEMDAS
paranthesis,exponential,multiplication,division,addition,substraction
"""

#identity operator
print(a is b)
print(a is not b)

#Python List
lst=["cherry","banana","apple"]
print(lst)

#24-02-2025
print(lst[0])
print(lst[1])

#append() adds element at end of list
lst=["cherry","banana","apple"]
lst.append("mango")
print(lst)

#clear removes all element
lst=["cherry","banana","apple"]
lst.clear()
print(lst)

#example
lst=[2,3,4,5,6,7,8]
lst1=[]
for i in lst:
    if i%2==0:
        lst1.append(i)
print(lst1)

#copy method
lst=["cherry","banana","apple"]
lst2=lst.copy()
print(lst2)

#count
lst=["cherry","banana","cherry"]
lst.count("cherry")

#extend
lst=[1,2,3]
lst1=[4,5,6]
lst.extend(lst1)
print(lst)

#insert
lst=["cherry","banana","apple"]
lst.insert(2,"mango")
print(lst)

#pop element
lst=["cherry","banana","apple"]
lst.pop(2)
print(lst)

#remove
lst=["cherry","banana","cherry"]
lst.remove("cherry")
print(lst)

#reverse
lst=["cherry","banana","mango"]
lst.reverse()
print(lst)

#sort()-alphabetically
lst=["orange","fig","coconut"]
lst.sort()
print(lst)

lst=[20,30,10,50]
lst=sorted(lst,key=int)
lst

#Nested list
nested_lst=[[1,2,3],["a","b","c"],[True,False]]
print(nested_lst)

#accessing list
nested_lst[0][2]
print(nested_lst[0])
print(nested_lst[-1][-1])
print(nested_lst[1][1])

#modifying list
nested_lst[1][1]="z"
print(nested_lst)

#Iterating over nested list
for sublist in nested_lst:
    print(sublist)

#using two for loops
for sublist in nested_lst:
    for item in sublist:
        print(item,end=" ")

#list comprehension with nested list
#flattening of list
flat_list=[item for sublist in nested_lst for item in sublist]
print(flat_list)

#adding an entire sublist
nested_lst=[[1,2,3],["a","b","c"],[True,False]]
nested_lst.append(["new","list"])
print(nested_lst)

#adding an element inside a sublist
nested_lst[0].append(4)
print(nested_lst)

#removing element from sublist
nested_lst[1].remove("c")
print(nested_lst)


#Tuple
#immutable,()paranthesis,Faster(size fixed)
#Cannot add,remove,or change elements
#read-only collection

tup=("cherry","banana","cherry")
print(tup)
print(tup[0])

#once a tuple is created u can't change it's value
x=("apple","banana","cherry")
print(id(x))
#first convert it into list
y=list(x)
y[1]='kiwi'
#list to tuple
x=tuple(y)
print(x)
print(id(x))

#tuple can have diff datatype
x=("apple",2,'hello')
print(x)

#accesing tuple elemeent using index
x=("apple","banana","cherry")
print(x[1])

#to join two or more tuples concatenation is used
tup1=('a','b','c')
tup2=(1,2,3)
tup=tup1+tup2
print(tup)

#Dictionary
dict1={'brand':'maruti','model':'2345','year':2011}
print(dict1)
print(len(dict1))
print(type(dict1))

dict1.get('model')
dict1.keys()

car={'brand':'ford','model':'mustang','year':1964}
print(id(car))
x=car.keys()
print(x)

#adding one more key and value
car['color']='white'
car
print(id(car))
x=car.keys()

#Removing dictionary element
car={"brand":"ford","model1":"mustang"}
car.pop("model1")
print(car)

#update
data={"brand":"ford","model1":"mustang"}
data.update({'brand':'maruti'})
data

#Accesing values in the dictionary 
car={"brand":"maruti","model":"branding","price":900000}
for i in car:
    print(car[i])
    
# accesing keys and values both 
#1]method 1 
for i in car:
    print(i,":",car[i])
 
#2]method 2
for key,value in car.items():
    print("%s=%s %(key,value)")
 
#3]method 3
for key,value in car.items():
    print(f"{key}: {value}")
    
#copying dictionary
#1]method-1
car={"brand":"maruti","model":"branding","price":900000}
print(id(car))
car2=car.copy()
print(car2)
print(id(car2))

#2]method-2
this_dict={"name":"shraddha","age":20,"class":"sy"}
print(id(this_dict))
dict1=dict(this_dict)
print(dict1)
print(id(dict1))

#Nested dictionary main dictionary key have values of nested dictionary
nested_dict={'japan':'2018','country':{'India':'2015','Itli':'1025'},'austrelia':'2024'}
print(nested_dict)

#Dictionary Methods
#clear->Remove all elements from dictionary
car={"brand":"maruti","model":"branding","price":900000}
car.clear()
print(car)

#create a dictionary with 3 keys all with values 0
x={'key1','key2','key3'}
y=0
nested_dict=dict.fromkeys(x,y)
nested_dict

#get()
nested_dict={'japan':'2018','country':{'India':'2015','Itli':'1025'},'austrelia':'2024'}
nested_dict.get("japan")
#items()->print each element in tuple and all dictionary in list
nested_dict.items()
#values()
nested_dict.values()

#sort by keys
nested_dict={'japan':'2018','country':{'India':'2015','Itli':'1025'},'austrelia':'2024'}
x={'d':'3','a':'2','z':'5','h':'1'} 
sorted_by_key=dict(sorted(x.items()))
print(sorted_by_key)

#sorted by values
sorted_values=dict(sorted(x.items(),key=lambda item:item[1])) 
print(sorted_values)
#how it works
#data.items() produces->[('d',3),('a',2),('z',5),('h':1)]
#lambada ('d':3)->returns 3 and so on,the tuple are sorted based on the return values

                
####-Lambda Function/Anonymous function-####
#lambda function 
add=lambda a,b,c:a+b+c
add(2,3,4)

#min(my_dict):return the minimum key
#min(my_dict.values()):returns minimum value
#min(my_dict,key=my_dict.get()):returns the corresponding to the minimum
sorted_dict={"banana":40,"apple":100,"grapes":120,"mango":200}
free_item_key=min(sorted_dict,key=sorted_dict.get)
free_item_value=sorted_dict[free_item_key]
print(f"You will get the lowest priced item'{free_item_key}' ({free_item_value})")
free_item_min=min(sorted_dict)
free_item_min
free_item_minvalue=min(sorted_dict.values())
free_item_minvalue

sorted_dict={"banana":40,"apple":100,"grapes":120,"mango":200}
free_item_key=max(sorted_dict,key=sorted_dict.get)
free_item_value=sorted_dict[free_item_key]
print(f"You will get the highest priced item'{free_item_key}' ({free_item_value})")

#sorting in descending order
sorted_by_values_desc=dict(sorted_dict.items(),key=lambda item:item[1])
sorted_by_values_desc

#adding values in dictionary
dict1={'apple':'100','mango':'200','fig':'250'}
sum=0
for value in dict1.values():
    sum=sum+int(value)
print(sum)

#convert values to integers and sum them up
dict1={'apple':'100','mango':'200','fig':'250'}
total_sum=sum(int(value) for value in dict1.values())
total_sum

#concatenate dictionary
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50}
dict1.update(dict2)
dict1
dict1.update(dict3)
dict1
dict1=dict1|dict2|dict3#another method
dict1

#to check given key is already exists or not
dict1={'a':20,'b':30}
print('a'in dict1)

#while with break statement 
i=1
while i<6:
    print(i)
    if (i==3):
        break
    i=i+1
    
#suppose u are selling milk 100 litres and there is queue of customers
#the moment sell reaches to 100 litres,you need to inform to the customer
#that the milk is finished
milk_available = 100  # Total milk available
customer = 1

while milk_available > 0:
    requested = int(input(f"Customer {customer}, enter the amount of milk you need: "))
    
    if requested <= milk_available:
        milk_available -= requested
        print(f"Milk sold: {requested} litres. Remaining: {milk_available} litres.")
    else:
        print(f"Only {milk_available} litres available. Cannot sell {requested} litres.")
    
    if milk_available == 0:
        print("Milk is finished. Sorry, we can't serve more customers.")
        break  
    
    customer += 1


#continue statement
i=1
while i<6:
    i=i+1
    if (i==3):
        continue
    print(i)

#suppose you are standing in queue to auditorium,where students and 
#professors are in queue,if the professors are there you are allowing
#without checking but if there is student then he/she is being checked
queue = ["Professor", "Student", "Student", "Professor", "Student"]

for person in queue:
    if person == "Professor":
        print(f"{person} is allowed without checking.")
        continue  

    print(f"{person} is being checked before entry.")

lst=[1,2,3,0,4,5,6,-9]
for i in lst:
    if i==0:
        continue
    if i%2!=0:
        print(f"{i} is odd")
#for loop-break and continue
fruits=["apple","banana","cherry"]
for i in fruits:
    print(i)
    if(i=='banana'):
        break

fruits=["apple","banana","cherry"]
for i in fruits:
    if(i=='banana'):
        break
    print(i)
    
fruits=['apple','banana','cherry']
for x in fruits:
    if(x=='banana'):
        continue
    print(x)
 
    
for x in range(6):
    print(x)
    
for x in range(2,6):
    print(x)

for x in range(2,30,3):
    print(x)

colors=["green","yellow","red"]
fruits=["guava","banana","apple"]
for x in colors:
    for y in fruits:
        print(x,y)
        
#function without argument
def my_function():
    print("Hello function!!")
my_function()

#function with argument
def my_func(name):
    print("hello "+name)
my_func("Ram")

#function with positional arguments
def my_func(name1,name2):
    print(name1+" "+name2)
my_func("Hello","World")

def my_func(name2,name1):
    print(name1+" "+name2)
my_func("Hello","World")

#arbitary argument function, *args
#if you do not know how many arguments that will
#be passed into ur function
#add * before the parameter name

#the function definition
def my_function(*args):
    print(args[0]+" "+args[2])
my_function("vaishu","Maithi","pranju")

#whenever key and value is needed
def myfun(**kwargs):
    for key,value in kwargs.items():
        print("%s==%s"%(key,value))
        print(f"{key} : {value}")
myfun(first_name="papalal",mid_name="mohanlal",last_name="Goyal")    

#default argument function
#if we call the function without argument
#it uses the default value
def my_function(country="India"):
    print("I am from "+country)
my_function("Norway")
my_function("Dubai")
my_function()
my_function("Brazil")

#passing list as a argument
#you can send any data types of argument to a function(string,int,float)
#if you pass list as a argument it will be still list
fruits=["orange","apple",'banana']
def my_function(fruits):
    for x in fruits:
        print(x)
my_function(fruits)

def my_funtion(x):
    y=x*5
    z=x*2
    return y,z#output is in tupple
my_funtion(5)

#pass function
def my_function1():
    pass
my_function1()
#allows to run whole script without any error
#having an empty funtion definition it shows error 
#without pass funtion

#recursive function
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
factorial(3)
factorial(6)

#lambda function
def add(a):
    sum=a+10
    return sum
add(20)
add=lambda a:a+10
print(add(20))

mul=lambda a:a*10
print(mul(20))

add=lambda a,b:a+b
print(add(5,6))

lst=[23,56,45,34,78,99]
odd_lst=list(filter(lambda x:(x%2!=0),lst))
print(odd_lst)

lst=[23,56,45,34,78,99]
even_lst=list(filter(lambda x:(x%2==0),lst))
print(even_lst)

#map(funtion,iterable)
#the map()function in python is a built in funtion
#that applies a given function to each item of an
#
lst=[23,56,45,34,78,99]
sqr_lst=list(map(lambda x:(x**2),lst))
print(sqr_lst)

text="apple,banana,orange"
words=text.split(",")#split by comma
print(words)#output is:['apple', 'banana', 'orange']

new_text="-".join(words) #join with '-'
print(new_text)#output is:apple-banana-orange

#find() & index()-Find Substriing
#find() returns the index of the first occurence
#index() same but it raise error if it not found
text="Hello XYZ"
print(text.find("XYZ"))
print(text.find("Python"))#output:-1
print(text.index("Hello"))
print(text.index("Python"))#Output:ValueError: substring not found


#count()-Count substring Occurence
text="Hello Hello Python"
print(text.count("Hello"))

#startswith() & endswith() -Check Start/End
text="Python is great"
print(text.startswith("Python"))#Output:True
print(text.endswith("great"))#Output:True

#isalpha(),isdigit(), isalnum()
#isalpha()->Return true if all characters are letter
#isdigit()->Return true if all characters are digit
#isalnum()->Return true if all characters are letters as well as digit(either letters or numbers)
text="Maithili1234"
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())#true

t="1"
print(t.isdigit())

#isupper()->Checks if all characters are in Uppercase
#islower()->Check if all characters are in Lowercase
t="HELLO"
t2="HELLO123"
t3="1234"
count=0
for i in range(len(t)):
    if t[i].isupper():
        count+=1
print(count)#output:5

for i in range(len(t2)):
    if t2[i].islower():
        count+=1
print(count)#output:0

for i in range(len(t3)):
    if t3[i].isupper():
        count+=1
print(count)#output:0

#Does it end with fullstop?
str="There are no traffic jams along the extra mile."
ans=str.endswith(".")
print(ans)

#Check in list there is any duplicate or not
lst1=[6,8,5,6,7]
lst1.sort()
print(lst1)
def is_duplicate(lst1):
    for i in range (len(lst1)-1):
        #compare current number with next number present in list
        if (lst1[i]==lst1[i+1]):
            return True
    return False
print(is_duplicate(lst1))

#Different Types of Error
print(zzz)#NameError

print("Hello"#SyntaxError
      
str="Hello"
str=str+5#TypeError

print(str[10])#IndexError: string index out of range

dict={1:11,2:22,3:33}
print(dict[5])#KeyError

str="Bye"
str.reverse()#AttributeError

str="moose"
ans_1=int(str)#ValueError

#Syntax,Sementic,Compile
'''
#Types of Exceptions
#Arithmetic exception
#Array index out of bound exception
#Array store
#FileNotFound
#IOException-general I/O Failure
#NullPointer Excetion
#outofmemory Exception
#Security Exception
#StackOverflow Exception

#try://statement except://statement
'''
#Use case-
''' alex wants to buy exactly N bananas from 
two vendors.Each vendor sells bananas
in fixed-sized bunches.
Alex can only purchase full bunches and 
not individual bananas
he needs your help to determine
the minimum cost required to buy exactly N bananas
'''
no_banana=int(input("Enter no of banana to be purchased:"))
lot1=int(input("What is size of lot1 that vendor1 provides:"))
price1=int(input("What is price of lot1:"))
lot2=int(input("What is size of lot2 that vendor2 provides:"))
price2=int(input("What is price of lot2:"))
def min_cost(no_banana,lot1,price1,lot2,price2):
    lot_a=no_banana//lot1
    print(f"lot_a:{lot_a}")
    lot_b=no_banana//lot2
    print(f"lot_b:{lot_b}")
    cost_a=lot_a*price1
    print(f"cost_a:{cost_a}")
    cost_b=lot_b*price2
    print(f"cost_b:{cost_b}")
    return min(cost_a,cost_b)
min_cost(no_banana, lot1, price1, lot2, price2)
    
#Bubble sort
def bubble_sort(lst):
    n=len(lst)
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
lst=[5,3,8,4,2]
bubble_sort(lst)

#GCD
#Euclidean Algorithm
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
ans=gcd(num1,num2)
print(f"GCD of {num1} and {num2} is:{ans}")

import math
a=int(input("Enter first no:"))
b=int(input("Enter second no:"))
ans=math.gcd(a,b)
print(ans)
list=[3,4,5,6,2]
n=len(list)
for i in range(0,2):
    for j in range(n-1):
        if(list[j] > list[j+1]):
            list[j],list[j+1]=list[j+1],list[j]
print(list[n-2])  #here instead of n-2 we can also use list[j]

list=[3,4,5,6,2]
n=len(list)
for i in range(0,2):
    for j in range(0,i):
        if (list[j] > list[i]):
                list[j],list[i]=list[i],list[j]
print(list[1])

list1=[3,4,5,6,2]
def secon_largest(list1):
    unique_elements=list(set(list1))   #here it converts the sets of the list again into list
    unique_elements.sort(reverse=True)
    if len(unique_elements) > 1:
        return unique_elements[1]
    else:
        return
print(secon_largest(list1))

#code to find the missing no from a list
list=[2,3,4,5,6]
n=len(list)
def missing_no(list,n):
    expected_sum=n*(n+1)//2
    actual_sum=sum(list)
    missing_no=abs(expected_sum - actual_sum)
    return missing_no
print(missing_no(list,n))

string1=input("Enter a string:")
list1=list(string1)
i=0
j=len(list1)-1
while(i<j):
     list1[i],list1[j]=list1[j],list1[i]
     i+=1
     j-=1
result=''.join(list1)
print(result)


a=12
b=14
def gcd(a,b):
    while b:
         a,b=b,a%b
    return a
gcd(a,b)

def lcm(a,b):
    lcm=abs(a*b)/gcd(a,b)
    return lcm
lcm(a,b)

'''Gary is an avid hiker. He tracks his hikes meticulously,
 paying close attention to small details like topography.
 During his last hike, he took exactly n steps. 
 For every step he took, he noted if it was an uphill (U) 
 or a downhill (D) step. Gary’s hikes start and end 
 at sea level.

We define the following terms:

A mountain is a non-empty sequence of consecutive
 steps above sea level, starting with a step up 
 from sea level and ending with a step down to sea level.
 A valley is a non-empty sequence of consecutive
 steps below sea level, starting with a step down 
 from sea level and ending with a step up to sea level.
Given Gary’s sequence of up and down steps 
during his last hike, find and print the number of valleys
 he walked through.

Gary is hiking, and he records each step as either U (uphill) or D (downhill). He always starts and ends at sea level (0 altitude).

We need to count the number of valleys he walks through.

What is a valley?
A valley is when:

Gary goes below sea level (altitude becomes negative).
He then comes back to sea level.
Example Walkthrough
Let’s say Gary takes the following 8 steps:
"DDUUUUDD" 
'''
#count the valleys:
def count_valleys(n,paths):
    elevation=0 # Starting at sea level
    valley_count=0 #Counter for valleys
    
    for step in path:
        if step =='U':# going up
           elevation+=1 
           if elevation==0: #IF we just came back 
                            # to sea level , a valley ended
              valley_count+=1 #Why check if elevation == 0?
              #inside if step == 'U' ?
              #A valley is only completed when coming up(U)
              #back to sea level (0).
        else:
            step=='D' #Going down
            elevation-=1 
    return valley_count

# Example Usage
n=8
path="UDDDUDUU"
print("Total Valleys", count_valleys(n,path))

def left_rotate(lst,d):
    n=len(lst)
    d=d%n
    left_rot=lst[d:]+lst[:d]
    return left_rot
lst=[1,2,3,4,5]
d=2
result=left_rotate(lst, d)
print(*result) 

def right_rotate(lst,d):
    n=len(lst)
    d=d%n
    right_rot=lst[:d]+lst[d:]
    return right_rot
lst=[1,2,3,4,5]
d=2
result=right_rotate(lst, d)
print(*result) 

#create matrix and print matrix
mat1=[[1,2,3],[4,5,6],[7,8,9]]
for i in mat1:
    print(i)
    
mat=[[1,2,3],[4,5,6],[7,8,9]]
rows =len(mat)
columns=len(mat[0])
print("rows:",rows)
print("columns:",columns)

for i in range(rows):#Iterating over rows
    for j in range(columns):#Iterating over columns
        print(f"Element at [{i}][{j}]={mat[i][j]}")

#matrix addition
mat1=[[1,2,3],[4,5,6],[7,8,9]]
mat2=[[1,2,3],[4,5,6],[7,8,9]]
result=[[0,0,0],[0,0,0],[0,0,0]]
rows=len(mat1)
columns=len(mat1[0])
for i in range(rows): 
    for j in range(columns):
        result[i][j]=mat1[i][j]+mat2[i][j]
result        

mat1=[[1,2,3],[4,5,6],[7,8,9]]
rows=len(mat1)
columns=len(mat1[0])
for i in range(rows): 
    for j in range(columns):
        if i==j:
            print(mat1[i][j])
            
#check if the given matrix is sparse
#a sparse matrix is a matrix in which most of 
#the elements are zero.If the number of 
#zero elements is greater than half of the total elements
mat1=[[1,2,0],[0,4,0],[0,0,6]]
#mat1=[[1,2,0],[0,4,5],[7,0,6]]
rows=len(mat1)
cols=len(mat1[0])
count=0
for i in range(rows):
    for j in range(cols):
        if mat1[i][j]==0:
            count=count+1
if count>(rows*cols)/2:
    print("sparse")
else:
    print("Not sparse")
    
#program to check if two matrices are identical
#rows must be equal to columns
#content must be equal of both matrix
def are_identical(mat1,mat2):
    rows1,cols1=len(mat1),len(mat1[0])
    rows2,cols2=len(mat2),len(mat2[0])
    if rows1!=rows2 or cols1!=cols2:
        return False
    for i in range(rows1):
        for j in range(cols1):
            if mat1[i][j]!=mat2[i][j]:
                return False
    return True

mat1=[[1,2,3],[4,5,6]]
mat2=[[1,2,3],[4,5,6]]

print("Are the matrices identical?",are_identical(mat1, mat2))

mat1=[[1,2,3],[4,5,6]]
mat2=[[1,2],[3,4]]
if are_identical(mat1, mat2):
    print("Identical")
else:
    print("not identical")

'''
#Given 2d array convert into 1d array in spiral order
1  2  3  4
5  6  7  8
9 10 11 12
13 14 15 16
'''
#Set
#to remove item from set
st={1,4,6}
st.remove(4)
print(st)

#intersection of sets
st1={1,4,6}
st2={2,4,6}
st=st1&st2
print(st)

#union of sets
st=st1|st2
print(st)

def dict():
    return {i:i**2 for i in range(1,16)}
print(dict())

#max and min of set
max_set=max(st)
print(max_set)
min_set=min(st)
print(min_set)

#given a string return string made of two characters
text='wipro'
text1=text[:2]
final=text1*len(text)
print(final)

#given a string if first and last character is x,then display
#the string of without x,display as it is
text='madam'
if(text[0]==text[-1]):
    final=text[1:-1]
    print(final)
else:
    print(text)
    
#Given string and an integer n,
#return a string made of n repetition
#of the last n character of string 
#You may assume that n is between 0 and the length
#of the string (inclusive)

#for example, if the input are "Wipro" and 3,
#then the output should be "propropro".
text="wipro"
n=3
text1=text[2:5]
final=text1*n
print(final)

###SETS DATA STRUCTURE
#remove element
s={1,4,6}
s.remove(4)
print(s)
#find intersection of sets
s1={1,4,0,6}
s2={2,4,6,0}
s=s1&s2
print(s)
#union of sets
s1={1,4,0,6}
s2={2,4,6,0}
s=s1|s2
print(s)

#printing dictionary
#dictionary comprehension
d={x:x*x for x in range(1,16)}
print(d)

#to find minimum and maximum value of set
max_set=max(s)
print(max_set)
min_set=min(s)
print(min_set)

###############
#string data structure
#printing first two char n number of times
#n=length of string
text='wipro'
t1=text[:2]
final=t1*len(text)
print(final)

'''if first and last char is x 
then display the string without x,else
display as it is'''
t='madam'
if (t[0]== t[-1]):
    f=t[1:-1]
    print(f)
else:
    print(t)
    
############################
'''given a string and integer n
return strinng made of n repitatons
of the last n characters of the string
you may assume that n is between 0 and length
of string (exclusive)'''
t='wipro'
n=3
t1=t[2:5]
final=t1*n
print(final)

'''you are signing in bank and bank has 
forwarded OTP and check wheather it is
numeric and 6 digits .if valid print ok
else print non valid'''
otp=input("Enter otp forwarded")
if otp.isdigit() and len(otp)==6:
    print("ok")
else:
    print("invalid OTP")
    
#########exception handling
#zero division error
a=10
b=0
try:
    res=a/b
except ZeroDivisionError:
    print("cannot divide by 0!")

#index error
num=[1,2,3]
#print(num[5])
try:
    print(num[5])
except IndexError:
    print("index out of range error")

#handling exceptions withoout naming them
try:
    n=50
    d=int(input('enter denominator'))
    quotient=(n/d)
    print("divison performed succesfully")
except ValueError:
    print("only integere should be entered")
except:
    print("oops...some exception raised")

#handling exception using using try..except..else
try:
    n=50
    d=int(input('enter denominator'))
    quotient=(n/d)
    print("divison performed succesfully")
except ZeroDivisionError:
    print("division by zero not allowed")
except ValueError:
    print("only integere should be entered")
else:
    print("division is",quotient)

#xception handling using try except else finally
try:
    n=50
    d=int(input('enter denominator'))
    quotient=(n/d)
    print("divison performed succesfully")
except ZeroDivisionError:
    print("division by zero not allowed")
except ValueError:
    print("only integere should be entered")
else:
    print("division is",quotient)
finally:
    print("over and out")
    
#filenot found
with open('C:/Users/Lenovo/Desktop/pythonfundamentals/py_digits.txt','r') as file:
    contents=file.read()
print(contents.rstrip())
 

try:
    with open('C:/Users/Lenovo/Desktop/pythonfundamentals/py_digits.txt','r') as file:
        contents=file.read()
except FileNotFoundError:
    print("file not found")

#permision error
with open('C:/Users/Lenovo/Desktop/pythonfundamentals/py_digits.txt') as file:
    contents=file.read()
print(contents.rstrip())
#with try and catch
try:
    with open('E:/Vaishu coding/Data Science/1-Python/py_digits.txt"') as file:
        contents=file.read()
    print(contents.rstrip())
except PermissionError:
    print("dont have permisiion to access file ")
    
    
#attribute error
obj=None
print(obj.some_attribute)
if obj is not None:
    print(obj.some_attribute)
else:
    print("object is none!")
    
#MemoryError
l=[1](10*10)  #raises memory error

#handling using generator
def generate_num():
    for i in range(10**10):
        yield i #yield numbers one by one  prevent memory error
gen=generate_num()
print(next(gen))

###########################################
import sys
sys.setrecursionlimit(1000)

def safe_recursive_function(depth=0,max_depth=10):
    if depth>=max_depth:
        return "Done"
    return safe_recursive_function(depth+1,max_depth)
print(safe_recursive_function())

#write a program to read the entire content from txt file
with open("E:/Vaishu coding/Data Science/1-Python/py_digits.txt",'r') as File:
    contents=File.read()
    print(contents.rstrip())

with open("E:/Vaishu coding/Data Science/1-Python/py_digits.txt",'r') as File:
    lines=File.readlines()
    if lines:
        print("First line:",lines[0].strip())
        print("last line:",lines[-1].strip())

filename ="E:/Vaishu coding/Data Science/1-Python/programming.txt" 
with open(filename,'w') as file:
    file.write("I love programming.\n")
    file.write("I love creating new game.\n")
    in_line=input("Enter the line")
    file.write(in_line)

#write a program to read contents from a text file line by 
#line and store each line into a list
filename="E:/Vaishu coding/Data Science/1-Python/py_digits.txt"
with open(filename,'r') as file:
    lines=file.readlines()
    pi_string=[]
    for line in lines:
        pi_string.append(line.rstrip())
        #pi_string+=line.rstrip()
        print(pi_string)
    print(len(pi_string))
    
#write a program to fine the largest word from the txt file
#contents assuming that the file will have only one longest word
filename="E:/Vaishu coding/Data Science/1-Python/programming.txt"
with open(filename,'r') as file:
    lines=file.readlines()
    longest_word=''
    for line in lines:
        words=line.split()
        for word in words:
            if(len(word)>len(longest_word)):
                longest_word=word
print("The Longest word:",longest_word)

filename = "E:/Vaishu coding/Data Science/1-Python/programming.txt"
with open(filename, 'r') as file:
    lines = file.readlines()
    smallest_word = None
    for line in lines:
        words = line.split()
        for word in words:
            if smallest_word is None or len(word) < len(smallest_word):
                smallest_word = word
print("The smallest word:", smallest_word)

#write a program to count the frequency of a 
#user entered word in the text file
filename = "E:/Vaishu coding/Data Science/1-Python/programming.txt"
input_line=input("Enter the text:")
words=input_line.split()
word_count=len(words)

#write user input to the file
with open(filename,'w')as file:
    file.write(input_line)
#display the word count
print("The total words entered:",word_count)

#Find string code
'''CRAZY zak has designed the below steps which can be applied 
on any given string (sentence)to produce a number
STEP 1: in each word, find the sum of the Difference between 
the first letter and the last letter , second letter and the 
penultimate letter , and so on till the centre of the word.

STEP 2:Concatinate the sums of each word to form the result

for example: 
    If the given String is "WORLD WIDE WEB"
    
STEP 1:in each word , find the sum of the Difference between
the first letter and the last letter, second letter and the
 penultimate letter and so on till the center of the word 
 
 WORLD = [W-D]+[O-L]+[R] = [23-4]+[15-12]+[18]=[19]+[3]+[18]=[40]
 WDE = [W-E]+[l-D]=[23-5]+[9-4]=[23]
 WEB = [W-B]+[E]=[23-2]+[5]=[26]
 '''
sentence ='world wide web'
sentence =sentence.upper()#convert to uppercase
words =sentence.split()#split into words
words
#convert each word into list of characters
char_lists=[list(word) for word in words]
char_lists

first_char=char_lists[0][0]
last_char=char_lists[0][-1]

#Get ASCII values
ascii_first=ord(first_char)
ascii_last=ord(last_char)

print(f"First Character: {first_char}, ASCII: {ascii_first}")
print(f"Last Character: {last_char}, ASCII: {ascii_last}")

#######################################
sentence ='world wide web'
sentence =sentence.upper()#convert to uppercase
words =sentence.split()#split into words
words
#convert each word into list of characters
char_lists=[list(word) for word in words]
char_lists

ascii_difference=[]
for word in char_lists:
    first_char=word[0]
    last_char=word[-1]
    ascii_first=ord(first_char)
    ascii_last=ord(last_char)
    
    difference=abs(ascii_first-ascii_last)
    ascii_difference.append(difference)
for word,diff in zip(words,ascii_difference):
    print(f"Word:{word},ASCII Difference:{diff}")
    
'''write a program to accept two numbers from the user
and perform division.If any exception occurs,
print an error message or else print the result.
'''
try:
    num1=float(input("Enter Number1:"))
    num2=float(input("Enter number2:"))
    num=num1/num2
    print("Result is",num)
except ZeroDivisionError:
    print("Error:Division by zero is not allowed.")
except ValueError:
    print("Error:Please enter numric values only.")
    num1=float(input(""))
    
'''write a program to accept a number from the user
and check whether it's prime or not.If user enters
anything other than number,
handle the exception and print an error message.
'''
def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i==0:
            return False
    return True

try:
    num=int(input("Please enter the number:"))
    if is_prime(num):
        print("number is prime")
    else:
        print("Number is not prime")
except ValueError:
    print("Error:please enter valid integer")

'''
write a program to accept the file name
to be opened from the user
if file exist print the contents of file
in title case or else handle the exception and 
print an error message
'''
try:
    file_name=input("please enter the file name with absolute path:")
    with open(file_name,'r')as file:
        content=file.read()
        print(content.title())
except FileNotFoundError:
    print("Error:File not Found.Please enter the correct file with absolute path")
except PermissionError:
    print("Error:You don't have permission to access the file")
    
'''
Declare a list with 10 integer and ask the user to enter an index 
check whether the number in that index is positive or negative 
number . If any invalid index is entered handle the exception and print an error message
'''
numbers=[2,4,7,1,13,57,-3,-6,10,89]
try:
    index =int(input("Enter an index (0-9):"))
    value=numbers[index]
    if value>0:
        print(f"The number at index {index} is positive.")
    else:
        print(f"The number at index {index} is negative.")
except IndexError:
    print("Error:Index out of range.Please enter a valid index")
except ValueError:
    print("Error:Please enter a valid integer.")

#convert letters into their mapped ASCII value
def get_mapped_value(letter):
    return ord(letter)-ord('A')+ 1
letters=['A','B','R','W','Z']
for letter in letters:
    print(f"letter: {letter}, Mapped Value: {get_mapped_value(letter)}")

#addition using strings: write a function that
#takes two numbers in string format and forms a 
#string containing the sum (addition) of these
#two numbers.
#assumption:    
#the input will contain only numeric digits.
#the input strings can be of any large lengths
#the input strings are "1234" and "56"

def add_of_string(num1,num2):
    sum=str(int(num1)+int(num2))
    return sum
add_of_string("1234","56")


#kamal is data analyst in a lottery management
#organization.one of the task assigned to kamal 
#is to find the most frequently occuring digit
#in a series of input below are couple of example
#to illustrate hpw to find the most frequently
#occuring digit in a series of input numbers
from collections import Counter
def most_frequent_digit(numbers):
    digit_count=Counter()
    
    #count occurences of each digit
    for num in numbers:
        digit_count.update(str(num))
        
    #find the most frequent digits
    max_frequency=max(digit_count.values())
    most_frequency=[int(digit)for digit,count in digit_count.items() if count==max_frequency]
    
    return most_frequency,max_frequency

numbers=[1237,262,666,140]
most_frequency,frequency=most_frequent_digit(numbers)
print(f"most frequently occuring digit:{most_frequency}")

def find_digit_to_remove(input1):
    str_num=str(input1)#convert number to string    
    #cheak if number is already palindrome
    if str_num==str_num[::-1]:
        return -1#no digit needs to be remove
    #try removing each digit one by one
    for i in range(len(str_num)):
        new_num=str_num[:i] + str_num[i+1:]#remove digit at index i
        if new_num==new_num[::-1]:#cheak if number is palindrome
            return int(str_num[i])#return the removed
    return -1#if no single digit removal makes it a palindrome
    
print(find_digit_to_remove(12332))
print(find_digit_to_remove(251532))
print(find_digit_to_remove(10101))
print(find_digit_to_remove(981894))


#given an array with "N" elements,you are expected
#to find the sum of the values that are present
#in non-prime indices of the array.
#note: the array index starts with 0
def sum_nom_prime(input1,input2):
    def is_prime(num):
        if num<2:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    total=0
    for i in range(input2):
        if not is_prime(i):
            total+=input1[i]
    return total
input1=[10,20,30,40,50,60,70,80,90,100]
input2=10
sum_nom_prime(input1, input2)

input1="The Good The Bad and The Ugly"
words=input1.split()
words
char_lists=[list(word)for word in words]
char_lists
letter_counts=[len(chars)for chars in char_lists]
letter_counts
def total_sum(num):
    total=0
    while (num!=0):
        last_digit=num%10
        total=total+last_digit
        num//=10
    return total
total=[total_sum(num)for num in letter_count]
total
result=sum(total)
print("PIN",result)

def get_pin(input1):
    word=input1.split()
    total_length=sum(len(word)for word in words)
    while total_length>=10:
        total_length=sum(int(digit)for digit in str(total_length))
    return total_length
get_pin("The Good The Bad and The Ugly")
get_pin("Wipro Technologies")
  
      
'''Adittion using strings :write a function that
takes two nus in string formate and forms a string containing
the sum of this two nos'''
def add_of_string(num1,num2):
    sum=str(int(num1)+int(num2))
    return sum
print(add_of_string(10,20))
    

'''Find the most frequently occuring digit in 
series '''
from collections import Counter
def most_frequent_digit(numbers):
    digit_count = Counter()
    for num in numbers:
        digit_count.update(str(num))
    max_frequency=max(digit_count.values())
    most_frequency=[int(digit) for digit,count in digit_count.items() if count==max_frequency]
    return most_frequency,max_frequency
numbers=[1234,1234,44678]
most_frequent,frequency=most_frequent_digit(numbers)
print(f'most frequent occuring digit:{most_frequent}')
      
  
'''To find palindrome if the digit  is not palindrom the remove 
then remove those digit print how many digits are removed '''
def find_digit_to_remove(input1):
    str_num=str(input1)
    #Check if n is already palindrom 
    if str_num == str_num[::-1]:
        return -1#no digit need to be removed
    #Try removing each digit one by one
    for i in range(len(str_num)):
        new_num = str_num[:i]+str_num[i+1:]
        #remove digit at index i
        if new_num == new_num[::-1]:
            return int(str_num[i])
    return -1 
print(find_digit_to_remove(12332))      
print(find_digit_to_remove(122332))      
print(find_digit_to_remove(133321))      
print(find_digit_to_remove(123))      


'''Array with n elements expcted to find
 sum of values that are present in non-prime
 indices of the array.
'''
def sum_non_prime(input1,input2):
    def is_prime(num):
        if num<2:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
            return True
    total=0
    for i in range(input2):
            if not is_prime(i):
                total+=input1[i]
    return total
input1=[10,20,30,40,50,60,70,80,90,100]
input2=10
print(sum_non_prime(input1,input2))

################################################
lst=[3,1,5,2,4,6,7,9,11,8,10,12,13,15,17,19]
lst=[1,3,5,7,11,13]#only odd nos
lst=[0,2,4,6,8,9]#only even nos
lst=[1,2,3,4,5,6,7,8,9]#odd and even alternate
lst=[2,4,5,6,8]#single odd
curr_len=0
curr_sum=0
max_len=0
longest_sums=0
for num in lst:
    if num%2!=0:
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
       

    
lst=[3,-1,-2,5,-3,-4,-5,6,-7,-8,-9,-10,-11,-12]
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
       

def minminusproduct(input1,input2):
    min_num=min(input1)
    subtracted_array=[x-min_num for x in input1]
    result_array=[x*min_num for x in subtracted_array]
    return result_array
input1=[4,8,2,6]
input1=[4,4,4,4]
input1=[4,8,2,6]
input2=0
minminusproduct(input1,input2)

#find password:
#detective buckshee juniour has been approched
#by the shantinekatan kids society for help in
#inding the password to the game complex. after
#hearing the secenerio,detective buckshee junior
#realizes that he will need a program's support.
#he contacts you and requests your help
#please help        
from collections import counter

def find_password(input1,input2,input3,input4,input5):
    def is_stable(number):
        digit_counts=counter(str(number)).values()#get digit frequency
        unique_counts=set(digit_counts)#convert frequency to set
        only_one_unique_count=len(unique_counts)#cheak if all counts are same
        
        return only_one_unique_count
    numbers=[input1,input2,input3,input4,input5]
    stable_sum=sum(num for num in numbers if is_stable(num))
    unstable_sum=sum(num for num in numbers if not is_stable(num))
    return stable_sum-unstable_sum

input1,input2,input3,input4,input5=12,1313,122,678,898
password=find_password(input1, input2, input3, input4, input5)
print("password:",password)

#for a input n,print following pattern where each
#line of n lines of output will contain a n 
#digited number starting from 1 to n and rest
#of the digits will be starting digit + 1.

n=int(input("enter the number:"))
for i in range(n):
    print(i+1,end="")
    for j in range(n-1):
        print(i+2,end="")
    print("")
    
    
#reverse the number
def reverse_string(s):
    return s[::-1]#using slicing for better performance

input_string="abcde"
output_string=reverse_string(input_string)
print(output_string)

#another method to solve reverse the number
def reverse_string(s):
    return''.join(s[i]for i in range(len(s)-1,-1,-1))#using string concatenation

input_string="abcde"
output_string=reverse_string(input_string)
print(output_string)

#pascal triangle
def pascal_triangle(n):
    triangle=[]#create empty list to store rows
    
    for i in range(n):
        row=[1]#every roe starts with 1
        if i>0:#from the second row onward
            for j in range(1,i):
                row.append(triangle[i-1][j-1]+triangle[i-1][j])#sum of two numbers above
            row.append(1)#every row ends with 1
        triangle.append(row)#add  row to the triangle
    return triangle

#function to print pascal triangle
def print_triangle(triangle):
    for row in triangle:
        print(*row)#simple last print
        
n=int(input("enter number of rows:"))
triangle=pascal_triangle(n)
print_triangle(triangle)


