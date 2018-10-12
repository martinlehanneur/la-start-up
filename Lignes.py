#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 09:41:03 2018

@author: QuentindSC
"""

#import matplotlib.pyplot as plt

from PIL import Image

path = "../la-start-up/transfo.png" # Image path
img = Image.open(path)
width, height = img.size
newimg = Image.new("RGB", (width, height), "white")
Ls = []
L = []
Temp =[]
Temps = []
l = 0
inc = 0
front = 5
Abs =[]

for y in range (1, height):
    inc += 1
    l += 1
    Abs.append(l)
    if (inc == front):
        inc = 0
        
        for x in range (1, width):
            p = img.getpixel((x, y))
            Temp.append(p[0])
            L.append(Temp)
           
        po = int(l/height*10000)/100
        print(po,"%")
       
print("100 %")

µ = 0
for i in L[0]:
    µ += L[0][i]/width


σ = 0
for j in L[0]:
    σ += (pow(L[0][j] - µ, 2))/width

for k in L[0]:
    if (L[0][k] >= µ):
        Ls.append(L[0][k])

print(µ)
#plt.grid(True)
#plt.plot(Abs, Ls)
#plt.show()