from numpy import genfromtxt
import numpy as np
from PIL import Image
w = 960
h = 540
data = np.zeros((h,w,3), dtype=np.uint8)

my_data = genfromtxt('DS8.txt',dtype='int')
print(my_data.shape)

for x in range(540):
    for y in range(960):
        data[x][y] = [255,255,255]
for y in range(42817):
    for x in range(2):
        if(x==0):
            x1 = my_data[y][x]
        elif(x == 1):
            y1 = my_data[y][x]
    data[x1][y1] = [0,0,0]

a = Image.fromarray(data,'RGB')
a.save('my1.png')
a.show()








