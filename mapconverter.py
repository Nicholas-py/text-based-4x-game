import sys
print(sys.executable)
from time import sleep
from PIL import Image
from tifffile import tifffile
import numpy as np
print('Imports finished, running...')
stderr =sys.stderr
sys.stderr = open('log.txt','a+')

xres, yres = 300,300
asciidarkening =" `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"

def numformat(n):
    assert n >= 0
    if n == 0:
        return '0'
    string = ''
    newn = n
    while newn > 0:
        nprime = newn%1000
        if newn != n:
            string = ' '+string
        sval = str(nprime)
        if len(sval) < 3 and newn >= 1000:
            if len(sval) == 2:
                sval = '0'+sval
            elif len(sval) == 1:
                sval = "00"+sval

        string = sval + string
        newn = newn//1000
    return string

img2 = tifffile.TiffFile('tifs/wc2.1_30s_elev.tif')
img2 = img2.asarray()
height, width = (img2.shape)
xstart = int(14*width/30)
xend = int(20*width/30)
ystart = int(4*height/30)
yend = int(12*height/30)
string = ''
for i in range(ystart,yend,int((yend-ystart)/yres)):
    for j in range(xstart,xend, int((xend-xstart)/xres)):
        current =  img2[i,j]
        sadd = ''
        if current < -1000:
            sadd = ' '
        else:
            sadd = '1'
        string += sadd
    string += '\n'
    
print('europemap.txt complete')

file2 = open('maps/europemap.txt','w')
file2.write(string)
file2.close()

img2 = tifffile.TiffFile('tifs/wc2.1_30s_elev.tif')
img2 = img2.asarray()
height, width = (img2.shape)
xstart = int(14*width/30)
xend = int(20*width/30)
ystart = int(4*height/30)
yend = int(12*height/30)
string = ''
for i in range(ystart,yend,int((yend-ystart)/yres)):
    for j in range(xstart,xend, int((xend-xstart)/xres)):
        current =  img2[i,j]
        sadd = ''
        if current < -1000:
            sadd = ' '
        elif current < 10:
            sadd += '-'
        elif current < 100:
            sadd += '+'
        elif current < 800:
            sadd += 'z'
        elif current < 2000:
            sadd += 'w'
        elif current < 9000:
            sadd += '@'
        else:
            raise ValueError('whattttt')
        string += sadd
    string += '\n'
    
print('europemapelev.txt complete')

file2 = open('maps/europemapelev.txt','w')
file2.write(string)
file2.close()

for lol in range(1,13):
    img2 = tifffile.TiffFile('tifs/wc2.1_30s_tavg/wc2.1_30s_tavg_'+['0',''][lol >= 10]+str(lol)+'.tif')
    img2 = img2.asarray()
    xres, yres = 300,300
    xstart = int(14*width/30)
    xend = int(20*width/30)
    ystart = int(4*height/30)
    yend = int(12*height/30)
    string = ''
    for i in range(ystart,yend,int((yend-ystart)/yres)):
        for j in range(xstart,xend, int((xend-xstart)/xres)):
            current =  img2[i,j]
            sadd = ''
            if current < -100:
                sadd = ' '
            elif current < 0:
                sadd += '-'
            elif current < 10:
                sadd += '+'
            elif current < 20:
                sadd += 'z'
            elif current < 30:
                sadd += 'w'
            elif current < 9000:
                sadd += '@'
            else:
                raise ValueError('whattttt')
            string += sadd
        string += '\n'
        
    print('europemaptemp'+str(lol)+'.txt complete')

    file2 = open('maps/europemaptemp'+str(lol)+'.txt','w')
    file2.write(string)
    file2.close()

for lol in range(1,13):
    img2 = tifffile.TiffFile('tifs/wc2.1_30s_prec/wc2.1_30s_prec_'+['0',''][lol >= 10]+str(lol)+'.tif')
    img2 = img2.asarray()
    xres, yres = 300,300
    xstart = int(14*width/30)
    xend = int(20*width/30)
    ystart = int(4*height/30)
    yend = int(12*height/30)
    string = ''
    for i in range(ystart,yend,int((yend-ystart)/yres)):
        for j in range(xstart,xend, int((xend-xstart)/xres)):
            current =  img2[i,j]
            sadd = ''
            if current == -32768:
                sadd = ' '
            elif current < 20:
                sadd += '-'
            elif current < 60:
                sadd += '+'
            elif current < 120:
                sadd += 'z'
            elif current < 170:
                sadd += 'w'
            elif current < 9000:
                sadd += '@'
            else:
                raise ValueError('whattttt')
            string += sadd
        string += '\n'
        
    print('europemapprec'+str(lol)+'.txt','complete')

    file2 = open('maps/europemapprec'+str(lol)+'.txt','w')
    file2.write(string)
    file2.close()

sys.stderr = stderr