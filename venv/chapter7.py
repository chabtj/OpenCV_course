import cv2
import numpy as np
def empty (a):
    pass
img=cv2.imread('/Users/lannistarker/Desktop/unnamed.jpg')
imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.namedWindow("trackbar")
cv2.resizeWindow("trackbar",640,240)
cv2.createTrackbar("Hmin","trackbar",0,179,empty)
cv2.createTrackbar("Hmax","trackbar",179,179,empty)
cv2.createTrackbar("Smin","trackbar",0,255,empty)
cv2.createTrackbar("Smax","trackbar",255,255,empty)
cv2.createTrackbar("Vmin","trackbar",0,255,empty)
cv2.createTrackbar("Vmax","trackbar",255,255,empty)

while True:
    Hmin=cv2.getTrackbarPos("Hmin","trackbar")
    Hmax=cv2.getTrackbarPos("Hmax","trackbar")
    Smin=cv2.getTrackbarPos("Smin","trackbar")
    Smax=cv2.getTrackbarPos("Smax","trackbar")
    Vmin=cv2.getTrackbarPos("Vmin","trackbar")
    Vmax=cv2.getTrackbarPos("Vmax","trackbar")
    min=np.array([Hmin,Smin,Vmin])
    max=np.array([Hmax,Smax,Vmax])
    mask=cv2.inRange(imgHSV,min,max)
    imgfinal=cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("pic",mask)
    cv2.imshow("pic,",imgfinal)
    cv2.waitKey(1)

