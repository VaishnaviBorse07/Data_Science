# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 08:12:21 2025

@author: vaish
"""

import pandas as pd
import numpy as np
df=pd.read_csv(r"E:\Vaishu coding\Data Science\3-Python\income.csv",names=["name","income"],skiprows=[0])
df
df.income.describe()
'''
Skewed Data:
The mean (1.4M) is much higher than the median (7,000), suggesting a right-skewed distribution.
→ There’s likely one or two very high incomes (outliers) pulling the average up.

Outlier Alert:
The maximum (10 million) is far above Q3 (7,750), which is a huge jump.
→ That 10 million is almost certainly an extreme outlier.

Low Variability Among Most Values:
The 25th–75th percentile range (IQR) is small:

Q1 = 5,500

Q3 = 7,750
→ Most incomes are clustered between 5,500 and 7,750, except for the big outlier.

High Standard Deviation:
Std = 3.77M → very large relative to the mean → confirms extreme spread due to that 10M value.
'''
df.income.quantile(0)
df.income.quantile(0.25,interpolation="higher")
df.income.quantile(0.5,interpolation="higher")
df.income.quantile(1)
#percentile_99=df.income.quantile
df['income'][3]=np.NAN
df
df.income.mean()
df_new = df.fillna(df.income.mean())
df_new