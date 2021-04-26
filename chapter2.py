import cv2
import numpy as np
kernel=np.zeros((5,5),np.uint8)
img = cv2.imread('/Users/lannistarker/Desktop/tree.jpg')
#greyimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("greyimage",greyimg)
blurimg=cv2.GaussianBlur(img,(17,17),0)#kernel size is given to be odd for symmetry
#cv2.imshow ("frame",blurimg)

imgcanny=cv2.Canny(img ,50,50)#edges are detected using cannny 
imgdilation=cv2.dilate(imgcanny,kernel,iterations=1)#image dilation
imgeroded=cv2.erode(imgdilation,kernel,iterations=1)
cv2.imshow("window",imgeroded)
cv2.waitKey(0)