# -*- coding: utf-8 -*-

import pandas as pd

rcsv = pd.read_csv("../data/001.csv")
print(rcsv)

# headerが1行、1列目をindexに指定
rcsv = pd.read_csv("../data/001.csv", header=0, index_col=0)
print(rcsv)

# ヘッダーが無い場合は自分で指定もできる
rcsv = pd.read_csv("../data/001.csv", names=['zero', 'one'])
print(rcsv)

# 10行飛ばして読み込み
rcsv = pd.read_csv("../data/001.csv", skiprows=10, names=['a', 'b'])
print(rcsv)

# 10行最後を飛ばす。一部サポートされないのであまり使わない？
rcsv = pd.read_csv("../data/001.csv", skipfooter=10)
print(rcsv)

# 1列目（0オリジン）だけ使う
rcsv = pd.read_csv("../data/001.csv", usecols=[1])
print(rcsv)
