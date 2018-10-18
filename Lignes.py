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

inc = 0
front = 2
Abs =[]

n = 0
s = 0
m = 0

for y in range (1, height):
    inc += 1
    
    if (inc == front):
        n += 1
        inc = 0
        
        for x in range (1, width):
            p = img.getpixel((x, y))
            Temp.append(p[0])
        
#        po = int(l/height*10000)/100
#        print(po,"%")
        
        L.append(Temp)
        Temp = []
       
#print("100 %")

for y in range (1, n): 
    inc += 1
    if (inc == front):
        inc = 0
        for i in L[y]:
            m += L[y][i]
        m = m/width
        
        for i in L[y]:
            s += (pow(L[y][i] - m, 2))
        s = sqrt(s/width)
    
        for i,v in enumerate(L[y]):
            if (v >= m + 2*s):
                Temps.append(i)
        
        Ls.append(Temps)
        Temps = []
#    po = int(l/height*10000)/100
#    print po,"%"
print "\nmoyenne :", m,"\nécart-type :", s  
#plt.grid(True)
#plt.plot(Abs, Ls)
#plt.show()