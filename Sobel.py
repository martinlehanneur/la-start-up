from PIL import Image
from math import sqrt
import numpy as np
from scipy.ndimage import convolve

path = "../la-start-up/tuile4.png" # Image path
img = Image.open(path)
width, height = img.size
newimg = Image.new("RGB", (width, height), "white")
sobel_x = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
sobel_y = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
l = 0
for x in range(1, width-1):  # ignore the edge pixels
    for y in range(1, height-1): # ignore edge pixels
        G = [[0,0,0],[0,0,0], [0,0,0]]
        # top left pixel
        p = img.getpixel((x-1, y-1))
        r = p[0]
        g = p[1]
        b = p[2]
        var=r + g + b
        #var=int(var)
        # intensity ranges from 0 to 765 (255 * 3)
        G[0][0] =int(var)/3



        # remaining left column
        p = img.getpixel((x-1, y))
        r = p[0]
        g = p[1]
        b = p[2]
        var=r + g + b
        G[0][1] =int(var)/3

        p = img.getpixel((x-1, y+1))
        r = p[0]
        g = p[1]
        b = p[2]
        var=r + g + b
        G[0][2] =int(var)/3

        # middle pixels
        p = img.getpixel((x, y-1))
        r = p[0]
        g = p[1]
        b = p[2]
        var=r + g + b

        G[1][0] =int(var)/3

        p = img.getpixel((x, y+1))
        r = p[0]
        g = p[1]
        b = p[2]
        var=r + g + b

        G[1][2] =int(var)/3

        # right column
        p = img.getpixel((x+1, y-1))
        r = p[0]
        g = p[1]
        b = p[2]
        var=r + g + b

        G[2][0] =int(var)/3

        p = img.getpixel((x+1, y))
        r = p[0]
        g = p[1]
        b = p[2]
        var=r + g + b


        G[2][1] =int(var)/3

        p = img.getpixel((x+1, y+1))
        r = p[0]
        g = p[1]
        b = p[2]
        var=r + g + b

        G[2][2] =int(var)/3

        # calculate the length of the gradient (Pythagorean theorem)
      

        Gx = np.sum(convolve(sobel_x, G))
        Gy = np.sum(convolve(sobel_y, G))
        grad = sqrt(pow(Gx, 2)+pow(Gy, 2))/8
        #print(grad)
        # normalise the length of gradient to the range 0 to 255
        grad = int(grad)

        # draw the length in the edge image
        newimg.putpixel((x,y),(grad, grad, grad))
    l = l + 1
    po = l*10000/width
    po = float(po)/float(100)
    print po,"%"
        
newimg.show()
newimg.save("../la-start-up/transfo.png")
