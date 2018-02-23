'''
given code finds histogram equalization
'''

import numpy as np

# input image
image = np.array([[6,6,6,10],[6,6,6,10],[17,17,17,17],[17,17,17,88]])

# finding frequency count for each value
uniques, count = np.unique(image, return_counts=True)
totalPixel = np.sum(count)
print ("Total pixel = {}".format(totalPixel))

#finding bins
bins = max(uniques)- min(uniques)

#finding hi and fi
hiArr = np.asarray((uniques, count)).T
print(hiArr)
fiList = []
fi = 0
for freq in hiArr:
    fi = fi + freq[1]
    fiList.append([freq[0], fi])
# for freq -ends
print(fiList)

print ("bins = {}".format(bins))

#calculating histogram
histVal = []
for index, fi in enumerate(fiList):
    if index ==0:
        tempNum = float(fi[1]*(bins))/float(2*totalPixel)
    else:
        tempNum = float((fi[1]+fiList[index-1][1])*(bins))/float(2*totalPixel)
    # if index -ends
    floorPix = np.floor(tempNum)
    print("floorPix = {}".format(tempNum))
    if floorPix>bins:
        histVal.append([fi[0], floorPix-1])
    else:
        histVal.append([fi[0], floorPix])
    # if floorPix -ends
# for index, fi -ends

print(histVal)

