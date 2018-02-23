nMin = 0
nMax = 255
oMin = 0
oMax = 3

space = float(nMax-nMin)/float(oMax-oMin)
bins = oMax-oMin

for i in range(bins+1):
    print("{}:{}".format(i+oMin, int(nMin+(i*space))))
# for i -ends
