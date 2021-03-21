import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'name':['Tom','Jack','Stevr'],'Age':[28,37,29]}
df = pd.DataFrame(data,index=['rank1','rank2','rank3'],dtype=float)
print(df[:2])
'''
Pandas.DataFrame 方法处理二维数据
'''