import numpy as np
from scipy import linalg
A = np.array([[1,2],[3,4]])
res2 = linalg.det(A)  # 求解行列式
print("行列式的的解是：\n",res2)
u,v = linalg.eig(A)
print("特征值：\n",u,"特征向量：\n",v)  #求解特征值和特征向量
