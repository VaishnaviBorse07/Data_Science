# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 08:27:33 2025

@author: vaish
"""

import numpy as np 
#Sample Dataset
data=[10,12,23,23,16,23,21,16]
print("Original Data:",data)

#Step 1:Mean
mean=np.mean(data)
print("Mean:(Avg)",mean)

#Step 2:Mean Absolute Deviation(MAD)
#It's the average of absolute deviiations from the mean
mad=np.mean([abs(x-mean) for x in data])
print("Mean Absolute Deviation(MAD):",mad)

#Step 3:Variance
#It's the average of squared difference from the mean
variance=np.var(data)
print("Variance:",variance)

#Step 4:Standard Deviation
#It's the square root of the variance
std_dev=np.std(data)#by default,uses population st
print("Standard Deviation:",std_dev)

####################################################
#History and Math Test Scores from the image
history_score=[75,72,68,65,67,73]
math_score=[93,96,43,47,51,50]
def calculate_mad(scores):
    mean=sum(scores)/len(scores)
    mad=sum(abs(x-mean)for x in scores)/len(scores)
    return mad

#Calculate MAD
history_mad=calculate_mad(history_score)
math_mad=calculate_mad(math_score)

print("Mean Absolute Deviation (MAD):")
print(f"History Test:{history_mad:.2f}")
print(f"Math Test:{math_mad:.2f}")
'''I will suggest math faculty to focus more on students give 
them remedial class and more assignments '''
'''
Although both the History Test and the Math Test
have the same average score o 70
their mean Absolute Deviation(MAD)
tell a different story.
The MAD of the history test is lower which means the scores are 
closer to the mean.
the students perform more consistently with less variation in score.
the MAD of the math test is much higher,indicating that the score are more
spread out.This shows greater inconsistency ,with some students
scoring very high and others much lower .
'''

import math

#Dataset 1:from left table
scores_1=[75,72,68,65,67,73]

#Dataset 2:from right table
scores_2=[83,70,70,63,70,70]

def calculate_standard_deviation(scores):
    mean=sum(scores)/len(scores)
    squared_diffs=[(x-mean)**2 for x in scores]
    variance=sum(squared_diffs)/len(scores)
    std_dev=math.sqrt(variance)
    return std_dev
#Calculate Standard Deviation
std_dev_1=calculate_standard_deviation(scores_1)
std_dev_2=calculate_standard_deviation(scores_2)

print("Standard Deviation:")
print(f"Dataset 1:{std_dev_1:.2f}")
print(f"Dataset 2:{std_dev_2:.2f}")

'''
Even though both datasets have the same average(mean) 0

dataset 1(left table)
Standard deviation = 3.55
Most scores are close to the mean
(small) squared differences).
Indicates consistent performance
among students with low variability

Dataset 2(Right table)
Standard Deviation = 6.02
some scores (like 83 and 63) are far from the mean,
causing larger squared differences.
Indicates higher variability,
even though most students scored 70.

The presence of a few extreme values
(outliers) increases the spread.

Standard deviation reveals the consistency of 
data.A lower SD means values are tightly packed around
the mean, while a higher SD means they are more
spread out-even if the mean is the same.
This is a great example to teach why standard deviation
matters in analyzing performace,quality control,
or any situation where consistency is important.
'''

import numpy as np
#original weights
original_weights=[105,156,145,172,100]
#add 5 points to each for winter clothing
adjusted_weights=[weight+5 for weight in original_weights]
#calculate mean and SD
mean_original=np.mean(original_weights)
std_original=np.std(original_weights,ddof=1)
mean_adjusted=np.mean(adjusted_weights)
std_adjusted=np.std(adjusted_weights,ddof=1)

'''
ddof=1 in np.std()
ddof stands for delta degrees of freedom.
By default,np.std() uses ddof=0,which calculates the
population standard deviation,
when u set ddof=1, it calculates the 
sample standard deviation instead.
'''
print(f"original mean: {mean_original:.2f},original std deviation:{std_original}")
print(f"adjusted mean: {mean_adjusted:.2f},original std deviation:{std_adjusted}")

############################################################
import numpy as np

#original data
weights=[105,156,145,172,100]
#water formula: (weight*2.5)+740
water_intake=[(w*2.5)+750 for w in weights]
#calculate original stats
mean_weight=np.mean(weights)
std_weight=np.std(weights,ddof=1)
#calculate new stats
mean_water=mean_weight*2.5+750
std_water=std_weight*2.5
print(f"original mean weight:{mean_weight:.2f},original std dev:{std_weight:.2f}")
print(f"Mean water intake:{mean_water:.2f} ml")
print(f"std Dev of water:{std_water:.2f} ml")

#outliers
#a single data point that goes far outside the average
# value of a group of statistics.

import numpy as np
import pylab
import scipy.stats as stats
measurements=np.random.normal(loc=20,scale=5,size=100)
stats.probplot(measurements,dist='norm',plot=pylab)
pylab.show()
