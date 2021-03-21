import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 折线图
df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('2019/2/27',periods=10),columns=list('ABCD'))  #periods 表示周期
df.plot()
plt.show()