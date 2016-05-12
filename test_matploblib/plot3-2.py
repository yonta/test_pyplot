# -*- coding: utf-8 -*-

import numpy as np
from pandas import Series, DataFrame
from pandas import *
# from pylab import *
import matplotlib.pyplot as plt
from numpy.random import randn

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

plt.show()
