from IPython.core.interactiveshell import InteractiveShell
from IPython.display import display, HTML
InteractiveShell.ast_node_interactivity = "all"    # so that all lines printed
#from utils.sage_logic import *
import re
from math import *
import matplotlib.pyplot as plt
import numpy
from sympy import simplify
from sympy import solve
from sympy.abc import m,n,o,p,X,Y,Z

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

x = numpy.linspace(-10, 10, 1000)
def zeichnen (x,y):
    x = numpy.linspace(-10, 10, 1000)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='X-Achse', ylabel='Y-Achse')
    ax.grid(True, linestyle='-.')
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)

def groesserEins ():
    x = numpy.linspace(-10, 10, 1000)
    fig, ax = plt.subplots()
    ax.plot(x, x)
    ax.plot(x, x**2)
    ax.plot(x, x**3)
    ax.plot(x, x**4)
    ax.plot(x, x**5)
    ax.set(xlabel='X-Achse', ylabel='Y-Achse')
    ax.grid(True, linestyle='-.')
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)
    
def nullBisEins ():
    x = numpy.linspace(0, 10, 1000)
    fig, ax = plt.subplots()
    ax.plot(x, x)
    ax.plot(x, x**0.9)
    ax.plot(x, x**0.5)
    ax.plot(x, x**0.2)
    ax.plot(x, x**0)
    ax.set(xlabel='X-Achse', ylabel='Y-Achse')
    ax.grid(True, linestyle='-.')
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)

def kleinerNull ():
    x = numpy.linspace(-10, 10, 1000)
    fig, ax = plt.subplots()
    ax.plot(x, x**(-4))
    ax.plot(x, x**(-2))
    y = x**(-1)
    y2 = y.copy()
    y2[y > 10] = numpy.nan
    ax.plot(x, y2)
    y = x**(-3)
    y3 = y.copy()
    y3[y > 10] = numpy.nan
    ax.plot(x, y3)
    ax.set(xlabel='X-Achse', ylabel='Y-Achse')
    ax.grid(True, linestyle='-.')
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)

def exponential ():
    x = numpy.linspace(-200, 200, 1000)
    fig, ax = plt.subplots()
    ax.plot(x, x**2)
    ax.plot(x, 2**x)
    ax.set(xlabel='X-Achse', ylabel='Y-Achse')
    ax.grid(True, linestyle='-.')
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 500)
    
Berechnen_Sie_5_Prozent_Von_13 = 0.05*13
Berechnen_Sie_6_Prozent_Von_80 = 0.06*80
Berechnen_Sie_32_Prozent_Von_17 = 0.32*17
Preis_15_Euro_plus_Mehrwertsteuer = 15 * 1.19
Preis_1_Euro_plus_Mehrwertsteuer = 1 * 1.19
Preis_1000_Euro_plus_Mehrwertsteuer = 1000 * 1.19
Betrag_von_50_Euro_nach_3_Prozent_Abzahlung = 50 * 0.97
Betrag_von_50_Euro_nach_7_Prozent_Abzahlung = 50 * 0.93
Betrag_von_1000_Euro_nach_10_Prozent_Abzahlung = 1000 * 0.9
bei_50_Prozent_Wachstum = 7000 * 1.5
bei_100_Prozent_Wachstum = 7000 * 2
bei_200_Prozent_Wachstum = 7000 * 3
Durch_dies_teilen_entspricht_5_Prozent = 20
Durch_dies_teilen_entspricht_33_Prozent = 3
Durch_dies_teilen_entspricht_20_Prozent = 5
Durch_dies_teilen_entspricht_50_Prozent = 2
Durch_dies_teilen_entspricht_2_Prozent = 50
Nettogehalt = 3000 * 0.88
Bruttogehalt = 2600 / 0.88
Aktie_Nach_3_Jahren = 100 * 0.75 * 1.30 * 0.75 * 1.30 * 0.75 * 1.30
