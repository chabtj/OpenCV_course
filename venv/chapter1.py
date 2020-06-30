import cv2
'''img = cv2.imread("/Users/lannistarker/desktop/pic1.png")
cv2.imshow("first",img)
cv2.waitKey(0)
'''
'''vid1=cv2.VideoCapture("/Users/lannistarker/desktop/abc.mp4")
while True:
    success,frame=vid1.read()
    cv2.imshow( "two",frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
'''
vid = cv2.VideoCapture(0)
vid.set(3,640)
vid.set(4,480)
vid.set(10,100)
while True :
    success,frame=vid.read()
    cv2.imshow("two",frame)
    if ( cv2.waitKey(1) & 0xff==ord('q') ):
        break