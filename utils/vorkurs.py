from IPython.core.interactiveshell import InteractiveShell
from IPython.display import display, HTML
InteractiveShell.ast_node_interactivity = "all"    # so that all lines printed
#from utils.sage_logic import *
import re
from math import *

TODO = ""

def fs (a):
    return frozenset(a) 
def CartProd (a,b):
    return {(x,y) for x in a for y in b}
from itertools import combinations
def PowerSet(iterable):
    s = list(iterable)
    res = set()
    for r in range(len(s)+1):
        temp = combinations(s,r)
        for x in temp:
            res.add(fs(x))
    return res


########## solutions

def pruefe (exercise,myList):
    solutions = {"t_34_1": {x for x in range(0,51) if x % 2 == 0}, 
                "t_34_2": {x*y for x in range(0,6) for y in range(0,6) if x % 2 == 0  and y % 2 == 1},
                "t_34_3": {x for x in range(0,51) if x % 2 == 0} | {"Text",fs({1,2})}}

    if exercise == "tutorial 3.4":
        print ("gerade:", myList[0] == solutions["t_34_1"])
        print ("produkte:", myList[1] == solutions["t_34_2"])
        print ("vielfalt:", myList[2] == solutions["t_34_3"])


