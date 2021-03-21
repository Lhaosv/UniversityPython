# 利用DataFrame创建二维数组   Series创建一维数组
import pandas as pd
import numpy as np
d = {'name':pd.Series(['Tom','James','Ricky','Vin','Steve']),'Age':pd.Series([25,26,25,23,30]),'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20])}
df = pd.DataFrame(d)
print(df)
