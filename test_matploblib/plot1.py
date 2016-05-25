# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

# 日本語を使うため必要 in Linux、Windowsだと？
# fontprop = matplotlib.font_manager.FontProperties(
#     fname="/usr/share/fonts/truetype/fonts-japanese-gothic.ttf")

# 新規のウィンドウを描画
fig = plt.figure()

# サブプロットを追加
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

# 最後のsubplot指定部にプロットする
# plt.plot(ran, 'k--')

# randn: 1行50列のランダムに正規分布に沿った数の配列を生成する。分散1・平均0
#        ってことは、結果に(xN+M)すれば分散N倍・平均+Mできる
N = 10000
ran = randn(N)
# print(ran)

# cumsum: 累積和（配列をsumでfoldlした結果）を返す
rancum = ran.cumsum()
# print(ran)

# ax3.で描画先を指定
# 黒色 (k) の破線で描画する
ax3.plot(rancum, 'k--')

# ran = randn(100)
# ヒストグラム（縦軸が頻度、横軸が範囲の統計のための棒グラフ）を表示
# bins:横軸である範囲の数、alpha:透過度
ax1.hist(ran, bins=20, color='k', alpha=0.3)

# 0オリジンで30個の配列を返す。この例なら[0, ... , 29]
rg = np.arange(30)
# print(range)

ran = randn(30)
# print(ran)

# 散布図
# (x, y)の形式で2つの配列を指定して描画する
ax2.scatter(rg, rg + 3 * ran)

# subplots: サブプロットを一気に作成
# sharex,shareyでx軸y軸をそれぞれ共有許可設定にしている
newfig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(randn(500), bins=50, color='k', alpha=0.5)

# サブプロット間の空白を詰めてみる
# left～topはウィンドウの使用割合を決める
plt.subplots_adjust(left=None, bottom=None, right=None,
                    top=None, wspace=0, hspace=0)

# 実際にグラフウィンドウを表示し描画する
# 複数のFigureオブジェクトがあればそれぞれ別ウィンドウ
plt.show()

# 保存
plt.savefig('image.png')

# import os
# print(__file__)
# print(os.path.dirname(__file__))
# d = os.path.abspath(os.path.dirname(__file__))
# print(d)
# だめだめだめだめ
# plt.savefig(d + "/imgae1-2.png")
# plt.savefig('c:/msys64/home/image.png')
# plt.savefig(r'c:/msys64/home/kei/image.png')
# plt.savefig(r'c:\msys64\home\kei\image.png')
