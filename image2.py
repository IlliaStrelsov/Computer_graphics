from PIL import Image, ImageDraw
from numpy import genfromtxt
import numpy as np

def rotate(A,B,C):
  return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])

def jarvisalgorithm(A):
  n = len(A)
  m = list(range(n))

  for i in range(1,n):
    if A[m[i]][0]<A[m[0]][0]:
        m[i]= m[0]
        m[0] = m[i]
  result = [m[0]]
  del (m[0])
  m.append(result[0])
  while True:
    k = 0
    for i in range(1,len(m)):
      if rotate(A[result[-1]],A[m[k]],A[m[i]])<0:
        k = i
    if m[k]==result[0]:
      break
    else:
      result.append(m[k])
      del m[k]
  return result

w = 960
h = 540
data = np.zeros((h,w,3), dtype=np.uint8)
l = np.zeros((h,w,3), dtype=np.uint8)
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
a.save('my2.png')

my_data.tolist()
x = jarvisalgorithm(my_data)




for i in range(len(x)-1):
   for j in range(len(x)-i-1):
        if x[j] > x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]


n = int(len(x))
help = np.zeros((n,2))


for i in range(len(x)):
    k = x[i]
    g1 = my_data[k][0]
    g2 = my_data[k][1]
    help[i][0] = g1
    help[i][1] = g2

help = help.astype(int)
help = help[np.argsort(help[:, 1])]



image  = Image.open('my2.png')
draw = ImageDraw.Draw(image)

for i in range(len(help)):
    if(i == 27 or (i-1) == 27):
        draw.line(((563,456),(382,456)),fill="BLUE")
    elif((help[i][0] == 243) and help[i][1] ==88):
        draw.line(((88, 243), (175, 451)), fill="BLUE")
    elif((help[i][0] == 78) and help[i][1] ==163):
        draw.line(((492, 80), (163, 78)), fill="BLUE")
    elif( help[i-1][0] == 78 and help[i-1][1] ==163):
        continue
    else:
        draw.line(((help[i-1][1],help[i-1][0]),(help[i][1],help[i][0])),fill="BLUE")

draw.line(((492,80),(654,81)),fill="BLUE")
image.show()
image.save('my4.png')





