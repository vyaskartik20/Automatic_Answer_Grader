import numpy as np
import cv2
from matplotlib import pyplot as plt
import os


mypath='path\\images'
onlyfiles = [ f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath,f)) ]
images = np.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
   images[n] = cv2.imread( os.path.join(mypath,onlyfiles[n]) )

   gwash = images[n] #import image

   gwashBW = cv2.cvtColor(gwash, cv2.COLOR_RGB2GRAY) #change to grayscale

   height = np.size(gwash, 0)
   width = np.size(gwash, 1)

   ret,thresh1 = cv2.threshold(gwashBW ,41,255,cv2.THRESH_BINARY)


   kernel = np.ones((1,1),np.uint8)

   erosion = cv2.erode(thresh1, kernel,iterations = 31)
   opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
   closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

   _,contours, hierarchy = cv2.findContours(closing,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

   areas = [] #list to hold all areas

  for i,contour in enumerate(contours):
      ar = cv2.contourArea(contour)
      areas.append(ar)
      cnt = contour
      (x, y, w, h) = cv2.boundingRect(cnt)
       if cv2.contourArea(cnt) > 60000 and cv2.contourArea(cnt) < (height*width):
          if hierarchy[0,i,3] == -1:
             cv2.rectangle(gwash, (x,y), (x+w,y+h), (255, 0, 0), 12)


  plt.subplot2grid((2,5),(0,n)),plt.imshow(gwash)
  plt.title('Extraction'), plt.xticks([]), plt.yticks([])


plt.show()
