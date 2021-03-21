import numpy as np
# 不同角度的正弦值
arr4 = np.array([0,45,90])
# 通过乘pi/180转化为弧度
print(np.sin(arr4*np.pi/180))