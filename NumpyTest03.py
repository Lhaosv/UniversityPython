# 创建从1开始到10终止，步长为2的浮点型数组
import numpy as np
arr3 = np.arange(1,10,2,dtype = float)
print(arr3)
arr4 = np.arange(20) # 索引最大的范围
s = slice(1,20,3) # 从索引1开始到索引20停止，步长为3
print(arr4[s])
b = arr4[2:14:2]# 从索引2开始到索引14停止，步长为2
print(b)
