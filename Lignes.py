#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 09:41:03 2018

@author: QuentindSC
"""

import matplotlib.pyplot as plt

from PIL import Image
from math import sqrt
import numpy as np

path = "../la-start-up/transfo.png" # Image path
img = Image.open(path)
width, height = img.size
newimg = Image.new("RGB", (width, height), "white")

Ls = []
L = []
Temp =[]
Temps = []

np.array(L)
np.array(Ls)

inc = 0
front = 2


Abs = []
Moy = []
Var = []

l = 0
n = 0
s = 0
m = 0


for y in range (1, height):
    inc += 1
    
    if (inc == front):
        Abs.append(n)
        n += 1
        inc = 0
        
        for x in range (1, width):
            p = img.getpixel((x, y))
            Temp.append(p[0])
        L.append(Temp)
        Temp = []
    l += 1
    po = l*10000/height
    po =float(po)/float(100)
    print po,"%"
       

       
print "100 %"
l = 0

for y in range (1, n): 
    inc += 1
    if (inc == front):
        inc = 0
        for i in L[y]:
            m += L[y][i]
        m = m/width
        Moy.append(m);
        
        for i in L[y]:
            s += (pow(L[y][i] - m, 2))
        s = s/width
        Var.append(int(s));
        s = sqrt(s)
        
        for i,I in enumerate(L[y]):
            if (I >= m + 2*s):
                Temps.append(i)
        
        Ls.append(Temps)
        Temps = []
    l += 1
    po = l*10000/n
    po =float(po)/float(100)
print "\nMoyennes :", Moy,"\nVariances :", Var  
plt.grid(True)
plt.plot(Ls[1]) #Affichage de l ligne voulue, ici la première.

plt.show()