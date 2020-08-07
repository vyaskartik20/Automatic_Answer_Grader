import numpy as np
import cv2
import math


img = cv2.imread('1.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.blur(gray,(20,20))

bi = cv2.bilateralFilter(gray, 5, 75, 75)
cv2.imshow('bi',bi)

dst = cv2.cornerHarris(bi, 2, 3, 0.04)
#--- create a black image to see where those corners occur ---
mask = np.zeros_like(gray)

#--- applying a threshold and turning those pixels above the threshold to white ---
mask[dst>0.01*dst.max()] = 255
# cv2.imshow('mask', mask)
cv2.imwrite('mask.png',mask)

img[dst > 0.01 * dst.max()] = [0, 0, 255]   #--- [0, 0, 255] --> Red ---
# cv2.imshow('dst', img)
cv2.imwrite('dst.png',img)

coordinates = np.argwhere(mask)

# print(coordinates)

coor_list = [l.tolist() for l in list(coordinates)]

coor_tuples = [tuple(l) for l in coor_list]

thresh = 5

def distance(pt1, pt2):
    (x1, y1), (x2, y2) = pt1, pt2
    dist = math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
    return dist

coor_tuples_copy = coor_tuples

i = 1
for pt1 in coor_tuples:

    # print(' I :', i)
    for pt2 in coor_tuples[i::1]:
        # print(pt1, pt2)
        # print('Distance :', distance(pt1, pt2))
        if(distance(pt1, pt2) < thresh):
            coor_tuples_copy.remove(pt2)
        i+=1


img2 = img.copy()
for pt in coor_tuples:
    cv2.circle(img2, tuple(reversed(pt)), 3, (0, 0, 255), -1)
cv2.imwrite('Image_with_4_corners.png', img2)
