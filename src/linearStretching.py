'''
performing linear stretching by providing 
old min as oMin, old max as oMax,
new min as nMin and new max as nMax.

histogram stretching: (nMax-nMin)/(oMax-oMin)*i+nMin
'''


nMin = 0
nMax = 255
oMin = 0
oMax = 3

space = float(nMax-nMin)/float(oMax-oMin)
bins = oMax-oMin

for i in range(bins+1):
    print("{}:{}".format(i+oMin, int(nMin+(i*space))))
# for i -ends
