'''
You are given a picture with 5 point at the following (x,y) coordinates:
(1,3), (2,1), (2,5), (3,3), (3,5)
Apply the Hough Transform algorithm to search for circles in the parametric representation
(x - x0)^2 + (y - y0)^2 = r^2:
Quantize r2 into three values: 2, 3, 4.
Quantize x0 into four values: -1, 1, 3, 5.
Quantize y0 into four values: -1, 1, 3, 5.
'''

import numpy as np

pointArr=np.array([(1,3),(2,1),(2,5),(3,3),(3,5)])
r2Arr = np.array([2,3,4])
x0Arr = np.array([-1,1,3,5])
y0Arr = np.array([-1,1,3,5])

spaceArr = np.zeros([4,4,3])
count = 0
for point in pointArr:
    x,y = point
    print ("point (x,y)=({},{})".format(x,y))
    for x0Index, x0 in enumerate(x0Arr):
        for y0Index, y0 in enumerate(y0Arr):
            r2 = np.square(x-x0)+np.square(y-y0)
            
            count+=1
            if r2>=2 and r2<=4:
                spaceArr[x0Index, y0Index, r2-2]+=1
                print("({}-{})^2+({}-{})^2 = {}".format(x, x0, y, y0, r2))
            #if r2 -ends
        #for y0 -ends
    #for x0 -ends
    print("")
#for point -ends
print ("r2 is computed {} times".format(count))
print("Printing space arr:")
for i in range(3):
    print(spaceArr[:,:,i])
