import math
from ROW import ROW
from COLS import COLS
from SYM import SYM
from NUM import NUM
from DATA import DATA

b4 = {}
for k, _ in globals().items():
    b4[k] = k

l, the, help = [], {}, """gate: guess, assess, try, expand
(c) 2023, Tim Menzies, BSD-2
Learn a little, guess a lot, try the strangest guess, learn a little more, repeat
USAGE:
  lua gate.lua [OPTIONS] 
OPTIONS:
  -c --cohen    small effect size               = .35
  -f --file     csv data file name              = ../data/diabetes.csv
  -h --help     show help                       = false
  -k --k        low class frequency kludge      = 1
  -m --m        low attribute frequency kludge  = 2
  -s --seed     random number seed              = 31210
  -t --todo     start up action                 = help"""

def isa(x, y):
    return type(y, (x,), {})

def is_(s):
    t = {'a': s}
    t.__index = t
    return t



