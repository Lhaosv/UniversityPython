import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 箱型图
df = pd.DataFrame(np.random.rand(10,5),columns=['A','B','C','D','E'])
df.plot.box()
plt.show()