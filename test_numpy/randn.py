# -*- coding: utf-8 -*-
from numpy.random import randn

n = 10000
ran = randn(n)
ave = ran.sum() / n
print(ave)
var = ran.var()
print(var)


import numpy.random
print(numpy.random.randn(10))

from numpy.random import randn
print(randn(10))
