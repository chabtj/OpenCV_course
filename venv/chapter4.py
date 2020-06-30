import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)

img[:]=255,0,0

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)#last paramter is thickness and the second last is teh color
cv2.rectangle(img,(0,0),(250,250),(0,0,255),3,cv2.FILLED)
cv2.circle(img,(250,250),125,(0,0,255),3)
cv2.putText(img,"OPENCV",(250,250),cv2.FONT_ITALIC,1,(0,0,255),3)
cv2.imshow("hello",img)

cv2.waitKey(0)