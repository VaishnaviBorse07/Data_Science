# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 15:03:19 2025

@author: vaish
"""
###################################################
'''PANDAS'''
###################################################
import pandas as pd
tech=[['spark',20000,'30days'],['pandas',2000,'40days'],]
df=pd.DataFrame(tech)
print(df)

column_names=['courses','fees','duration']
row_label=['a','b']
df=pd.DataFrame(tech,columns=column_names,index=row_label)
print(df)

df.dtypes  #it is used to check the datatype 
types={'course':str,'fees':float,'duration':str}
df.dtypes

#when we create dataframe using dictionary then it is creating the dataframe coloumn wise and when we are creating it with the list then it is going to create row wise

tech={'courses':['spark','pyspark','hadoop'],
      'fees':[2000,25000,26000],
      'duration':['30days','40days','50days'],
      'discount':[1000,2000,3000]}
df=pd.DataFrame(tech)
df

df.to_csv('data_file.csv')

df_new=pd.read_csv('data_file.csv')


#various operations on dataframe
import pandas as pd
import numpy as np
technologies=({'course':['spark','pyspark','hadoop','python','pandas',np.nan,'spark','pthon'],
               'fees':[2000,3000,4000,5000,6000,7000,8000,7999],
               'duration':['30days','40days','50days','60days','','80days','90days','100days'],
               'discount':[100,200,300,400,500,600,700,800]})
row=['r0','r1','r2','r3','r4','r5','r6','r7']
df_1=pd.DataFrame(technologies,index=row)
df_1

df_1.columns
df_1.columns.values  #it prints about the array
df_1.index
df_1.dtypes


#if we want to acess the single coloumn of the dataframe then we use
df_1['fees']
df_1[['fees','duration']]

#[star_row:end_row,star_coloumn:end_coloumn]
df2=df_1[0:5,:]
df['duration','discount'][0:8]

#acess a particular cell only 
df_1['duration'][3]
df_1['fees']=df_1['fees']-100
df_1['fees']

#df.describe only work on numerical coloumns catogarical data means strings and no combination
df_1.describe()   #this function ids also called as 5 no summary 

df_1.columns=['a','b','c','d']
df_1

df2=df_1.rename({'a':'c1','b':'c2'},axis=1)
df2=df_1.rename({'a':'c1','b':'c2'},axis='columns')
df2=df_1.rename(columns={'a':'c1','b':'c2'})
df2

#########################################
import pandas as pd
import numpy as np
technologies=({'course':['spark','pyspark','hadoop','python','pandas',np.nan,'spark','pthon'],
               'fees':[2000,3000,4000,5000,6000,7000,8000,7999],
               'duration':['30days','40days','50days','60days','','80days','90days','100days'],
               'discount':[100,200,300,400,500,600,700,800]})
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_labels)
#Drop DataFrame Rows and Columns
df=pd.DataFrame(technologies,index=row_labels)

#Drop rows by labels
df1=df.drop(['r1','r2'])
df1
df=pd.DataFrame(technologies,index=row_labels)
#delete row by position
df1=df.drop(df.index[[1,3]])
df1
#delete rows by index range
df1=df.drop(df.index[2:])
df1
#when you have default indexs for rows
df=pd.DataFrame(technologies)
df1=df.drop(0)
df1

df=pd.DataFrame(technologies)
df1=df.drop([0,3])#it will delete the row 0 and row 3
df1

df1=df.drop(range(0,2))#it will delete 0 and 1
df1

###########################################
#Pandas Select Rows by Index(position/label)
df=pd.DataFrame(technologies,index=row_labels)
df2=df.iloc[2] #select Row by index
df2
df2=df.iloc[[2,3,6]] #select rows by index list
df2
df2=df.iloc[1:5] #select rows by integer index range
df2
df2=df.iloc[:1]#select first row
df2
df2=df.iloc[:3]#select first 3 rows
df2
df2=df.iloc[-1:]#select last row
df2
df2=df.iloc[-3:]#select last 3 row
df2
df2=df.iloc[::2]#selects alternate rows
df2

#Select Rows by Index Labels
df2=df.loc['r2']
df2
df2=df.loc[['r2','r3','r6']]
df2
df2=df.loc['r1':'r5']
df2
df2=df.loc['r1':'r5':2]
df2

#pandas select columns by name or index
#by using df[]Notations
df2=df['course']
df2
#selectmultiple columns
df2=df[["course","fees","duration"]]
df2
df2=df.loc[:,["course","fees","duration"]]
df2
#select column between two columns
df2=df.loc[:,'fees':'Discount']
#select columns by range
df2=df.loc[:,'duration':]
#Select the columns by range
#all the columns upto duration
df2=df.loc[:,:'duration']
df2=df.loc[:,::-2]

###########################################################
import numpy as np
import pandas as pd
import matplotlib as plt

df=pd.read_csv(r"E:\Vaishu coding\Data Science\2-Python\melb_data.csv")
df
df.describe()
df
df2=df.iloc[:1]
df2
df2=df['Propertycount']
df2
df2=df.iloc[1,1]
df2
df2=df.drop(0)
df2
df2=df.drop(range(1,11))
df2
df4=df.iloc[1:11]
df4
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7','r8','r9']
df4=pd.DataFrame(df4,index=row_labels)
df4
df.columns
df.columns.values  #it prints about the array
df.index
df.dtypes

#np.nan, None and ''
import pandas as pd
import numpy as np
technologies={
    'Categories':["Spark","Pyspark","Hadoop","Python"],
    'Fee':[20000,25000,27000,22000],
    'Duration':['','40days',np.nan,None],
    'Discount':[1000,1500,1200,1700] 
    }
indexes=['r1','r2','r3','r4']
df=pd.DataFrame(technologies,index=indexes)
print(df)
df=pd.DataFrame(technologies,index=indexes)
df2=df.dropna() ##dropping np.nan and None
print(df2)


#drop nan and None containing rows
df_clean=df.dropna(subset=['Duration'])

#removing empty strings containing rows as well
df_clean=df_clean[df_clean['Duration']!='']


#############################################
#Converting all the columns into same data type using astype

df=df.astype(str)
df.dtypes

#now converting some specific columni into integer and some to float
df=df.astype({"Fee":int,"Discount":float})
print(df.dtypes)

#doing the same conversionn using a list
cols=["Fee","Discount"]
df=pd.DataFrame(technologies)
df[cols]=df[cols].astype('float') #u are giving the data type with ''
df.dtypes

"""But Python (specifically, pandas) is designed to interpret that
 string as the name of a data type.
 'float' is a string → pandas internally
 looks it up in a type mapping dictionary.
It knows 'float' → maps to Python's float class (float).
So pandas reads it as: "Convert this column to type float."
"""
#by using for loop
for col in ['Fee','Discount']:
    df[col]=df[col].astype('float')
    
    
#Raising or ignoring error while conversion of column is failed
df=df.astype({"Categories":int},errors='ignore')
df.dtypes

df=df.astype({"Categories":int},errors='raise')

####################################################
#using DataFrame.to_numeric() to convert data to numeric
df["Fee"]=pd.to_numeric(df["Fee"])
df.dtypes
##
#converting multiple to numeric type using apply method
df=pd.DataFrame(technologies)
df.dtypes
 df[['Fee','Discount']]=df[['Fee','Discount']].apply(pd.to_numeric)
df.dtypes

#quic example to get number of rows in Data frame
rows_count=len(df.index)
row_count=len()

#Using DataFrame.apply to apply somwthing to column
import pandas as pd
import numpy as np
data=[(3,5,7),(2,4,6),(5,8,9)]
df=pd.DataFrame(data,columns=['A','B','C'])


#adding 3 into all cells using apply()
def add_3(x):
    return x+3
df2=df.apply(add_3)

#using apply() modify only single column
import pandas as pd
df=pd.DataFrame(data,columns=['A','B','C'])
def add_4(x):
    return x+4
df['B']=df['B'].apply(add_4)

#for multiple columns
#using lambda function

df["A"]=df["A"].apply(lambda x:x-2)
df

#using panads.dataframe.transform
df
def add_2(x):
    return x+2 
df=df.transform(add_2)

#using map function
df['A']=df['A'].map(lambda A:A/2)
print(df)


'''
why does it become int32?
Pandas internally chooses the most efficient
platform-dependent NumPy dtype that corresponds to Python's int. This depends on your operating system
and Python/NumPy version: On 32-bit systems, int usually maps to int32
On 64-bit systems, int often maps to int64
However, sometimes due to memory optimization
or system constraints, pandas might still pick int32
even on a 64-bit system
'''
#you can explicitly control the dtype like this:
df = df.astype({"fee":"int64","Discount":"float64"})
################################################
import pandas as pd

# Step 1: Create or load the DataFrame
data = {
    "fee": ["100", "200", "300"],
    "Discount": ["10.5", "20.0", "15.25"]
}
df = pd.DataFrame(data)

# Step 2: Convert data types
df = df.astype({"fee": "int64", "Discount": "float64"})

print(df.dtypes)
print(df)

################################################
#using Numpy function on single column
import pandas as pd
import numpy as np
data = [(3,5,7),(2,4,6),(5,8,9)]
df = pd.DataFrame(data , columns = ['A','B','C'])
print(df)
################################################
#using Numpy function on single column
#using dataframe apply() and [] operator
import numpy as np
df['A'] = df['A'].apply(np.square)
print (df)
############################
import numpy as np
df['A'] = df['A'].map(lambda A: A/2)
print (df)
#####################################
#using numpy square method
#using numpy square() and [] operator
df['A'] = np.square(df['A'])
print(df)
######################################
#Pandas groupby() with exanples
import pandas as pd
technologies = ({
    'courses':['Spark',"PySpark","Hadoop","Python",
               "Pandas","Hadoop","Spark","Python","NA"],
    'fee':[22000,25000,23000,24000,26000,25000,
           25000,22000,1500],
    'Duration':['30days',"50days","55days","40days",
                "60days","35days","30days","50days","40days"],
    'Dicount':[1000,2300,1000,1200,2500,None,1400,1600,0]
    })

df = pd.DataFrame(technologies)
print(df)
#############################
#use groupby() to compute the sum
df2 = df.groupby(["courses"]).sum()
print (df2)
##################################
#group by multiple column
df2 = df.groupby(['courses', 'Duration']).sum()
print(df2)
#####################################
#Add Index to teh grouped data
#Add Row Index to the group by  result
df2 = df.groupby(['courses','Duration']).sum().reset_index()
print(df2)

###########################################
#get the list of all column names from headers
Column_headers = list(df.columns.values)
print("the column Header :",Column_headers)

##################################
#using list(df) to get the column headers as a list 
column_headers = list(df.columns)
column_headers
#using list(df)to get the list of all columns
column_headers = list(df)
column_headers

########################################
#########################################
#Pandas Shuffle DataFrame Row
#shuffle the dataframe rows and return all rows
df1 = df.sample(frac = 1)
print(df1)

#Create a new index starting from zero
df1 = df.sample(frac = 1).reset_index()
print(df1)

#########################################
#Drop shuffle index
df1 = df.sample(frac = 1).reset_index(drop=True)
print(df1)

#########################################
import pandas as pd
technologies = ({
    'courses':['Spark',"PySpark","Hadoop","Python",
               "Pandas","Hadoop","Spark","Python","NA"],
    'fee':[22000,25000,23000,24000,26000,25000,
           25000,22000,1500],
    'Duration':['30days',"50days","55days","40days",
                "60days","35days","30days","50days","40days"],
    'Discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
    })

df = pd.DataFrame(technologies)
print(df)


####################################################
import pandas as pd
technologies={'Courses':["Spark","PySpark","Python","pandas"],
              'Fees':[20000,25000,22000,30000],
              'Duration':['30 days','40 days','35 days','50 days']}
index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies,index=index_labels)

technologies2={'Courses':["Spark","Java","Python","Go"],
               'Discount':[2000,2300,1200,2000]}
index_labels2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index=index_labels2)

df3=df1.join(df2,lsuffix="_left",rsuffix="_right")
print(df3)

#pandas inner-join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how="inner")
print(df3)

#right
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how="right")
print(df3)

#left
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how="left")
print(df3)

#using panda merge
df3=pd.merge(df1,df2)
print(df3)

df3=df1.merge(df2)
print(df3)

df=pd.DataFrame({'Courses':["Spark","PySpark","Python","pandas"],
                 'fees':[20000,25000,22000,24000]})

df1=pd.DataFrame({'Courses':["Pandas","Hadoop","Hyperion","java"],
                  'fees':[25000,25200,24500,24900]})

data=[df,df1]
df2=pd.concat(data)
print(df2)

df=pd.DataFrame({'Courses':["Spark","PySpark","Python","Pandas"],
                 'fees':[20000,25000,22000,24000]})
df1=pd.DataFrame({'Courses':["Unix","Hadoop","Hyperion","Java"],
                  'fees':[25000,25200,24500,24900]})
df2=pd.DataFrame({'Duration':["30Days","40Days","35Days","60Days","55Days"],
                  'Discount':[1000,2300,2500,2000,3000]})
df3=pd.concat([df,df1,df2])
print(df3)

df=pd.read_csv('courses.csv')
print(df)
df.to_excel(r'E:\Vaishu coding\Data Science\2-Python\courses.xlsx')

import pandas as pd
df=pd.read_excel(r'E:\Vaishu coding\Data Science\2-Python\courses.xlsx')
print(df)


########################################################################
'''NUMPY'''
########################################################################
#all()
import numpy as np
x=np.array([1,2,3])
x
np.all(x)

x=np.array([1,2,3,0])
np.all(x)

#any()
x=np.array([1,0,0])
np.any(x)
x=np.array([1,2,np.nan,np.inf])
x
#isfinite()
np.isfinite(x)

#isnan()
np.isnan(x)

#greater and greater_equal
x=np.array([3,5])
y=np.array([2,5])
np.greater(x,y)
np.greater_equal(x,y)

#identity
array_2D=np.identity(3)
array_2D

#random.normal
rand_No=np.random.normal(0,1,2)
rand_No

#arrange
a=np.arange(10,22)
a

##########################################
import numpy as np
lst=[1,2,3]
arr=np.array(lst)
arr
arr.ndim
arr.shape
type(arr)

arr_two=np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
arr_two.ndim
arr_two.shape

mat=np.matrix([[1,2,3],
               [4,5,6],
               [7,8,9]])
mat.ndim
mat.shape

arr=np.random.randint(1,100,9)
arr
arr.ndim
new_arr=arr.reshape(3,3)
new_arr.ndim
new_arr.ravel()#multi-dimensional array to single dimension array
arr[2]
arr[2:6]

import numpy as np
arr=np.random.randint(1,100,9)
arr.ndim
new_arr=arr.reshape(3,3)
new_arr.ndim
new_arr.ravel()
arr[2]
#Extracting ele from 2 to 5
arr[2:6]
new_arr
'''
array([[12,25,42],
       [83,46,67],
       [63,30,37]])
'''
new_arr[2,1:3]
new_arr[[0,2,0,2],[0,0,2,2]]

arr=np.random.randint(1,100,9)
arr
np.sqrt(arr)
np.sin(arr)
np.exp(arr)
np.log(arr)
np.mean(arr)
np.median(arr)
####################################
arr1=np.array([10,20,30,40,50,60,70])
arr1
arr1.mean()
np.percentile(arr1,25)#q1
np.percentile(arr1,50)#q2
np.percentile(arr1,75)#q3

import numpy as np
import matplotlib.pyplot as plt
A=np.array([[11,12,13],[21,22,23],[31,32,33]])
A
A.ndim
A.shape
A.size

A[1,2]
A[1][2]
A[0][0]
A[0][0:2]
#Addition of two arrays
X=np.array([[1,0],[0,1]])
X
Y=np.array([[2,1],[1,2]])
Y
Z=X+Y
Z
#Multiplying arrays
Y=np.array([[2,1],[1,2]])
Y
Z=2*Y
Z
Z=X*Y
Z
A=np.array([[0,1,1],[1,0,1]])
A
B=np.array([[1,1],[1,1],[-1,1]])
B
Z=np.dot(A,B)
Z
'''The componentwise product of matrices is called 
the Hadamard product or sometimes the Schur
 product. Given two m by n matrices A and B, 
 the Hadamard product of A and B, written A ∘ B,
 is the m by n matrix C with elements given by 
 cij = aij bij.'''
 c=np.array([[1,1],[2,2],[3,3]])
 c
 c.T
###############################################
#To check version of any package
import numpy as np
print(np._version_)
print(np.show_config())
###############################################
'''Write a numpy program to test element wise for
complex no,real no in given array also test if a given
number is of scaler type or not'''
import numpy as np
a=np.array([1+1j,1+0j,4.5,3,2,2j])
print("Original array")
print(a)
print("Checking for complex number:")
print(np.iscomplex(a))
print("Checking for real number:")
print(np.isreal(a))
print("Checking for scaler type:")
print(np.isscalar(3.1))#True
print(np.isscalar([3.1]))#False
############################################
import numpy as np
p=[[1,0],[0,1]]
p=np.array(p)
q=np.array([[1,2],[3,4]])
print("Original Matrix:")
print(p)
print(q)
result=np.outer(p,q)#Hadamard product
print(result)

#############################################
import numpy as np
a=np.array([[1,2],
            [3,4]])
b=np.array([[5,6],
            [7,8]])
hadamard=a*b
print("Hadamard product:",hadamard)

#############################################
import numpy as np
a=np.array([1,2])
b=np.array([3,4,5])
outer=np.outer(a,b)
print("Outer product:",outer)

############################################
import numpy as np
p=np.array([[1,0],[0,1]])
q=np.array([[1,2],[3,4]])
print(p)
print(q)
result1=np.cross(p,q)
r2=np.cross(q,p)
print("Cross product (p,q):",result1)
print("Cross product (q,p):",r2)
##############################################
import numpy as np
from numpy import linalg as la
a=np.array([[1,0],[1,2]])
print("Original 2d array:",a)
print("Determinent=",la.det(a))

################################################
import numpy as np
m=np.mat("3 -2;1 0")
print("Original matrix:")
print("a\n",m)
w,v=np.linalg.eig(m)
print("Eigen vector:",w)
print("Eigen value:",v)

###########################################
'''Inverse of matrix'''
import numpy as np
m=np.array([[1,2],[3,4]])
print("Original matrix")
print(m)
result=np.linalg.inv(m)
print("Inverse of matrix:")
print(result)

###########################################
import matplotlib.pyplot as plt
import seaborn as sns
tips=sns.load_dataset("tips")
tips.head()
sns.displot(tips.total_bill,kde=True)  #here the kde is used to show the line of ditribution 
sns.jointplot(x=tips.tip,kde=True)
'''doistribution is right skewed most of the cutomers have given the tips on the left side between 1 to 4 dollar '''
sns.displot(tips.size,kde=True)
sns.jointplot(x=tips.tip,y=tips.total_bill,kind='hex') #hex is used to represent in the form of hexagoan
'''kind='reg'#reg is to add density line '''

'''catter plot(centre):
    each point represent oberservation of each customer (a customers bills coresponds to the tip)
    there is a positive correalation as  total bill increases the tips is also increase however the increased is not perfectly liner-some varition also exist especially for the higher bills histogram on the top is for the x axis 
    shows the sistribution of the tip amount ,most tips falls between 2 and 5
    with fewer falls at the higher end 
    and historgram in the right side is for the y axis 
    show the distribution of total bills 
    the mahority of bills are in the 10 to 20 dollrs range '''
    
sns.pairplot(tips,kind='reg')

sns.displot(tips.sex,kde=True)
sns.jointplot(x=tips.sex,y=tips.tip,kind='hex')


tips.time.value_counts()
sns.pairplot(tips,hue="time")
'''there are more no of cutomers are present int the dinner time as compared to the lunch time '''
sns.pairplot(tips,hue="sex",kind='reg')
'''mens have given more noo of tips as compared to the femals '''
sns.pairplot(tips,hue="smoker",kind='reg')
'''there are less smokers are present as compared to smoker '''
sns.pairplot(tips,hue="day",kind='reg')
'''the no of cutomers are high in saturday  and most tips are given in  saturday also the total bills are also maximum in saturday'''

'''sunday follows closely with a broad range of bills 
friday has a narrower spread 
indicating fewer total bills,mostly lower
thurday (blue) is more consistent but less frequent than weekends.tips follows the same trend like total bills '''

sns.heatmap(tips.corr(numeric_only=True),annot=True)
'''
Understanding Correlation Coefficients
Ranges from -1 to +1.
+1->perfect positive correlation(both increases together)
0->no coorelation
-1->perfect negative correlation(one increases, the)
total_bill & tip  0.68   strong positive correlation
total_bill & size  0.50  moderate positive correlation
tip & size 0.49 Moderate correaltion- bigger group
'''
tips.dtypes
sns.boxplot(tips.total_bill)#their are outliers in total bill
sns.boxplot(tips.tip)
sns.countplot(x = 'day' , data = tips)#highest number of customer are on saturday
sns.countplot(y = 'sex' , data = tips)#male customer are more than female
tips.sex.value_counts().plot(kind='pie')
tips.sex.value_counts().plot(kind='bar')

sns.countplot(data = tips[tips.time == 'Dinner'], x = 'day')
sns.countplot(data = tips[tips.time == 'Lunch'],x='day')

fg = sns.FacetGrid(tips,row = 'smoker',col = 'time')
fg.map(sns.histplot, 'total_bill')

'''
this is a facet grid of histograms
showing the distribution of total bills
across different smoking statuses and time of day
(Lunch vs Dinner)
Top-left : Smokers during lunch
Top-right : Smokers during Dinner
Bottom- left : Non Smokers during lunch
Bottom right : Non smokers during Dinner
Smokers vs Non Smokers
Dinner(top-right vs Bottom-right):
Both Smokers and non-smokers show similar bill
Smokers have a slightly more spread-out
distribution , indicatng more variability

Lunch (Top-Left vs Bottom left):
Non smokers (bottom left) make up the majority
of lunch patrons.
Smokers(top-left) are much fewer at lunch,
with total bills mostly under $20
Lunch vs Dinner
Dinner is clearly more popular regardless
of smoking status
Total bills are generally higher and
more varied at dinner , especially for smokers

'''

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#load dataset
tips = sns.load_dataset('tips')

#histogram of total bill
plt.hist(tips['total_bill'],bins = 20,color = 'skyblue',
         edgecolor = 'black')
plt.title('Total BillDistribution')
plt.xlabel('Total Bill')
plt.ylabel('Count')
plt.show()

#2.Histogram for tip
plt.hist(tips['tip'],bins = 20,color = 'lightgreen',
         edgecolor = 'black')
plt.title('Tip Distribution')
plt.xlabel('Tip')
plt.ylabel('Count')
plt.show()

#3.Scatter plot of tip vs total bill
plt.scatter(tips['tip'],tips['total_bill'],color='purple',edgecolor='purple',alpha = 0.6)
plt.title('Tip vs Total Bill')
plt.xlabel('Tip')
plt.ylabel('Total Bill')
plt.show()

#simple correlation heatmap
corr = tips.corr(numeric_only = True)
plt.imshow(corr, cmap = 'coolwarm', interpolation = 'none')
plt.colorbar()
plt.xticks(range(len(corr)),corr.columns,rotation = 45)
'''
plt.xticks(...)
This fucntion controls the labels on the x-axis
where the ticks are placed
what labels are shown
how teh labels are rotated or styled
range(len(color))
this generates the positions for the ticks:
corr is a square matrix (like 3*3 if there are 3 numeric columns)
len(corr) gives how many coloumns (and rows) there are,
say:3,

range (len(corr))-> [0,1,2]-> places ticks at position 0,1,2
corr.columns
these are the labels for those tick positions:
    ['total bill','tip','size']
    so now you're labeling tick 0 as 'total bill' , tick 1 as 'tip'
'''

plt.yticks[range(len(corr)),corr.columns]
plt.title('Correaltion Matrix')
plt.show()

#5.BOXPLOT
plt.boxplot(tips['total_bill'])
plt.title('Boxplot - Total Bill')
plt.show()

plt.boxplot(tips['tip'])
plt.title('Boxplot - Tip')
plt.show() 

#6.BARGRAPH 
tips['day'].value_counts().plot(kind = 'bar',color = 'orange')
plt.title('Count by Day')
plt.xlabel('Day')
plt.ylabel('Count')
plt.show()

#7.Count of Gender

tips['sex'].value_counts().plot(kind = 'bar',color ='lightblue')
plt.title('Count by Gender')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.show()
#insight : number of male customers are more in the 
#comparison of females
##########################################################
#Gender pie chart
tips['sex'].value_counts().plot(kind = 'pie',autopct = '%1.1f%%')



'''
The autopct = ' %1.1f%%' parameter is used in
Matplotlib's pie() function to display the
percentage value on each slice of a pie chart
Breakdown of '%1.1f%%':
1.1f means:
1 = minimum width of the number (not strictly neede here)
.1f format the number as a float with 1 decimal place
the final %% is to display a literal percent sign %
(because % has special meaning in formatting string,
 so we escape it with another %)


Example:
import matplotlib.pyplot as plt
labels = ['A','B','C']
sizes = [30,45,25]

plt.pie(sizes,labels=labels,sutopct = '%1.1f%%')
plt.axis('equal')
plt.show()
'''

plt.title('Gender Distribution')
plt.ylabel('')
#even though pie charts doent have y axis
#matplotlib still has that axis object in the
#background . so setting ylabel('') just makes
#sure nothing is displayed there
plt.show()

#write a python program to draw a line with
#suitable label in the x axis,y axis and a title
import matplotlib.pyplot as plt
X=range(1,50)
Y=[value*3 for value in X]
print("Values of X:")
print(*range(1,50))
print("Values of Y (thrice of X):")
print(Y)
#plot lines and/or markers to the axes
plt.plot(X,Y)
#Set the x axis label of the current axis
plt.xlabel('x-axis')
#Set the y axis label of the current axis
plt.ylabel('y-axis')
#set a title
plt.title('Draw a line')
#show and display the figure
plt.show()


#using given axis values with suitable label
#in the x-axis,y-axis,and a title
import matplotlib.pyplot as plt
#x-axis values
x=[1,2,3]
#y-axis values
y=[2,4,1]
#plot lines and/or markers to the axes
plt.plot(x,y)
#Set the x axis label of the current axis
plt.xlabel('x-axis')
#Set the y axis label of the current axis
plt.ylabel('y-axis')
#set a title
plt.title('Sample graph')
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv(r"E:\Vaishu coding\Data Science\2-Python\fdata.csv")
df.plot()
plt.show()

import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]

#line 2 points
x2=[10,20,30]
y2=[40,10,30]
#set the x-axis label of the current axis.
plt.xlabel('x-axis')
#set the y-axis label of the current axis.
plt.ylabel('y-axis')
#set a title
plt.title('Two or more lines with different widths and colors')
#display the figure
plt.plot(x1,y1,color='lightgreen',linewidth=3,label='line1-width-3')
plt.plot(x2,y2,color='purple',linewidth=5,label='line1-width-5')
plt.legend()
plt.show()

################################################################
import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]

#line 2 points
x2=[10,20,30]
y2=[40,10,30]
#set the x-axis label of the current axis.
plt.xlabel('x-axis')
#set the y-axis label of the current axis.
plt.ylabel('y-axis')
#set a title
plt.title('Two or more lines with different widths and colors')
#styling the plots
plt.plot(x1,y1,color='lightgreen',linewidth=3,label='line1-dotted',linestyle='dotted')
plt.plot(x2,y2,color='purple',linewidth=5,label='line2-dashed',linestyle='dashed')
#adds the label
plt.legend()
#displays the figure
plt.show()

##################################################
#write a python program to plot two or more
#lines and set the line markers
import matplotlib.pyplot as plt
x=[1,4,5,6,7]
y=[2,6,3,6,3]
plt.plot(x,y,color='red',linestyle='dashdot',linewidth=5,label='x-doted',marker='o',markerfacecolor='blue',markersize=12)
#set the y-limits oof the current axes.
plt.ylim(1,8)
#set the x-limits oof the current axes.
plt.xlim(1,8)
#naming the x axis
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Display marker')
plt.show()

############################################

import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0.,5.,0.2)
# green dashes, blue squares and red triangles

plt.plot(t,t,'g--',t,t**2,'bs',t,t**3,'r^')
'''
x = t, y = t  
'g--' = green (g) dashed line (--)  
Plots a diagonal dashed green line (y = x)

t, t**2, 'bs'  
x = t, y = t**2  
'bs' = blue (b) squares (s) as markers  
Plots t² as blue squares

t, t**3, 'r^'  
x = t, y = t**3  
'r^' = red (r) triangle-up markers (^)  
Plots t³ as red triangles
'''
plt.show()

###########################################
#use of plt.xticks
import matplotlib.pyplot as plt
x_pos=[0,1,2,3]
x=['Apple','Banana','Mango','Orange']
plt.bar(x_pos,[10,15,7,12])
plt.xticks(x_pos,x)
plt.ylabel('Quantity')
plt.title('Fruits stock')
plt.show()

###########################################
#wap to display a bar chart of the popularity of pl
import matplotlib.pyplot as plt
x=['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.7,17.6,8.8,8,7.7,6.7]
x_pos=[i for i,_ in enumerate(x)]
'''
x_pos=[i for i,_ in enumerate(x)]
This creates a list of index positions for each langauge
enumerate(x) gives (index,language) pairs:
(0,'Java'),(1,'Python'),...,(5,'C++')
[i for i._in enumerate(x)] extracts just the indices:
    
x_pos=[0,1,2,3,4,5]

'''
plt.bar(x_pos,popularity,color='lightblue')
plt.xlabel("Language")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language\n"+"Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos,x)
plt.show()

#################################################
import matplotlib.pyplot as plt
x=['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.7,17.6,8.8,8,7.7,6.7]
x_pos=[i for i,_ in enumerate(x)]
plt.barh(x_pos,popularity,color='lightgreen')
plt.xlabel("Popularity")
plt.ylabel("Languages")
plt.title("Popularity of Programming Language\n"+"Worldwide, Oct 2017 compared to a year ago")
plt.yticks(x_pos,x)
plt.show()

################################################
#Wap to create bar plot of scores by group and gender
#use multiple X values on the same chart for men and women
import matplotlib.pyplot as plt
import numpy as np
#data to plot
n_groups=5
men_means=(22,30,33,30,26)
women_means=(25,32,30,35,29)
#create plot
fig,ax=plt.subplots()
index=np.arange(n_groups)
bar_width=0.35
opacity=0.8
rects1=plt.bar(index,men_means,bar_width,alpha=opacity,color='g',label='Men')
rects2=plt.bar(index,women_means,bar_width,alpha=opacity,color='r',label='Women')
plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index+bar_width,('G1','G2','G3','G4','G5'))
plt.legend()
plt.tight_layout()
plt.show()

