import cv2
import numpy as np
img=cv2.imread('/Users/lannistarker/Desktop/unnamed.jpg')
width=234
height=328
pts=np.float32([[300,99],[481,233],[85,345],[277,496]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts,pts2)
print (type(matrix))
imgresolved=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("hello",imgresolved)
cv2.waitKey(0)

