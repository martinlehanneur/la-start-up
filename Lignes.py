import matplotlib.pyplot as plt

from PIL import Image
from math import sqrt
import numpy as np

path = "../la-start-up/transfo.png" # Image path
img = Image.open(path)
width, height = img.size
newimg = Image.new("RGB", (width, height), "white")

LZ = []
LI = []
L = []
Temp =[]
TempI = []
TempZ = []

np.array(L)


inc = 0
front = 4 #permet de prendre une ligne toute les front lignes


Ave = []
Ave2 = []
Stdev = []
Stdev2 = []


l = 0
n = 0
s = 0
s2 = 0
a = 0
a2 = 0

for y in range (1, height - 1):

    inc += 1
    
    if (inc == front):
        n += 1
        inc = 0
        
        for x in range (1, width - 1):
            p = img.getpixel((x, y))
            Temp.append(p[0])
        L.append(Temp)
        Temp = []
        
    l += 1
    po = l*10000/height
    po =float(po)/float(100)
    print po,"%"
       

       
print "100 % *******************************************************************************************************"
l = 0
        
for y in range (0, n - 1):      
    for i in L[y]:
        a += i
    a = float(int(float(a)/float(width)*100)/float(100))
    Ave.append(a);
        
    for i in L[y]:
        s += pow(i - a, 2)
    s = float(int(sqrt(float(s)/float(width))*100)/float(100))
    Stdev.append(s)
     
    for i in range(0, width - 2):
        if (L[y][i] >= a + 2*s):
            TempI.append(L[y][i])
                
        else:
            TempI.append(0)
                
    LI.append(TempI)
    TempI = []   
    
    l += 1
    po = l*10000/n
    po =float(po)/float(100)
    print po,"%"
    
print "100 % *******************************************************************************************************"
l = 0

def autocorr(rank):
    z = 0
    Z = []
    for tau in range (0, len(L[rank]) - 1):
        for i in range(tau, len(L[rank]) - 1):
            z += (L[rank][i] - Ave[rank])*(L[rank][i - tau] - Ave[rank])
        Z.append(z)
        z = 0
    return Z; 

Z = autocorr(160) 
   
for i in Z:
    a2 += i
a2 = float(int(float(a2)/float(width)*100)/float(100))
Ave2.append(a2);
        
for i in Z:
    s2 += pow(i - a2, 2)
s2 = float(int(sqrt(float(s2)/float(width))*100)/float(100))
Stdev2.append(s2)
     
    
for i in Z:
    if (i >= a2 + s2):
        TempZ.append(i)
                
    else:
        TempZ.append(0)
                
    LZ.append(TempZ)
    TempZ = []     
    
    l += 1
    po = l*10000/len(Z)
    po =float(po)/float(100)
    print po,"%"
    
print "100 % *******************************************************************************************************"
    
print "\n    AVERAGES :", Ave,"\n    STANDARD DEVIATIONS :", Stdev  

plt.figure(1)

plt.subplot(211)
plt.grid(True)

plt.plot(L[160], '^')#Affichage de la ligne voulue.
plt.plot(LI[160], '*')#Affichage en superposition des pics d'Intensity
plt.xlabel('Sample')
plt.ylabel('Intensity') 

plt.subplot(212)
plt.grid(True)
plt.plot(Z, '+')
plt.plot(LZ, '*')
plt.xlabel('Sample')
plt.ylabel('Correlation') 

plt.show(True)

