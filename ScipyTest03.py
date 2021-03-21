# 绘制二维空间图

import numpy as np
from scipy.interpolate import *
import matplotlib.pyplot as plt

# 两个维度空间点绘图
x = np.linspace(0,4,12)
y = np.cos(x**2/3+4)  #x**2表示x的平方
print(x,y)
plt.plot(x,y,'o')
plt.show()


