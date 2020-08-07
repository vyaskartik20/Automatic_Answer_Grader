import cv2
import numpy as np

image = cv2.imread('1.png')
# blur = cv2.blur(1,(5,5))
blurImg = cv2.blur(image,(10,10))
gray = cv2.cvtColor(blurImg, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 120, 255, 1)

corners = cv2.goodFeaturesToTrack(canny,4,0.85,200)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(image,(x,y),5,(36,255,12),-1)

# cv2.imshow('canny', canny)
# cv2.imshow('image', image)
cv2.imwrite('12.png',image)
cv2.waitKey()
