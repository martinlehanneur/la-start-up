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
L = []
l = 0
inc = 0
front = 10
Temp =[]

for y in range (1, height):
    inc += 1
    l += 1
    if (inc == front):
        inc = 0
        for x in range (1, width):
            
            p = img.getpixel((x, y))
            Temp.append(p[0])
            L.append(Temp)
        
        po = int(l/height*10000)/100
        print(po,"%")
print(L)
        


#plt.grid(True)
#plt.plot(Temp, L)
#plt.show()