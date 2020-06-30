import cv2
import numpy as np
img = cv2.imread('/Users/lannistarker/Desktop/shapes.png')
imggrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurimggrey=cv2.GaussianBlur(imggrey,(17,17),1)
imgcanny=cv2.Canny(imggrey,50,50)
cv2.imshow("mat",imgcanny)
imgcopy=img
def getcontours(img):
    countours,hierarchy =cv2.findContours(img,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    for i in countours:
        Area=cv2.contourArea(i)

        if ( Area>500 and Area<20000):
            cv2.drawContours(imgcopy,i,-1,(0,255,0),3)
            perimeter=cv2.arcLength(i,True)
            approx=cv2.approxPolyDP(i,0.01*perimeter,True)

            x,y,w,h=cv2.boundingRect(approx)
            cv2.rectangle(imgcopy,(x,y),(x+w,y+h),(255,0,0),3)

            objecttype=""
            if (len(approx)==3):
                objecttype="Triangle"
            elif( len(approx)==4):
                if (abs(w-h)<10):
                    objecttype="Square"
                else:
                    objecttype="Rectangle"
            else :
                objecttype="NONE"
            print(objecttype)
            cv2.putText(imgcopy,objecttype,
                        (x+w//2-15,y+h//2-15)
                        ,cv2.FONT_ITALIC,
                        0.7,(0,0,0),
                        3)





getcontours(imgcanny)

cv2.imshow("mat1",imgcopy)
cv2.waitKey(0)