# -*- coding: utf-8 -*-

import numpy as np
from pandas import Series, DataFrame
from pandas import *
# from pylab import *
import matplotlib.pyplot as plt
from numpy.random import randn

# pandas.Seriesの単純なプロッティング
s = Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
s.plot()

# pandas.DataFrameの単純なプロッティング
# Series・DataFrameなどpandasの大半のオブジェクトはmatplotlibのplotを持っている
df = DataFrame(np.random.randn(10, 4).cumsum(0),
               columns=['A', 'B', 'C', 'D'],
               index=np.arange(0, 100, 10))
df.plot()

# シリーズを可視化する
#data = Series(np.random.randn(16), index=list('abcdefghijklmnop'))
# 縦の棒グラフ
#data.plot(kind='bar', ax=axes[0], color='k', alpha=0.7)
# 横の棒グラフ
#data.plot(kind='barh', ax=axes[1], color='r', alpha=0.6)

# 棒グラフ
r = randn(10, 4)
print(r)
df2 = DataFrame(r, columns=['a', 'b', 'c', 'd'])
df2.plot(kind='bar')

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

# plt.show(grid=False, alpha=0.8)

# df.plot(kind='barh', stacked=True, alpha=0.5)  # 積み上げ棒グラフにする (stacked オプション)

plt.show()
