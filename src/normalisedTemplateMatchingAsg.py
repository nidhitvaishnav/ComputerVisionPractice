import numpy as np

#2*2 template and 2*2 image window
template = np.array([[1,2],[4,3]])
img1 = np.array([[1,2],[7,3]])
img2 = np.array([[2,2],[2,2]])
img3 = np.array([[8,9],[11,10]])
img4 = np.array([[11,20],[40,30]])
img5 = np.array([[100,100],[100,100]])

img = img3

#c = lambda(template) cross-correlation with f(image)
c = np.zeros((2,2))

c[0][0] = template[0][0]*img[0][0] + template[0][1]*img[0][1]\
                +template[1][0]*img[1][0] + template[1][1]*img[1][1]
c[0][1] = template[0][0]*img[0][1] + template[1][0]*img[1][1]
c[1][0] = template[0][0]*img[1][0] + template[0][1]*img[1][1]
c[1][1] = template[0][0]*img[1][1]

print("c = lambda cross correlation f:\n{}".format(c))

#finding f2 bt making squere of each image pixel value
f2 = np.zeros((2,2))
for i in range(2):
    for j in range(2):
        f2[i][j]=img[i][j]*img[i][j]
    #for j -ends
#for i -ends

print("\nf2: \n{}".format(f2))

#making lamba1(template) 1 on each values
lambda1 = np.array([[1,1],[1,1]])
 
 #n2 = lambda1 cross-correlation with f2
n2 = np.zeros((2,2))
n2[0][0] = lambda1[0][0]*f2[0][0] + lambda1[0][1]*f2[0][1]\
                +lambda1[1][0]*f2[1][0] + lambda1[1][1]*f2[1][1]
n2[0][1] = lambda1[0][0]*f2[0][1] + lambda1[1][0]*f2[1][1]
n2[1][0] = lambda1[0][0]*f2[1][0] + lambda1[0][1]*f2[1][1]
n2[1][1] = lambda1[0][0]*f2[1][1]


print("\nn2:\n{}".format(n2))

#finding q
#q = c[i][j]/sqrt(n2[i][j])
q = np.zeros((2,2))
for i in range(2):
    for j in range(2):
        q[i][j] = float(c[i][j])/float(np.sqrt(n2[i][j]))
    #for j -ends
#for i -ends

print("\nq:\n{}".format(q))    
    
