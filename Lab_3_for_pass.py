from pyDatalog import pyDatalog

import random
pyDatalog.create_terms('X, Z, Y, Sm, div, Average, y, SumRand')
(y[X] == sum_(Y, for_each=Y)) <= ((Y._in(range_(X+1))))
print(y[0] == Sm)
(div[X, Y] == Z) <= (X // Y == Z)
print(div[y[0], 0] == Average)
