import cv2
# import os
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
# ./test13/Cropped

def registration():
	for i in range(1, 7):
		# if((i!=2)and(i!=4)and(i!=6)and(i!=9)):
			# Open the image files.
			#im = cv2.imread("data_sets/test_" + str(i) + ".jpg")
			# if((i!=4)and(i!=9)and(i!=11)):
			im = cv2.imread("RUN/test15/Cropped" + str(i) + "/1.png")
			# imwr

			#im = cv2.imread('result_edited/result_edited_1.jpg')
			#cv2.imshow('image',im)
			#cv2.waitKey(0)
			#cv2.destroyAllWindows()

			row, col = im.shape[:2]
			bottom = im[row-2:row, 0:col]
			mean = cv2.mean(bottom)[0]


			bordersize = 50
			img1_color = cv2.copyMakeBorder(
				im,
				top=bordersize,
				bottom=bordersize,
				left=bordersize,
				right=bordersize,
				borderType=cv2.BORDER_CONSTANT,
				value=[mean, mean, mean]
			)

			#img1_color = cv2.imread("data_sets/real_test_" + str(i) + ".jpg")  # Image to be aligned.
			#img2_color = cv2.imread("data_sets/example.jpg")


			img2_color = cv2.imread("RUN/answer/answerkey/1.png")    # Reference image.
			# img3_color = cv2.imread("RUN/answer/blank/1.png")


			# cv2.imshow('image',img1_color)
			# cv2.waitKey(0)
			# cv2.destroyAllWindows()

			#extra
			# row,col=img2_color.shape[:2]
			# bottom=img2_color[row-2:row,0:col]
			# mean=cv2.mean(bottom)[0]
			# bordersize=300
			# img_2=cv2.copyMakeBorder(
			#     img2_color,
			#     top=bordersize,
			#     bottom=bordersize,
			#     left=bordersize,
			#     right=bordersize,
			#     borderType=cv2.BORDER_CONSTANT,
			#     value=[mean,mean,mean]
			# )
			# cv2.imshow('image',img_2)
			# cv2.waitKey(0)
			# cv2.destroyAllWindows()

			# Convert to grayscale.

			img1 = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY)
			img2 = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY)
			height, width = img2.shape




			# Create ORB detector with 5000 features.

			orb_detector = cv2.ORB_create(5000)

			# Find keypoints and descriptors.
			# The first arg is the image, second arg is the mask
			#  (which is not reqiured in this case).

			kp1, d1 = orb_detector.detectAndCompute(img1, None)
			kp2, d2 = orb_detector.detectAndCompute(img2, None)

			# Match features between the two images.
			# We create a Brute Force matcher with
			# Hamming distance as measurement mode.

			matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

			# Match the two sets of descriptors.

			matches = matcher.match(d1, d2)

			# Sort matches on the basis of their Hamming distance.

			matches.sort(key = lambda x: x.distance)
			#extra
			# img3 = cv2.drawMatches(img1_color,kp1,img2_color,kp2,matches[:10],None,flags=2)
			# plt.imshow(img3),plt.show()
			# Take the top 90 % matches forward.
			matches = matches[:int(len(matches)*90)]
			no_of_matches = len(matches)

			# Define empty matrices of shape no_of_matches * 2.
			p1 = np.zeros((no_of_matches, 2))
			p2 = np.zeros((no_of_matches, 2))
			#
			for j in range(len(matches)):
				p1[j, :] = kp1[matches[j].queryIdx].pt
				p2[j, :] = kp2[matches[j].trainIdx].pt

			# Find the homography matrix.
			homography, mask = cv2.findHomography(p1, p2, cv2.RANSAC)

			# Use this matrix to transform the
			# colored image wrt the reference image.
			transformed_img = cv2.warpPerspective(img1_color, homography, (width, height))


			# Save the output.
			#cv2.imwrite('outputad/output_' + str(i) + '.jpg', transformed_img)
			# cv2.imwrite('outputads/output_' + str(i) + '.png',transformed_img)
		#image registration done

			#img2 = cv2.imread("data_sets/example.jpg")
			img2 = cv2.imread("RUN/answer/answerkey/1.png")
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




			cv2.imwrite("RUN/result/resultt" + str(i) + "/result0"+".png", dilation3)

























			img2_color = cv2.imread("RUN/answer/blank/1.png")    # Reference image.
			# img3_color = cv2.imread("RUN/answer/blank/1.png")


			# cv2.imshow('image',img1_color)
			# cv2.waitKey(0)
			# cv2.destroyAllWindows()

			#extra
			# row,col=img2_color.shape[:2]
			# bottom=img2_color[row-2:row,0:col]
			# mean=cv2.mean(bottom)[0]
			# bordersize=300
			# img_2=cv2.copyMakeBorder(
			#     img2_color,
			#     top=bordersize,
			#     bottom=bordersize,
			#     left=bordersize,
			#     right=bordersize,
			#     borderType=cv2.BORDER_CONSTANT,
			#     value=[mean,mean,mean]
			# )
			# cv2.imshow('image',img_2)
			# cv2.waitKey(0)
			# cv2.destroyAllWindows()

			# Convert to grayscale.

			img1 = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY)
			img2 = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY)
			height, width = img2.shape




			# Create ORB detector with 5000 features.

			orb_detector = cv2.ORB_create(5000)

			# Find keypoints and descriptors.
			# The first arg is the image, second arg is the mask
			#  (which is not reqiured in this case).

			kp1, d1 = orb_detector.detectAndCompute(img1, None)
			kp2, d2 = orb_detector.detectAndCompute(img2, None)

			# Match features between the two images.
			# We create a Brute Force matcher with
			# Hamming distance as measurement mode.

			matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

			# Match the two sets of descriptors.

			matches = matcher.match(d1, d2)

			# Sort matches on the basis of their Hamming distance.

			matches.sort(key = lambda x: x.distance)
			#extra
			# img3 = cv2.drawMatches(img1_color,kp1,img2_color,kp2,matches[:10],None,flags=2)
			# plt.imshow(img3),plt.show()
			# Take the top 90 % matches forward.
			matches = matches[:int(len(matches)*90)]
			no_of_matches = len(matches)

			# Define empty matrices of shape no_of_matches * 2.
			p1 = np.zeros((no_of_matches, 2))
			p2 = np.zeros((no_of_matches, 2))
			#
			for j in range(len(matches)):
				p1[j, :] = kp1[matches[j].queryIdx].pt
				p2[j, :] = kp2[matches[j].trainIdx].pt

			# Find the homography matrix.
			homography, mask = cv2.findHomography(p1, p2, cv2.RANSAC)

			# Use this matrix to transform the
			# colored image wrt the reference image.
			transformed_img = cv2.warpPerspective(img1_color, homography, (width, height))


			# Save the output.
			#cv2.imwrite('outputad/output_' + str(i) + '.jpg', transformed_img)
			# cv2.imwrite('outputads/output_' + str(i) + '.png',transformed_img)
		#image registration done

			#img2 = cv2.imread("data_sets/example.jpg")
			img2 = cv2.imread("RUN/answer/blank/1.png")
			img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
			#img1 = cv2.imread("outputad/output_" + str(i) + ".jpg")
			img1 = cv2.cvtColor(transformed_img,cv2.COLOR_BGR2GRAY)




			kernel = np.ones((2,2), np.uint8)
			thresh1 = cv2.erode(img1,kernel,iterations=2)
			thresh1 = cv2.dilate(thresh1,kernel,iterations=2)
			ret,thresh1 = cv2.threshold(thresh1,127,255,cv2.THRESH_BINARY_INV)
			# cv2.imwrite("resultad/thresh1_" + str(i) + ".jpg", thresh1)

			thresh2 = cv2.erode(img2,kernel,iterations=2)
			thresh2 = cv2.dilate(thresh2,kernel,iterations=2)
			ret,thresh2 = cv2.threshold(thresh2,127,255,cv2.THRESH_BINARY_INV)
			# cv2.imwrite("resultad/thresh2_" + str(i) + ".jpg", thresh2)



			img3 = cv2.absdiff(thresh1, thresh2)
			kernel3 = np.ones((5,5),np.uint8)
			erosion3 = cv2.erode(img3,kernel3,iterations = 2)
			dilation3 = cv2.dilate(erosion3,kernel3,iterations = 1)

			# dirname="resultt"
			# os.mkdir(dirname)
			#cv2.imwrite("resultt/resultttt_" + str(i) + ".jpg", dilation3)




			cv2.imwrite("RUN/result/resultt" + str(i) + "/result1"+".png", dilation3)
