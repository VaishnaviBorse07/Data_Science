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


