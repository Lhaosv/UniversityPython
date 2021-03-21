import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 条形图
df = pd.DataFrame(np.random.randn(10,4),columns=['A','B','C','D'])  #periods 表示周期
df.plot.bar()
plt.show()