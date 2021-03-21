import numpy as np
arr6 = np.array([[17,23],[39,53]])
# 保存到 outfile.npy文件中
np.save("outfile.npy",arr6)

# 加载npy文件
arr7 = np.load("outfile.npy")
print(arr7)
np.savetxt("out.txt",arr6)
# 加载txt文件
arr8 = np.loadtxt("out.txt")
print(arr8)