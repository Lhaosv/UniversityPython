import numpy as np
from scipy import linalg
"""
3x+2y=2
x-y=4
5y+z=-2
数组a表示未知数的系数矩阵，数组b表示等号右边方程组值的矩阵
"""
a = np.array([[3,2,0],[1,-1,0],[0,5,1]])
b = np.array([2,4,-2])
res1 = linalg.solve(a,b)
print("线性方程组的解是：",res1)
