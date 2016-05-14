# -*- coding: utf-8 -*-

# DataFrameの操作について、すっげー参考になるURL
#   http://sinhrks.hatenablog.com/entry/2014/11/15/230705

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

df = pd.read_csv('../data/data_trigger.csv',
                 # 先頭列をindexに使用するので、index指定は無し
                 header=1,  # 2行切り捨て
                 names=['time', 'value1', 'value2', 'trigger1', 'trigger2'])
# print(df)
# print(df.info())

xt = np.arange(0, 15.1, 1)
df.plot(label='value1',
        ax=ax1, x=['time'], y=['value1'], kind='scatter',
        color='#ff7700', xlim=(0, 15), xticks=xt, grid=True)
df.plot(label='value2',
        ax=ax1, x=['time'], y=['value2'], kind='scatter',
        color='b', xlim=(0, 15), xticks=xt, grid=True)

yt = np.arange(0, 4.1, 1)
df.plot(ax=ax2, x=['time'], y=['trigger1'],
        kind='line', linewidth=2,
        color='r', xticks=xt, ylim=(-1, 5), yticks=yt, grid=True)
df.plot(ax=ax2, x=['time'], y=['trigger2'],
        kind='line', linewidth=2,
        color='g', xticks=xt, ylim=(-1, 5), yticks=yt, grid=True)

plt.show()

# テスト用DataFrame
# df = pd.DataFrame([[0.5, 0.1, 0],
#                    [1.0, 0.4, 1]],
#                   columns=['time', 'value1', 'trigger1'])
# print(df)

# DataFrameから列をセレクトすると、1次元配列となり型はSeries
#   df : DataFrame
#   df['trigger1'] : Series

# 以下は列の選択で同意
# 特定行を取出すときはaxis=0(default)、特定列を取り出すときはaxis=1
# 3、4、…と次元が上がれば、axisも増えていく
#   df.xs('trigger1', axis=1)
#   df.ix[:, 'trigger1']
#   df['trigger1']

# 以下は行の選択で同意
#   df.xs(0)
#   df.ix[0,:]
#   df.ix[0]

# 以下の2つは同意だが、DataFrameが帰るのを明示する前者のほうが良いと思う
#   df.ix[[True, False], :]
#   df.ix[[True, False]]

# 以下は同意。map/lambda式を組み合せた場合はより複雑な式が表現できる。
#   df[df['trigger1'] == 1]
#   df[df['trigger1'].map(lambda x: x == 1)]
#   df.ix[df['trigger1'].map(lambda x: x == 1)]
#   df.ix[df['trigger1'].map(lambda x: x == 1), :]

# 複数条件は簡単なものなら以下の前者ように省略もできる
#   df[(df['trigger1'] == 1) & (df['trigger2'] == 0)]
#   df.ix[df['trigger1'] == 1, :].ix[df['trigger2'] == 0, :]

# applyを使うと、各行ごとの要素同士を計算することもできる。
# axis=0で各列ごとに、axis=1で各行ごとに計算する。
# この例では、各行のvalue1*value2を行ったSeriesを作成する。
#   df.apply(lambda x: x['value1'] * x['value2'], axis=1)

# minやmaxは全体の最小・最大値の値そのものを返す。
# idxminやidxmaxは全体の最小・最大値のindexを返す。

# 基本方針:
#   各条件に一致する行をSeriesで取り出し、最後にDataFrameにappendする。
#   timeだけ抜き出せば良いが、valueも統計で使うはずなので取っておく。

x0 = df[(df['trigger1'] == 1)].iloc[0, :]
# 最小値を取るだけなら下記のようになる。今回はDataFrameで返すことにする。
#   x1 = df[(df['trigger1'] == 1) & (df['trigger2'] == 0)].ix[:, 'value2'].min()
# 長くなると、どこで改行をするか難しい
x1 = df.ix[
    df[(df['trigger1'] == 1) & (df['trigger2'] == 0)].ix[
        :, 'value2'].idxmin(axis=0), :]
x2 = df.ix[
    df[(df['trigger1'] == 4) & (df['trigger2'] == 0)].ix[
        :, 'value1'].idxmin(axis=0)]
x3 = df[(df['trigger2'] == 2)].iloc[0, :]

x = pd.DataFrame(columns=['time', 'value1', 'value2', 'trigger1', 'trigger2'])
x = x.append([x0, x1, x2, x3], ignore_index=True)

print(x)
