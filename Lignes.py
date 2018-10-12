#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 09:41:03 2018

@author: QuentindSC
"""

#import matplotlib.pyplot as plt

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

l = 0
inc = 0
front = 5
Abs =[]

σ = 0
µ = 0

for y in range (1, height):
    inc += 1
    l += 1
    Abs.append(l)
    
    if (inc == front):
        inc = 0
        
        for x in range (1, width):
            p = img.getpixel((x, y))
            Temp.append(p[0])
        
        po = int(l/height*10000)/100
        print(po,"%")
        
        L.append(Temp)
        Temp = []
       
print("100 %")


for i in L[0]:
    µ += (L[0][i])/width
µ =int(µ)


for j in L[0]:
    σ += (pow(L[0][j] - µ, 2))/width

σ = int(sqrt(σ))
for k,e in enumerate(L[0]):
    if (e >= µ + σ):
        Ls.append(k)

print( "\nµ =", µ,"\nσ =", σ)  
#plt.grid(True)
#plt.plot(Abs, Ls)
#plt.show()