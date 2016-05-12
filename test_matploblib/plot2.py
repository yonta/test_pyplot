# -*- coding: utf-8 -*-
import numpy as np
# from pandas import *
# from pylab import *
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from numpy.random import randn

prop = FontProperties(fname="c:/Windows/Fonts/VL-Gothic-Regular.ttf")

r = randn(30).cumsum()

# 色、線種、マーカーを指定する
# 黒、破線、マーカーは o（ドット）
plt.plot(r, color='k', linestyle='dashed', marker='o')

# RGB 値を明示
plt.plot(r, color='#ff0000', linestyle='dashed', marker='o', label='dashed')

# drawstyle を変更
plt.plot(r, color='#0000ff', drawstyle='steps-post', label='steps-post')

# 凡例を付ける
plt.legend(loc='best')

# 引数を与えずに現在値を確認する
print(plt.xlim())
# => (0.0, 30.0)
print(plt.xticks())
# => (array([  0.,   5.,  10.,  15.,  20.,  25.,  30.]), <a list of 7 Text xticklabel objects>)

# 新しい値を設定する
plt.xlim([0, 40])
# xtics未指定時はxlimに対して適当な数値が選ばれるようだ、5とか10とか
plt.xticks([0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40])
# xticksのほうがxlimよりも優先
plt.xticks(np.arange(11) * 5)

print(plt.ylim())
# => (-4.0, 3.0)
print(plt.yticks())
# => (array([-4., -3., -2., -1.,  0.,  1.,  2.,  3.]), <a list of 8 Text yticklabel objects>)

plt.ylim([-10, 10])
plt.yticks([-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])

#---------------------------------------------------------------------

# 新規画面
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.set_xticks([0, 250, 500, 750, 1000])

# x軸ラベルの回転・サイズ指定
# サイズはxx-small, x-small, small, midium, large, x- xx-..., などがあり、
# 数値でも1を100％とした割合で指定できる
ax.set_xticklabels(['A', 'B', 'C', 'D', 'E'], rotation=30, fontsize='xx-large')

# 日本語を使う場合はfontpropertiesを指定する
# 標準フォントは日本語非対応のため文字化けしてしまう
ax.set_title('テストの matplotlib plot です', fontproperties=prop)
ax.set_xlabel('ランク', fontproperties=prop)

r = randn(1000).cumsum()
ax.plot(r)

#---------------------------------------------------------------------

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


def randn1000():
    return randn(1000).cumsum()

# 凡例ラベルを指定してプロット
ax.plot(randn1000(), 'k', label='one')
ax.plot(randn1000(), 'b--', label='two')
ax.plot(randn1000(), 'r.', label='three')
ax.plot(randn1000(), 'g+', label='four')
ax.plot(randn1000(), 'b*', label='five')

plt.ylim([-100, 100])

# 凡例を表示
ax.legend(loc='best')

plt.show()
plt.savefig("image2.png")
