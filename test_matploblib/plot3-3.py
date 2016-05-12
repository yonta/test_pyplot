# -*- coding: utf-8 -*-

import numpy as np
from pandas import Series, DataFrame
from pandas import *
# from pylab import *
import matplotlib.pyplot as plt
from numpy.random import randn

fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)

# データフレームを可視化する
df = DataFrame(np.random.randn(6, 4),
               index=['1', '2', '3', '4', '5', '6'],
               columns=Index(['A', 'B', 'C', 'D'], name='Genus'))
print(df)
# =>
# Genus         A         B         C         D
# 1     -0.350817 -0.017378 -0.991230 -0.223608
# 2      0.478712 -0.472764  0.677484 -0.852312
# 3      1.402219  0.381440  0.370080  0.682125
# 4     -1.733590  0.296124 -0.014841  1.140705
# 5      0.373399  1.150718  1.341984  1.040759
# 6     -0.013301 -0.202793 -1.367493 -0.572954
df.plot()
plt.show()

# 棒グラフ
df.plot(kind='bar')
plt.show()

# 積み上げ式棒グラフ
df.plot(kind='bar', stacked=True)
plt.show()

# 正のみのランダム
df_positive = DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
print(df)

# 積み上げエリアグラフ
df_positive.plot.area(stacked=True)
plt.show()

# エリアグラフ
df_positive.plot.area(stacked=False)
plt.show()

# df.plot(kind='barh', stacked=True, alpha=0.5)  # 積み上げ棒グラフにする (stacked オプション)
