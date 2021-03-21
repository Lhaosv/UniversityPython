# 一维插值
import numpy as np
from scipy.interpolate import *
import matplotlib.pyplot as plt

# 两个维度空间点绘图
x = np.linspace(0,4,12)  # （0，4，12） 0-4 表示数字范围    12 表示元素的个数
y = np.cos(x**2/3+4)  #x**2表示x的平方
f1 = interp1d(x,y,kind = 'linear') #kind 表示种类：  linea 表示线性的   cubic 表示立方的
f2 = interp1d(x,y,kind = 'cubic')
xnew = np.linspace(0,4,30)
plt.plot(x,y,'o',xnew,f1(xnew),'-',xnew,f2(xnew),'--')  # xnew 表示插值之后的 x ， f(xnew) 表示插值之后的  y
plt.legend(['data','linear','cubic','nearest'],loc = 'best')  #loc 表示位置  # best 表示自适应
plt.show()