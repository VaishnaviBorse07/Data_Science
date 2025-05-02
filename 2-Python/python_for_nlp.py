# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 08:20:49 2025

@author: vaish
"""

#Regex
import re

#1. .(dot)-matches any character except newline
print(re.findall(r"a.c","abc aac acc adc a-c"))
#output=['abc', 'aac', 'acc', 'adc', 'a-c']

'''
a->match the letter a
.->match any one character (except newline \n)
c->matches letter c
so overall its looking for three character string where
the first letter is 'a'
the last letter is 'c'
the middle can be any character
abc(a + any character b + c)
abc(a + any character a + c)
abc(a + any character c + c)
abc(a + any character d + c)
abc(a + any character - + c)
'''

#2. ^(caret)-matches start of string
print(re.findall(r"^Hello","Hello World\nHello Python"))
#output:[Hello]
'''
^ -> this is the caret, and it means:
    "Matches the following patern only if it appears at the"
    Hello->This is the actual text you're trying to match.
    so ^Hello means:
    "Matches the word 'Hello' only if it is at the beginning of"
    input:"Hello World\nHello Python"
    "Hello World"
    "Hello Python" <-on a new line
    but since the ^ anchor only applies to the beginning
    of the whole string,it will match only the first
    "Hello", not the second one.
    Output:['Hello']
    
'''

#3. $(dollar)-matches end of string
print(re.findall(r"Python$","Hello Python"))
#output:['Python']

'''
Python->This is the text you're trying to match.
$->this means:
"Match this **only if it appears at the end of the string"
so Python$ means:
"match the word 'python' only if it's at the very end of string."
'''
print(re.findall(r"Python$","Hello Python Developer"))
#output:[]

#4. *(astrisk)-0 or more of the preceding character
print(re.findall(r"ab*c","ac abc abbc abbbc"))
#output:['ac', 'abc', 'abbc', 'abbbc']
'''
Pattern:ab*c
This pattern uses the astrisk *,which is one of the 
Breakdown:
a->Match the character 'a'
b*->Match zero or more 'b' characters
c->Match the character 'c'
word    Matches ab*c?  why?
ac       Yes           'b' appears zero times
abc      Yes           'b' appears once
abbc     Yes           'b' appears twice
abbbc    Yes           'b' appears thrice
'''

#5. +(plus) - 1 or more of the preceding character
print(re.findall(r"ab+c","ac abc abbc abbbc"))
#output:['abc', 'abbc', 'abbbc']
'''
ab+c
This pattern uses the plus + quantifier,
which is closely related to the *,
breakdown:
a ->Match the character 'a'
b+ -> Match one or more 'b' characters
c ->Match the character 'c'
So the full pattern matches:
'a' followed by at least one 'b',followed by 'c'
Let's check each word:
"ac" 
no 'b' between 'a' and 'c'.b+ requires at least one
"abc"
One 'b' -> matches 'ab+c'
"abbc"
two 'b's -> matches 'ab+c'
"abbbc"
three 'b's -> matches 'ab +c'
'''

#6. ? (question) - 0 or 1 of the preceding character
print(re.findall(r"ab?c","ac abc abbc abbbc"))
#output:['ac','abc']
'''
Pattern: ab?c
BREAKDOWN:
a -> Match the character 'a'
b? ->Mathc zero one  'b' character
c -> Match the character 'c'

so the full pattern matches
'a' followed by at most one 'b', followed by 'c'
let's check each word:
    
    word     Matches ab*c?     Why?
    ac       yes               'b' appears zero times(allowed)
    abc      yes               'b' appears one times(allowed)
    abbc     no                'b' appears two times(not allowed)
    abbbc    no                'b' appears three times(not allowed)
'''
#7. {}(curly braces)-exact or range of repetitions
print(re.findall(r"ab{2}c","abc abbc abbbc abbbbc"))
#output:['abbc']

'''
Pattern: ab{2}c
BREAKDOWN:
a -> Match the character 'a'
b? ->Mathc exactly 2 'b' character
c -> Match the character 'c'

so this regex will only matche
'a' followed by exactly 2 'b's, followed by 'c'
i.e teh string "abbc"
    
    word     Matches ab{2}c?    Why?
    abc       no               only 1 b -> needs 2
    abbc      yes              exactly 2 b's
    abbbc     No               three b's
    abbbbc    No               four b's
'''
#8. [](square brackets)-either b or c character set
print(re.findall(r"a[bc]d","abd acd aad aed"))
#output:['abd','acd']

#9. [^](negated set) - not in the set
print(re.findall(r"a[^bc]d","aad aed acd abd"))
#output:['aad', 'aed']
'''
Pattern: a[^bc]d
Breakdown:
a-> Match the character 'a'
[^bc]->Match any one character except 'b' or 'c'
The caret ^ inside square brackets negates the set.
d-> Match the character 'd'
so this pattern matches:
'a' followed by any character that is not b or c,
followed by 

word  Middle char
'''
#10.| (pipe)-logical or
print(re.findall(r"cat|dog","Ihave a cat and a dog"))
#o/p:-['cat', 'dog']
'''
pattern: cat|dog
breakdown:
    cat-> match the word 'cat' 
    dog-> match the word 'dog'
    \-> the or operator , which matches either the pattern so this pattern
    will match either cat or dog'
'''
#11 paranthesis () - grouping
print(re.findall(r"(ab)+","abab ab ababab"))
#o/p:-['ab', 'ab', 'ab']
'''
pattern:(ab)+
(ab)->group the character 'a'and 'b' together 
+ -> the plus quantifier means "one or more "of the precendance
so this pattern will match:
    one or more repetitons of the sequence'ab'
    word     matches              why
abab           yes              it matches exactly two 'ab'
ab             yes              it matches exactly one 'ab'
ababab         yes              it matches exactly three 'ab'
'''
# 12. \d - digit
print(re.findall(r"\d+", "123 abc 456"))
#o/p-['123', '456']
'''
pattern: \d+
\d-> matches any digit from 0 to 9
+ -> the plus quantifier means "one or more" of the precendance 
word           matches             why
123            yes             three digits, so it matches \d+
abc            no                 no digits here
456            yes             three digits here

'''
# 13. \D - no digits
print(re.findall(r"\D+","123 abc 456"))
#o/p-[' abc ']
'''
pattern: \D+
\D-> matches any non-digit from 0 to 9
+ -> the plus quantifier means "one or more" of the previous item 
word           matches             whys 
123            no             all digits are present
abc            yes             non-digits are present
456            no             all digits are present

'''
#14.\W -word character (alphanumeric+_)
print(re.findall(r"\w+","a_b 123 @!"))
#o/p:['a_b', '123']
'''
\w- matches any "word character ,that include
all letters : a-z,A-Z
all digits :0-9
the underscore:_
+- matches one or more of the above characters
so \W+ matches :
    any sequence of letters, digits,or underscore_.
'''
# 15. \w - non word character
print(re.findall(r"\W+","a_b 123 @!"))
#o/p:[' ', ' @!']
'''
\W -> matches any non-word character that means anything not a letter (a-z ,A-Z)
not a digit(0-9)
not the underscore_
+- match one or more of those non_word characters.
so 


'''
# 16. \s- whitespace
print(re.findall(r"\s+","a b\tc\nd"))
#o/p:[' ', '\t', '\n']
'''
\s- matches any whitespace character, including-
Tab \t
Newline \n
carriage return \r
from feed \f
vertical tab \v
+ -> matches one or more of the prvious 
character   type   matches     why
a          letter   no      not whitespace
' '         space    yes      whitespace
b           letter   no        not whitespace
\t         tab       yes       whitespace
c          letter    no
\n         newline   yes

'''

# 17. \S  - non whitespace
print(re.findall(r"\S+","a b\tc\nd"))
#o/p:['a', 'b', 'c', 'd']

'''
\S matches  any non - whitespace character that mesans,
everything except spaces(' ') tabs(\t) newlines(\n)
+ -> matches one or more of the preceding
\S matches group of character that are not whitespace

'''

# 18. re.sub ()- substitute using regex
text= "My number is 123-456-7890"
print(re.sub(r"\d{3}-\d{3}-\d{4}","--",text))
#o/p:My number is **--****
'''
\d{3}-> matches exactly 3 digits (e.g.123)
- -> matches a literal dash(-)
\d{3} -> another 3 digits 
- -> another dash
\d{4}-> exactly 4 digits

'''
# 19. re.split() - split by pattern (word tockanization)
print(re.split(r"[,;]","apple, banana;grape,orange"))
#o/p-['apple', ' banana', 'grape', 'orange']
'''
re.split(r"[,;]",.....)
re.split()is used to split a string using a 
regular expression pattern.
'''
#20. \b Matches:
#before the first letter/number of a word
text = "Hello world! Welcome to regex."
matches = re.findall(r"\b\w+\b",text)
print(matches)


text = "I love python and python is great."
matches = re.findall(r"\bpython\b",text)
print(matches)


text = "I likke python and java."
matches = re.findall(r"\python\b",text)
print(matches)

#######################
#Use case
import re
#1. extract order ids from log strings
logs="""
[INFO] order ID: SWY123456 placed at 6:45pm
[INFO] order ID: SWY987654 places at 7:10
"""
order_ids = re.findall(r"SWY\d{6}",logs)
print("Extracted order IDs:",order_ids)

# Validate email and phone number
customer_data=[
    {"email": "rahul.sharma@gmail.com","phone": "9373622645"},
    {"email": "gayatri99@gmail.com","phone": "9067222625"}]
email_pattern = r"^[\w\.-]+@[\w\.-]+\w+$"
phone_pattern = r"^[6-9]\d{9}$"
for customer in customer_data:
    valid_email = re.match(email_pattern,customer["email"])
    valid_phone = re.match(phone_pattern,customer["phone"])
    print(f"Validing {customer['email']} | Email:{bool(valid_email)}|phone:{bool(valid_phone)}")

# parse menu items and prices
import re
menu ="""
 1. paneer butter masala - 250
 2. chiken biryani -300
 3. veg thali - 180
 """
items = re.findall(r"\d+\.\s([\w\s]+)-\s?(\d+)", menu)
print("prased menu items & prices:", items)

# identitfy discount codes in notification messages
notifications = """
use code SWIGGY50 to get 50% off.
Hurry! Apply code FIRST100 for 100 off.
"""
discount_codes = re.findall(r"\b[A-Z]+\d*\b",notifications)
print("Discount codes:",discount_codes)

# clean customer reviews 
reviews = [
    "Food was awesom #happy",
    "Worst experience ever!!",
]
cleaned_reviews = [re.sub(r"[^\w\s.,!?]","",review) for review in reviews]
print("Cleaned Reviews:",cleaned_reviews)

#####################################################################

from PyPDF2 import PdfFileReader
from PyPDF2 import PdfReader
reader = PdfReader('python_tutorial.pdf')
print(len(reader.pages))
page = reader.pages[10]
text = page.extract_text()
print(text)



import re
chat2 = 'Hi: I have a problem with my order number 421889912' 
pattern = 'order[^\d](\d)'
matches = re.findall(pattern,chat2)
matches



import re
chat3 = 'Hi: Hello, i am haveing an problem with my order number # 421889912' 
pattern = 'order[^\d](\d)'
matches = re.findall(pattern,chat3)
matches

import re
chat4 = 'Hi: My order 421889912 is having an issue, I was charged 300$ when online it says 280$'
pattern = 'order[^\d](\d)'
matches = re.findall(pattern,chat4)
matches

def get_pattern_match(pattern,text):
    matches = re.findall(pattern, text)
    if matches:
        return matches[0]
get_pattern_match('order[^\d](\d)', chat2)

chat1 = 'Hi: you ask lot of questions 1235678912, abc@xyz.com'
chat2 = 'Hi: here it is: (123)-567-8912,abc@xyz.com'
chat3 = 'Hi: yes, phone: 1235678912 email: abc@xyz.com'
get_pattern_match("[a-zA-Z0-9_]@[a-z]\.[a-zA-Z0-9]*", chat1)
get_pattern_match("[a-zA-Z0-9_]@[a-z]\.[a-zA-Z0-9]*", chat2)
get_pattern_match("[a-zA-Z0-9_]@[a-z]\.[a-zA-Z0-9]*", chat3)

get_pattern_match("(\d{10})|(\(\d{3}\)-\d{3}-\d{4})",chat1)
get_pattern_match("(\d{10})|(\(\d{3}\)-\d{3}-\d{4})",chat2)
get_pattern_match("(\d{10})|(\(\d{3}\)-\d{3}-\d{4})",chat3)

text = '''
Musk in 2022
Senior Advisor to the President
Incumbent
Assumed office
January 20, 2025
Serving with Massad Boulos, Boris Epshteyn
President	Donald Trump
Preceded by	Tom Perez
Personal details
Born this is Elon Reeve Musk
June 28, 1971 (age 53)
Pretoria, South Africa
Citizenship	
South Africa
Canada
United States (from 2002)
Political party	Independent
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Domestic partner	Grimes (2018–2021)
Children	at least 14, including Vivian Wilson[1]
Parents	
Errol Musk (father)
Maye Musk (mother)
Relatives	Musk family
Education	University of Pennsylvania (BA, BS)
Occupation	
Co-Founder and CEO of xAI
CEO and product architect of Tesla
Founder, CEO, and chief engineer of SpaceX
Founder of the Boring Company, X Corp., and
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
President of the Musk Foundation
De facto leader of the Department of Government Efficiency
Awards	Full list
Signature	
'''
get_pattern_match(r'age (\d+)', text)
get_pattern_match(r'Born(.*)\n', text)
get_pattern_match(r'Born.\n(.)\(age',text).strip()

text1 = '''
Ambani in 2007
Born Mukesh Dhirubhai Ambani
19 April 1957 (age 68)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation	Businessman
Years active	1981–present
Organization	Reliance Industries
Title	Chairman and MD of Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parents	
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)
'''
get_pattern_match(r'age (\d+)', text1)
get_pattern_match(r'Born(.*)\n', text1)
get_pattern_match(r'Born.\n(.)\(age',text1).strip()