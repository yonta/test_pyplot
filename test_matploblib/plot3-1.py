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

plt.show()
