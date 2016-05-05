# -*- coding: utf-8 -*-
import numpy as np
from pandas import *
from pylab import *
import matplotlib.pyplot as plt
from matplotlib import font_manager
from numpy.random import randn

prop = matplotlib.font_manager.FontProperties(
    fname="/usr/share/fonts/truetype/fonts-japanese-gothic.ttf")

r = randn(30).cumsum()

# 色、線種、マーカーを指定する
# 黒、破線、マーカーは o
plt.plot(r, color='k', linestyle='dashed', marker='o')

plt.show()
plt.savefig("image.png")
