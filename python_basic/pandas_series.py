import numpy as np
import pandas as pd


s1=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s1.values)
print(s1['a'])

s2=pd.Series({'a':1,'b':3})
print(s2['a'])