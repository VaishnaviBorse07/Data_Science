# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 15:19:13 2025

@author: vaish
"""

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

result = int("".join(map(str,ascii_difference)))
print(f"final Output: {result}")

###########################################
def findStringCode(sentence):
    sentence=sentence.upper()
    words=sentence.split()
    word_sums=[]
    for word in words:
        length=len(word)
        total=0
        print("Processing word: {word}")
        for i in range(length//2):
           first_char=word[i]
           last_char=word[length-1-i]
           
           first_val=ord(first_char)-ord('A')+ 1
           last_val=ord(last_char)-ord('A')+ 1
           
           diff=abs(first_val-last_val)
           print(f"Pair:({first_char},{last_char})->({first_val}-{last_val})={diff}")
           total+=diff
           
        if length % 2==1:
           mid_char=word[length//2]
           mid_value=ord(mid_char)-ord('A')+1
           print(f"Middle Charater: {mid_char},Mapped Value:{mid_value}")
           total+=mid_value
        print(f"Total for {word}:{total}")
        word_sums.append(str(total))
        
    final_result=int("".join(word_sums))
    print(f"\nFinal Output: {final_result}")
    return final_result
sentence="WORLD WIDE WEB"
output=findStringCode(sentence)
            
#####################################################
'''Farah is one of the few associates in Global Safe
Lockers Corp Limited, who has access to the company's
exclusive locker that holds confidential information 
related to her division. The PIN to the locker gets
changed every two days. Farah receives the PIN in the
form of a string which she needs to decode to get the
single-digit numeric PIN.
The numeric PIN can be obtained by adding the lengths 
of each word of the string to get the total length,
and then continuously adding the digits of the total
length till we get a single digit.
For example, if the string is "Wipro Technologies", 
the numeric PIN will be 8.
Explanation:
Length of the word "Wipro" = 5
Length of the word "Technologies" = 12
Let us add all the lengths to get the Total Length = 5 + 12 = 17
The Total Length = 17, which is not a single-digit, so now let
us continuously  add all digits till we get a single digit i.e. 1+ 7 = 8
Therefore, the single-digit numeric PIN = 8
Farah approaches you to write a program that would generate the
single-digit numeric PIN if the string is input into the program. Help Farah by writing the function (method) that takes as input a string input1 that represents the sentence, and returns the single-digit numeric PIN.
Assumptions: For this assignment, let us assume that the given string will always contain more than one word.
Let's see one more example-
If the given string is "The Good The Bad and The Ugly", the numeric PIN would be = 5
Explanation:
Let us add lengths of all words to get the Total Length = 3+4+3+3+3+3+4= 23 Total Length = 23, which is not yet a single digit, so let us continue adding all digits of the Total Length, ie. 2+3=5
Therefore, single-digit numeric PIN =5
If the given string is "The Good The Bad and The Ugly", the numeric PIN would be = 5
Explanation:
Let us add lengths of all words to get the Total Length = 3+4+3+3+3+3+4= 23 Total Length = 23, which is not yet a single digit, so let us continue adding all digits of the Total Length, ie. 2+3=5
Therefore, single-digit numeric PIN =5
'''

input1="Wipro Technologies"
#Step 1:Split into words
words=input1.split()
words
#step 2:convert words into lists of characters
char_lists=[list(word) for word in words]
char_lists
#step 3:Count letters in each list
letter_counts=[len(chars) for chars in char_lists]
letter_counts
print("Character lists:",char_lists)
print("Letter Counts:",letter_counts)
def sum_digits(num):
    total=0
    while num!=0:
        last_digit=num%10
        total=total+last_digit
        num=num//10
    return total
print(sum_digits(456))
total=[sum_digits(i)for i in letter_counts]
total
total_sum=0
for i in total:
    total_sum=total_sum+i
total_sum

#################################################
input1="the good and the bad and ugly"
words=input1.split()
char_lists=[list(word) for word in words]
letter_counts=[len(chars) for chars in char_lists]
print(char_lists)
print(letter_counts)
def total_sum(num):
    total=0
    while num!=0:
        last_digit=num%10
        total=total+last_digit
        num=num//10
    return total
total=[total_sum(num)for num in letter_counts]
total
result=sum(total)
print('PIN',result)

############################################
def get_pin(input1):
    words=input1.split()
    total_length=sum(len(word)for word in words)
    while total_length>=10:
        total_length=sum(int(digit)for digit in str(total_length))
    return total_length
get_pin("Wipro Technologies")
get_pin("the good and the bad and ugly")
    
    
    