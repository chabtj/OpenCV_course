import cv2
img=cv2.imread('/Users/lannistarker/Desktop/tree.jpg')
cv2.imshow("hello",cv2.resize(img,(1000,1000)))

img1=img[0:200,300:500]#height comed first and then the width
cv2.imshow("hello",img1)
cv2.waitKey(0)