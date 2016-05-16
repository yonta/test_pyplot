# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties
prop = FontProperties(fname="c:/Windows/Fonts/VL-Gothic-Regular.ttf")

df = pd.read_csv("../data/001.csv", index_col=0)
print(df.head(10))

df.plot()
plt.savefig("image2.png")  # savefigはshowのあとにやると失敗して白紙になる
plt.show()
