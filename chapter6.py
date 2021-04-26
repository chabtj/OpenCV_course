import cv2
import numpy as np
img=cv2.imread('/Users/lannistarker/Desktop/unnamed.jpg')
img1=np.hstack((img,img,img))
cv2.imshow("hor",img1)
cv2.waitKey(0)