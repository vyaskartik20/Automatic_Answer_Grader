import cv2
import numpy as np
from matplotlib import pyplot as plt
# Open the image files.
img1_color = cv2.imread("img_4.jpeg") # Image to be aligned.
img2_color = cv2.imread("img_3.jpeg") # Reference image.

# Convert to grayscale.
img1 = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY)
height, width = img2.shape
# print(img1)
# print(len(img1))
# print(len(img1[0]))
# print(len(img2))
# print(len(img2[0]))
# # Create ORB detector with 5000 features.
# orb_detector = cv2.ORB_create(5000)
#
# # Find keypoints and descriptors.
# # The first arg is the image, second arg is the mask
# # (which is not reqiured in this case).
# kp1, d1 = orb_detector.detectAndCompute(img1, None)
# kp2, d2 = orb_detector.detectAndCompute(img2, None)
# print(d1)
# print(len(d1))
# print(len(d1[0]))
# print(d1[0])
# print(len(kp1))
# print(kp1[0])
# print(d2)
# print(len(d2))
# print(len(d2[0]))
# print(len(kp2))
# # Match features between the two images.
# # We create a Brute Force matcher with
# # Hamming distance as measurement mode.
# matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
#
# # Match the two sets of descriptors.
# matches = matcher.match(d1, d2)
# #print(matches)
# print(len(matches))
# print(matches[0])
# # Sort matches on the basis of their Hamming distance.
# matches.sort(key = lambda x: x.distance)
#
# # Take the top 90 % matches forward.
# matches = matches[:int(len(matches)*90)]
# no_of_matches = len(matches)
# print(no_of_matches)
# img3 = cv2.drawMatches(img1_color,kp1,img2_color,kp2,matches[:10],None,flags=2)
# plt.imshow(img3),plt.show()
# # Define empty matrices of shape no_of_matches * 2.
# p1 = np.zeros((no_of_matches, 2))
# p2 = np.zeros((no_of_matches, 2))
# print(p1)
# for i in range(len(matches)):
#     p1[i, :] = kp1[matches[i].queryIdx].pt
#     p2[i, :] = kp2[matches[i].trainIdx].pt
# print(p1)
# print(len(p1))
# print(len(p1[0]))
# print(p1[0])
# print(p2[0])
# p1=p1.astype(int)
# img3=cv2.drawKeypoints(img1_color,kp1,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# cv2.imshow("keypoints",img3)
# cv2.waitKey(0)
p1=[[14,1161],[658,1159],[653,14],[12,13]]
p2=[[14,1211],[684,1209],[679,13],[12,13]]
# j=0
# for i in p1:
#     #x,y=i.ravel()
#     cv2.circle(img1_color,(p1[j][0],p1[j][1]),3,255,-1)
#     j=j+1
# cv2.imshow("keypoints",img1_color)
# cv2.waitKey(0)

# Find the homography matrix.
homography, mask = cv2.findHomography(np.float32(p1), np.float32(p2), cv2.RANSAC)
print(homography)
print(len(mask[0]))
# Use this matrix to transform the
# colored image wrt the reference image.
transformed_img = cv2.warpPerspective(img1_color,
					homography, (width, height))
#print(len(transformed_img))
#print(len(transformed_img[0]))
# Save the output.
cv2.imwrite('output.jpeg', transformed_img)

img2 = cv2.imread("img_3.jpeg")
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#img1 = cv2.imread("outputad/output_" + str(i) + ".jpg")
img1 = cv2.cvtColor(transformed_img,cv2.COLOR_BGR2GRAY)




kernel = np.ones((2,2), np.uint8)
thresh1 = cv2.erode(img1,kernel,iterations=2)
thresh1 = cv2.dilate(thresh1,kernel,iterations=2)
ret,thresh1 = cv2.threshold(thresh1,127,255,cv2.THRESH_BINARY_INV)
#cv2.imwrite("resultad/thresh1_" + str(i) + ".jpg", thresh1)

thresh2 = cv2.erode(img2,kernel,iterations=2)
thresh2 = cv2.dilate(thresh2,kernel,iterations=2)
ret,thresh2 = cv2.threshold(thresh2,127,255,cv2.THRESH_BINARY_INV)
#cv2.imwrite("resultad/thresh2_" + str(i) + ".jpg", thresh2)



img3 = cv2.absdiff(thresh1, thresh2)
kernel3 = np.ones((5,5),np.uint8)
erosion3 = cv2.erode(img3,kernel3,iterations = 2)
dilation3 = cv2.dilate(erosion3,kernel3,iterations = 1)

# dirname="resultt"
# os.mkdir(dirname)
#cv2.imwrite("resultt/resultttt_" + str(i) + ".jpg", dilation3)




cv2.imwrite("diff.jpeg", dilation3)
