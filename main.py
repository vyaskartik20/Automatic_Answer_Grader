import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
from PIL import Image
# from transform_example import transfer
from pyimagesearch.transform import four_point_transform
from connected_component import components
from image_regg import registration
#
# for j in range(1,68):
#     os.rmdir("cropped/rollno"+str(j))
# os.rmdir("cropped")

# def sort_contours(cnts, method="left-to-right"):
#     # initialize the reverse flag and sort index
#     reverse = False
#     i = 0
#
#     # handle if we need to sort in reverse
#     if method == "right-to-left" or method == "bottom-to-top":
#         reverse = True
#
#     # handle if we are sorting against the y-coordinate rather than
#     # the x-coordinate of the bounding box
#     if method == "top-to-bottom" or method == "bottom-to-top":
#         i = 1
#
#     # construct the list of bounding boxes and sort them from top to
#     # bottom
#     boundingBoxes = [cv2.boundingRect(c) for c in cnts]
#     (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
#                                         key=lambda b: b[1][i], reverse=reverse))
#
#     # return the list of sorted contours and bounding boxes
#     return (cnts, boundingBoxes)
#
# def box_extraction(img_for_box_extraction_path, cropped_dir_path):
#
#     img = cv2.imread(img_for_box_extraction_path, 0)  # Read the image
#     img2 = cv2.imread(img_for_box_extraction_path, 0)
#     img3 = cv2.imread(img_for_box_extraction_path, 0)
#     font = cv2.FONT_HERSHEY_COMPLEX
#     # img = cv2.blur(img,(10,10))
#     (thresh, img_bin) = cv2.threshold(img, 128, 255,
#                                       cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # Thresholding the image
#     img_bin = 255-img_bin  # Invert the image
#
#     # img = np.full((100,80,3), 12, np.uint8)
#
#
#     # threshold image
#     # ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
#                     # 127, 255, cv2.THRESH_BINARY)
#     img = cv2.blur(img,(20,20))
#
#     cv2.imwrite("Methodology/Image_bin.jpg",img_bin)
#
#     # Defining a kernel length
#     kernel_length = np.array(img).shape[1]//400
#
#     # A verticle kernel of (1 X kernel_length), which will detect all the verticle lines from the image.
#     verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
#     # A horizontal kernel of (kernel_length X 1), which will help to detect all the horizontal line from the image.
#     hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
#     # A kernel of (3 X 3) ones.
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
#
#     # Morphological operation to detect verticle lines from an image
#     img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=3)
#     verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=3)
#     cv2.imwrite("Methodology/verticle_lines.jpg",verticle_lines_img)
#
#     # Morphological operation to detect horizontal lines from an image
#     img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=3)
#     horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=3)
#     cv2.imwrite("Methodology/horizontal_lines.jpg",horizontal_lines_img)
#
#     # Weighting parameters, this will decide the quantity of an image to be added to make a new image.
#     alpha = 0.50
#     beta = 1.0 - alpha
#     # This function helps to add two image with specific weight parameter to get a third image as summation of two image.
#     img_final_bin = cv2.addWeighted(verticle_lines_img, alpha, horizontal_lines_img, beta, 0.0)
#     img_final_bin = cv2.erode(~img_final_bin, kernel, iterations=2)
#     (thresh, img_final_bin) = cv2.threshold(img_final_bin, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#
#     # For Debugging
#     # Enable this line to see verticle and horizontal lines in the image which is used to find boxes
#     cv2.imwrite("Methodology/img_final_bin.jpg",img_final_bin)
#     # Find contours for image, which will detect all the boxes
#     contours, hierarchy = cv2.findContours(
#         img_final_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#     # print(len(contours))
#     # Sort all the contours by top to bottom.
#     (contours, boundingBoxes) = sort_contours(contours, method="left-to-right")
#
#     x1=-100
#     y1=0
#     # check=0
#     idx = 0
#     for c in contours:
#         # if check!=3:
#             # Returns the location and width,height for every contour
#             x, y, w, h = cv2.boundingRect(c)
#             # check+=1
#
#
#
#             # if ((x==x1)):
#             if (w > 400 and h > 600):
#             # if(cv2.contourArea(c)>50):
#                  if ((x>(x1+100))): #outer
#                 #if ((x<(x1+50))): #inner
#                     idx += 1
#
#                     # rect = cv2.minAreaRect(c)
#                     # box = cv2.boxPoints(rect)
#                     #
#                     # box = np.int0(box)
#                     # # draw a red 'nghien' rectangle
#                     # cv2.drawContours(img, [box], 0, (0, 0, 255))
#                     # cv2.imwrite("contour1.png", img)
#                     # # finally, get the min enclosing circle
#
#
#                     # hull = cv.c(points[, hull[, clockwise[, returnPoints]]
#                     # hull = cv2.convexHull(c)
#                     # print(hull)
#
#
#
#                     itr=0
#
#                     approx = cv2.approxPolyDP(c, 0.009 * cv2.arcLength(c, True), True)
#
# # draws boundary of contours.
#                     cv2.drawContours(img3, [approx], 0, (0, 0, 255), 5)
#
#                     # Used to flatted the array containing
#                     # the co-ordinates of the vertices.
#                     nq = approx.ravel()
#                     iq = 0
#
#                     for jq in nq :
#                         if(iq % 2 == 0):
#                             xq = nq[iq]
#                             yq = nq[iq + 1]
#
#                     # String containing the co-ordinates.
#                             string = str(xq) + " " + str(yq)
#
#                     #if(i == 0):
#                     # text on topmost co-ordinate.
#                     # cv2.putText(img2, "Arrow tip", (x, y),
#                     # font, 0.5, (255, 0, 0))
#                     #else:
#                     # text on remaining co-ordinates.
#                             cv2.putText(img3, string, (xq, yq),
#                             font, 0.5, (255, 255, 0))
#
#                             if(itr==1):
#                                 # xq=xq-16
#                                 # yq=yq-16
#                                 extTop="(%s, %s)" %(xq, yq)
#                             if(itr==2):
#                                 # xq=xq+16
#                                 # yq=yq-16
#                                 extRight="(%s, %s)" %(xq, yq)
#                             if(itr==3):
#                                 # xq=xq+16
#                                 # yq=yq+16
#                                 extBot="(%s, %s)" %(xq, yq)
#                             if(itr==0):
#                                 # xq=xq-16
#                                 # yq=yq+16
#                                 extLeft="(%s, %s)" %(xq, yq)
#
#                             itr = itr + 1
#
#                             # print(xq, yq)
#                         iq = iq + 1
#
#                     # Showing the final image.
#
#                     # cv2.imwrite('image2.png', img3)
#
#                     coords="[%s, %s, %s, %s]" %(extTop,extRight,extBot,extLeft)
#
#
#                     # extLeft = tuple(c[c[:, :, 0].argmin()][0])
#                     # extRight = tuple(c[c[:, :, 0].argmax()][0])
#                     # extTop = tuple(c[c[:, :, 1].argmin()][0])
#                     # extBot = tuple(c[c[:, :, 1].argmax()][0])
#
#                     # hull = []
#                     #
#                     # # calculate points for each contour
#                     #
#                     # hull.append(cv2.convexHull(c, False))
#                     #
#                     # # create an empty black image
#                     # drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
#                     #
#                     # # draw contours and hull points
#                     #
#                     # color_contours = (0, 255, 0) # color for contours
#                     # color = (255, 255, 255) # color for convex hull
#                     # # draw contours
#                     # cv2.drawContours(drawing, contours, i, color_contours, 2, 8, hierarchy)
#                     # # draw convex hull
#                     # cv2.drawContours(drawing, hull, i, color, 2, 8)
#
#
#                     # extTop="(%s, %s)" %(box[1][0],box[1][1])
#                     # extRight="(%s, %s)" %(box[2][0],box[2][1])
#                     # extBot="(%s, %s)" %(box[3][0],box[3][1])
#                     # extLeft="(%s, %s)" %(box[0][0],box[0][1])
#
#                     # extTop="(%s, %s)" %(box[1][0],box[1][1])
#                     # extRight="(%s, %s)" %(box[2][0],box[2][1])
#                     # extBot="(%s, %s)" %(box[3][0],box[3][1])
#                     # extLeft="(%s, %s)" %(box[0][0],box[0][1])
#
#
#                     #coords="[%s, %s, %s, %s]" %(extTop,extRight,extBot,extLeft)
#
#                     # print(coords)
#
#                     pts = np.array(eval(coords), dtype = "float32")
#
#
#                     new_img = four_point_transform(img2,pts)
#                     cv2.imwrite(cropped_dir_path+str(idx) + '.png', new_img)
#                     # print(x)
#
#
#
#                     # box = np.int0(box)
#                     # # draw a red 'nghien' rectangle
#                     # cv2.drawContours(img, [box], 0, (0, 0, 255))
#                     # cv2.imwrite("contour1.png", img)
#                     # coords="[(189.96536, 1084.9089), (822.29297, 1050.0603), (990.5377, 2167.3167), (328.2101, 2246.1653)]"
#                     # [(189.96536, 1084.9089), (852.29297, 1006.0603), (990.5377, 2167.3167), (328.2101, 2246.1653)]
#                 #x1=x #inner
#             # print(x)
#                 # y1=y
#                     x1=x  #outer
#                     # y1=y
#
#                     # print(coords)
#
#                     # img1 = cv2.imread(img_for_box_extraction_path, 0)  # Read the image
#                     # cv2.drawContours(img1,c, -1, (0, 255, 255), 2)
#                     # cv2.circle(img1, (189,1084) , 8, (0, 0, 255), -1)
#                     # cv2.circle(img1, (852,1006) , 8, (0, 255, 0), -1)
#                     # cv2.circle(img1, (990,2167) , 8, (255, 0, 0), -1)
#                     # cv2.circle(img1, (328,2246) , 8, (255, 255, 0), -1)
#                     # cv2.imwrite('new.png', img1)
#
#
#                     # if((extLeft[1])>(extBot[1])):
#                     #     coords="[%s, %s, %s, %s]" %(extLeft,extTop,extRight,extBot)
#                     #
#                     # else:
#                     #     coords="[%s, %s, %s, %s]" %(extTop,extRight,extBot,extLeft)
#
#                     # print (extLeft)
#                     # print ("    ")
#                     # print(extRight)
#                     # print ("    ")
#                     # print (extTop)
#                     # print ("    ")
#                     # print(extBot)
#                     # print ("\n")
#
#                     # box = cv2.boxPoints(c)
#
#                     # coords=(str1+ (extLeft) + str3 + (extTop)+ str3 +(extRight)+ str3 + (extBot)+str2)
#
#
#                     # print(coords)
#
#                     # print (x1)
#                     # print ("    ")
#                     # print(w)
#                     # print ("\n")
#                     # print (h)
#                     # print ("\n")
#
#
#
#
#             # If the box height is greater then 20, widht is >80, then only save it as a box in "cropped/" folder.
#             # if (w > 40 and h > 60) and (w<1000) and (h > 1.5*w):
#
#
#     # For Debugging
#     # Enable this line to see all contours.
#     # cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
#     # cv2.imwrite("./Temp/img_contour.jpg", img)
#
#     #
# def registration():
#     for k in range(1,68):
#         if k!=26 and k!=48:
#                 # if((i!=2)and(i!=4)and(i!=6)and(i!=9)):
#     			# Open the image files.
#     			#im = cv2.imread("data_sets/test_" + str(i) + ".jpg")
#     			# if((i!=4)and(i!=9)and(i!=11)):
#                 img1_color = cv2.imread("cropped/rollno"+str(k) + "/" +str(1)+ ".png")
#     			# imwr
#
#     			#im = cv2.imread('result_edited/result_edited_1.jpg')
#     			#cv2.imshow('image',im)
#     			#cv2.waitKey(0)
#     			#cv2.destroyAllWindows()
#
#     			# row, col = im.shape[:2]
#     			# bottom = im[row-2:row, 0:col]
#     			# mean = cv2.mean(bottom)[0]
#                 #
#                 #
#     			# bordersize = 50
#     			# img1_color = cv2.copyMakeBorder(
#     			# 	im,
#     			# 	top=bordersize,
#     			# 	bottom=bordersize,
#     			# 	left=bordersize,
#     			# 	right=bordersize,
#     			# 	borderType=cv2.BORDER_CONSTANT,
#     			# 	value=[mean, mean, mean]
#     			# )
#
#     			#img1_color = cv2.imread("data_sets/real_test_" + str(i) + ".jpg")  # Image to be aligned.
#     			#img2_color = cv2.imread("data_sets/example.jpg")
#
#
#                 img2_color = cv2.imread("cropped/rollno3/"+str(1)+".png")    # Reference image.
#     			# img3_color = cv2.imread("RUN/answer/blank/1.png")
#
#
#     			# cv2.imshow('image',img1_color)
#     			# cv2.waitKey(0)
#     			# cv2.destroyAllWindows()
#
#     			#extra
#     			# row,col=img2_color.shape[:2]
#     			# bottom=img2_color[row-2:row,0:col]
#     			# mean=cv2.mean(bottom)[0]
#     			# bordersize=300
#     			# img_2=cv2.copyMakeBorder(
#     			#     img2_color,
#     			#     top=bordersize,
#     			#     bottom=bordersize,
#     			#     left=bordersize,
#     			#     right=bordersize,
#     			#     borderType=cv2.BORDER_CONSTANT,
#     			#     value=[mean,mean,mean]
#     			# )
#     			# cv2.imshow('image',img_2)
#     			# cv2.waitKey(0)
#     			# cv2.destroyAllWindows()
#
#     			# Convert to grayscale.
#                 p1 = np.zeros((4, 2))
#                 p2 = np.zeros((4, 2))
#
#                 img1 = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY)
#                 contours, _= cv2.findContours(img1, cv2.RETR_TREE,
#                                    cv2.CHAIN_APPROX_SIMPLE)
#                 for cnt in contours :
#
#                                        approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
#
#                                        # draws boundary of contours.
#                                        # cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5)
#
#                                        # Used to flatted the array containing
#                                        # the co-ordinates of the vertices.
#                                        n = approx.ravel()
#                                        i = 0
#
#                                        for j in n :
#                                            if(i % 2 == 0):
#                                                p1[i][0] = n[i]
#                                                p1[i][1] = n[i + 1]
#
#                                                # String containing the co-ordinates.
#                                                # string = str(x) + " " + str(y)
#                                                #
#                                                # if(i == 0):
#                                                #     # text on topmost co-ordinate.
#                                                #     cv2.putText(img2, "Arrow tip", (x, y),
#                                                #     font, 0.5, (255, 0, 0))
#                                                # else:
#                                                #     # text on remaining co-ordinates.
#                                                #     cv2.putText(img2, string, (x, y),
#                                                #     font, 0.5, (0, 255, 0))
#                                                i = i + 1
#
#         		img2 = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY)
#     			height, width = img2.shape
#
#                 contours, _= cv2.findContours(img2, cv2.RETR_TREE,
#                                    cv2.CHAIN_APPROX_SIMPLE)
#                 for cnt in contours :
#
#                                        approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
#
#                                        # draws boundary of contours.
#                                        # cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5)
#
#                                        # Used to flatted the array containing
#                                        # the co-ordinates of the vertices.
#                                        n = approx.ravel()
#                                        i = 0
#
#                                        for j in n :
#                                            if(i % 2 == 0):
#                                                p2[i][0] = n[i]
#                                                p2[i][1] = n[i + 1]
#
#                                                # String containing the co-ordinates.
#                                                # string = str(x) + " " + str(y)
#                                                #
#                                                # if(i == 0):
#                                                #     # text on topmost co-ordinate.
#                                                #     cv2.putText(img2, "Arrow tip", (x, y),
#                                                #     font, 0.5, (255, 0, 0))
#                                                # else:
#                                                #     # text on remaining co-ordinates.
#                                                #     cv2.putText(img2, string, (x, y),
#                                                #     font, 0.5, (0, 255, 0))
#                                                    i = i + 1
#
#
#
#
#
#
#     			# Create ORB detector with 5000 features.
#
#     			# orb_detector = cv2.ORB_create(5000)
#                 #
#     			# # Find keypoints and descriptors.
#     			# # The first arg is the image, second arg is the mask
#     			# #  (which is not reqiured in this case).
#                 #
#     			# kp1, d1 = orb_detector.detectAndCompute(img1, None)
#     			# kp2, d2 = orb_detector.detectAndCompute(img2, None)
#                 #
#     			# # Match features between the two images.
#     			# # We create a Brute Force matcher with
#     			# # Hamming distance as measurement mode.
#                 #
#     			# matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
#                 #
#     			# # Match the two sets of descriptors.
#                 #
#     			# matches = matcher.match(d1, d2)
#                 #
#     			# # Sort matches on the basis of their Hamming distance.
#                 #
#     			# matches.sort(key = lambda x: x.distance)
#     			# #extra
#     			# # img3 = cv2.drawMatches(img1_color,kp1,img2_color,kp2,matches[:10],None,flags=2)
#     			# # plt.imshow(img3),plt.show()
#     			# # Take the top 90 % matches forward.
#     			# matches = matches[:int(len(matches)*90)]
#     			# no_of_matches = len(matches)
#                 #
#     			# # Define empty matrices of shape no_of_matches * 2.
#     			# p1 = np.zeros((no_of_matches, 2))
#     			# p2 = np.zeros((no_of_matches, 2))
#     			# #
#     			# for j in range(len(matches)):
#     			# 	p1[j, :] = kp1[matches[j].queryIdx].pt
#     			# 	p2[j, :] = kp2[matches[j].trainIdx].pt
#
#     			# Find the homography matrix.
#     			homography, mask = cv2.findHomography(p1, p2, cv2.RANSAC)
#
#     			# Use this matrix to transform the
#     			# colored image wrt the reference image.
#     			transformed_img = cv2.warpPerspective(img1_color, homography, (width, height))
#
#
#     			# Save the output.
#     			#cv2.imwrite('outputad/output_' + str(i) + '.jpg', transformed_img)
#     			# cv2.imwrite('outputads/output_' + str(i) + '.png',transformed_img)
#     		#image registration done
#
#     			#img2 = cv2.imread("data_sets/example.jpg")
#     			img2 = cv2.imread("cropped/rollno3/"+str(1)+".png")
#     			img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#     			#img1 = cv2.imread("outputad/output_" + str(i) + ".jpg")
#     			img1 = cv2.cvtColor(transformed_img,cv2.COLOR_BGR2GRAY)
#
#
#
#
#     			kernel = np.ones((2,2), np.uint8)
#     			thresh1 = cv2.erode(img1,kernel,iterations=2)
#     			thresh1 = cv2.dilate(thresh1,kernel,iterations=2)
#     			ret,thresh1 = cv2.threshold(thresh1,127,255,cv2.THRESH_BINARY_INV)
#     			#cv2.imwrite("resultad/thresh1_" + str(i) + ".jpg", thresh1)
#
#     			thresh2 = cv2.erode(img2,kernel,iterations=2)
#     			thresh2 = cv2.dilate(thresh2,kernel,iterations=2)
#     			ret,thresh2 = cv2.threshold(thresh2,127,255,cv2.THRESH_BINARY_INV)
#     			#cv2.imwrite("resultad/thresh2_" + str(i) + ".jpg", thresh2)
#
#
#
#     			img3 = cv2.absdiff(thresh1, thresh2)
#     			kernel3 = np.ones((5,5),np.uint8)
#     			erosion3 = cv2.erode(img3,kernel3,iterations = 2)
#     			dilation3 = cv2.dilate(erosion3,kernel3,iterations = 1)
#
#     			# dirname="resultt"
#     			# os.mkdir(dirname)
#     			#cv2.imwrite("resultt/resultttt_" + str(i) + ".jpg", dilation3)
#
#
#
#
#     			cv2.imwrite("registered/rollno"+str(k)+"/"+str(1)+".png", dilation3)
#
#                 img1_color = cv2.imread("cropped/rollno"+str(k) + "/" +str(2) ".png")
#     			# imwr
#
#     			#im = cv2.imread('result_edited/result_edited_1.jpg')
#     			#cv2.imshow('image',im)
#     			#cv2.waitKey(0)
#     			#cv2.destroyAllWindows()
#
#     			# row, col = im.shape[:2]
#     			# bottom = im[row-2:row, 0:col]
#     			# mean = cv2.mean(bottom)[0]
#                 #
#                 #
#     			# bordersize = 50
#     			# img1_color = cv2.copyMakeBorder(
#     			# 	im,
#     			# 	top=bordersize,
#     			# 	bottom=bordersize,
#     			# 	left=bordersize,
#     			# 	right=bordersize,
#     			# 	borderType=cv2.BORDER_CONSTANT,
#     			# 	value=[mean, mean, mean]
#     			# )
#
#     			#img1_color = cv2.imread("data_sets/real_test_" + str(i) + ".jpg")  # Image to be aligned.
#     			#img2_color = cv2.imread("data_sets/example.jpg")
#
#
#     			img2_color = cv2.imread("cropped/rollno3/"+str(2)+".png")    # Reference image.
#     			# img3_color = cv2.imread("RUN/answer/blank/1.png")
#
#
#     			# cv2.imshow('image',img1_color)
#     			# cv2.waitKey(0)
#     			# cv2.destroyAllWindows()
#
#     			#extra
#     			# row,col=img2_color.shape[:2]
#     			# bottom=img2_color[row-2:row,0:col]
#     			# mean=cv2.mean(bottom)[0]
#     			# bordersize=300
#     			# img_2=cv2.copyMakeBorder(
#     			#     img2_color,
#     			#     top=bordersize,
#     			#     bottom=bordersize,
#     			#     left=bordersize,
#     			#     right=bordersize,
#     			#     borderType=cv2.BORDER_CONSTANT,
#     			#     value=[mean,mean,mean]
#     			# )
#     			# cv2.imshow('image',img_2)
#     			# cv2.waitKey(0)
#     			# cv2.destroyAllWindows()
#
#     			# Convert to grayscale.
#                 p1 = np.zeros((4, 2))
#     			p2 = np.zeros((4, 2))
#
#     			img1 = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY)
#                 contours, _= cv2.findContours(img1, cv2.RETR_TREE,
#                                    cv2.CHAIN_APPROX_SIMPLE)
#                 for cnt in contours :
#
#                                        approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
#
#                                        # draws boundary of contours.
#                                        # cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5)
#
#                                        # Used to flatted the array containing
#                                        # the co-ordinates of the vertices.
#                                        n = approx.ravel()
#                                        i = 0
#
#                                        for j in n :
#                                            if(i % 2 == 0):
#                                                p1[i][0] = n[i]
#                                                p1[i][1] = n[i + 1]
#
#                                                # String containing the co-ordinates.
#                                                # string = str(x) + " " + str(y)
#                                                #
#                                                # if(i == 0):
#                                                #     # text on topmost co-ordinate.
#                                                #     cv2.putText(img2, "Arrow tip", (x, y),
#                                                #     font, 0.5, (255, 0, 0))
#                                                # else:
#                                                #     # text on remaining co-ordinates.
#                                                #     cv2.putText(img2, string, (x, y),
#                                                #     font, 0.5, (0, 255, 0))
#                                                    i = i + 1
#
#     			img2 = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY)
#     			height, width = img2.shape
#
#                 contours, _= cv2.findContours(img2, cv2.RETR_TREE,
#                                    cv2.CHAIN_APPROX_SIMPLE)
#                 for cnt in contours :
#
#                                        approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
#
#                                        # draws boundary of contours.
#                                        # cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5)
#
#                                        # Used to flatted the array containing
#                                        # the co-ordinates of the vertices.
#                                        n = approx.ravel()
#                                        i = 0
#
#                                        for j in n :
#                                            if(i % 2 == 0):
#                                                p2[i][0] = n[i]
#                                                p2[i][1] = n[i + 1]
#
#                                                # String containing the co-ordinates.
#                                                # string = str(x) + " " + str(y)
#                                                #
#                                                # if(i == 0):
#                                                #     # text on topmost co-ordinate.
#                                                #     cv2.putText(img2, "Arrow tip", (x, y),
#                                                #     font, 0.5, (255, 0, 0))
#                                                # else:
#                                                #     # text on remaining co-ordinates.
#                                                #     cv2.putText(img2, string, (x, y),
#                                                #     font, 0.5, (0, 255, 0))
#                                                    i = i + 1
#
#
#
#
#
#
#     			# Create ORB detector with 5000 features.
#
#     			# orb_detector = cv2.ORB_create(5000)
#                 #
#     			# # Find keypoints and descriptors.
#     			# # The first arg is the image, second arg is the mask
#     			# #  (which is not reqiured in this case).
#                 #
#     			# kp1, d1 = orb_detector.detectAndCompute(img1, None)
#     			# kp2, d2 = orb_detector.detectAndCompute(img2, None)
#                 #
#     			# # Match features between the two images.
#     			# # We create a Brute Force matcher with
#     			# # Hamming distance as measurement mode.
#                 #
#     			# matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
#                 #
#     			# # Match the two sets of descriptors.
#                 #
#     			# matches = matcher.match(d1, d2)
#                 #
#     			# # Sort matches on the basis of their Hamming distance.
#                 #
#     			# matches.sort(key = lambda x: x.distance)
#     			# #extra
#     			# # img3 = cv2.drawMatches(img1_color,kp1,img2_color,kp2,matches[:10],None,flags=2)
#     			# # plt.imshow(img3),plt.show()
#     			# # Take the top 90 % matches forward.
#     			# matches = matches[:int(len(matches)*90)]
#     			# no_of_matches = len(matches)
#                 #
#     			# # Define empty matrices of shape no_of_matches * 2.
#     			# p1 = np.zeros((no_of_matches, 2))
#     			# p2 = np.zeros((no_of_matches, 2))
#     			# #
#     			# for j in range(len(matches)):
#     			# 	p1[j, :] = kp1[matches[j].queryIdx].pt
#     			# 	p2[j, :] = kp2[matches[j].trainIdx].pt
#
#     			# Find the homography matrix.
#     			homography, mask = cv2.findHomography(p1, p2, cv2.RANSAC)
#
#     			# Use this matrix to transform the
#     			# colored image wrt the reference image.
#     			transformed_img = cv2.warpPerspective(img1_color, homography, (width, height))
#
#
#     			# Save the output.
#     			#cv2.imwrite('outputad/output_' + str(i) + '.jpg', transformed_img)
#     			# cv2.imwrite('outputads/output_' + str(i) + '.png',transformed_img)
#     		#image registration done
#
#     			#img2 = cv2.imread("data_sets/example.jpg")
#     			img2 = cv2.imread("cropped/rollno3/"+str(2)+".png")
#     			img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#     			#img1 = cv2.imread("outputad/output_" + str(i) + ".jpg")
#     			img1 = cv2.cvtColor(transformed_img,cv2.COLOR_BGR2GRAY)
#
#
#
#
#     			kernel = np.ones((2,2), np.uint8)
#     			thresh1 = cv2.erode(img1,kernel,iterations=2)
#     			thresh1 = cv2.dilate(thresh1,kernel,iterations=2)
#     			ret,thresh1 = cv2.threshold(thresh1,127,255,cv2.THRESH_BINARY_INV)
#     			#cv2.imwrite("resultad/thresh1_" + str(i) + ".jpg", thresh1)
#
#     			thresh2 = cv2.erode(img2,kernel,iterations=2)
#     			thresh2 = cv2.dilate(thresh2,kernel,iterations=2)
#     			ret,thresh2 = cv2.threshold(thresh2,127,255,cv2.THRESH_BINARY_INV)
#     			#cv2.imwrite("resultad/thresh2_" + str(i) + ".jpg", thresh2)
#
#
#
#     			img3 = cv2.absdiff(thresh1, thresh2)
#     			kernel3 = np.ones((5,5),np.uint8)
#     			erosion3 = cv2.erode(img3,kernel3,iterations = 2)
#     			dilation3 = cv2.dilate(erosion3,kernel3,iterations = 1)
#
#     			# dirname="resultt"
#     			# os.mkdir(dirname)
#     			#cv2.imwrite("resultt/resultttt_" + str(i) + ".jpg", dilation3)
#
#
#
#
#     			cv2.imwrite("registered/rollno"+str(k)+"/"+str(2)+".png", dilation3)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#     		# 	img2_color = cv2.imread("cropped/rollno3/"+str(j)+".png")    # Reference image.
#     		# 	# img3_color = cv2.imread("RUN/answer/blank/1.png")
#             #
#             #
#     		# 	# cv2.imshow('image',img1_color)
#     		# 	# cv2.waitKey(0)
#     		# 	# cv2.destroyAllWindows()
#             #
#     		# 	#extra
#     		# 	# row,col=img2_color.shape[:2]
#     		# 	# bottom=img2_color[row-2:row,0:col]
#     		# 	# mean=cv2.mean(bottom)[0]
#     		# 	# bordersize=300
#     		# 	# img_2=cv2.copyMakeBorder(
#     		# 	#     img2_color,
#     		# 	#     top=bordersize,
#     		# 	#     bottom=bordersize,
#     		# 	#     left=bordersize,
#     		# 	#     right=bordersize,
#     		# 	#     borderType=cv2.BORDER_CONSTANT,
#     		# 	#     value=[mean,mean,mean]
#     		# 	# )
#     		# 	# cv2.imshow('image',img_2)
#     		# 	# cv2.waitKey(0)
#     		# 	# cv2.destroyAllWindows()
#             #
#     		# 	# Convert to grayscale.
#             #
#     		# 	img1 = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY)
#     		# 	img2 = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY)
#     		# 	height, width = img2.shape
#             #
#             #
#             #
#             #
#     		# 	# Create ORB detector with 5000 features.
#             #
#     		# 	orb_detector = cv2.ORB_create(5000)
#             #
#     		# 	# Find keypoints and descriptors.
#     		# 	# The first arg is the image, second arg is the mask
#     		# 	#  (which is not reqiured in this case).
#             #
#     		# 	kp1, d1 = orb_detector.detectAndCompute(img1, None)
#     		# 	kp2, d2 = orb_detector.detectAndCompute(img2, None)
#             #
#     		# 	# Match features between the two images.
#     		# 	# We create a Brute Force matcher with
#     		# 	# Hamming distance as measurement mode.
#             #
#     		# 	matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
#             #
#     		# 	# Match the two sets of descriptors.
#             #
#     		# 	matches = matcher.match(d1, d2)
#             #
#     		# 	# Sort matches on the basis of their Hamming distance.
#             #
#     		# 	matches.sort(key = lambda x: x.distance)
#     		# 	#extra
#     		# 	# img3 = cv2.drawMatches(img1_color,kp1,img2_color,kp2,matches[:10],None,flags=2)
#     		# 	# plt.imshow(img3),plt.show()
#     		# 	# Take the top 90 % matches forward.
#     		# 	matches = matches[:int(len(matches)*90)]
#     		# 	no_of_matches = len(matches)
#             #
#     		# 	# Define empty matrices of shape no_of_matches * 2.
#     		# 	p1 = np.zeros((no_of_matches, 2))
#     		# 	p2 = np.zeros((no_of_matches, 2))
#     		# 	#
#     		# 	for j in range(len(matches)):
#     		# 		p1[j, :] = kp1[matches[j].queryIdx].pt
#     		# 		p2[j, :] = kp2[matches[j].trainIdx].pt
#             #
#     		# 	# Find the homography matrix.
#     		# 	homography, mask = cv2.findHomography(p1, p2, cv2.RANSAC)
#             #
#     		# 	# Use this matrix to transform the
#     		# 	# colored image wrt the reference image.
#     		# 	transformed_img = cv2.warpPerspective(img1_color, homography, (width, height))
#             #
#             #
#     		# 	# Save the output.
#     		# 	#cv2.imwrite('outputad/output_' + str(i) + '.jpg', transformed_img)
#     		# 	# cv2.imwrite('outputads/output_' + str(i) + '.png',transformed_img)
#     		# #image registration done
#             #
#     		# 	#img2 = cv2.imread("data_sets/example.jpg")
#     		# 	img2 = cv2.imread("RUN/answer/blank/1.png")
#     		# 	img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#     		# 	#img1 = cv2.imread("outputad/output_" + str(i) + ".jpg")
#     		# 	img1 = cv2.cvtColor(transformed_img,cv2.COLOR_BGR2GRAY)
#             #
#             #
#             #
#             #
#     		# 	kernel = np.ones((2,2), np.uint8)
#     		# 	thresh1 = cv2.erode(img1,kernel,iterations=2)
#     		# 	thresh1 = cv2.dilate(thresh1,kernel,iterations=2)
#     		# 	ret,thresh1 = cv2.threshold(thresh1,127,255,cv2.THRESH_BINARY_INV)
#     		# 	# cv2.imwrite("resultad/thresh1_" + str(i) + ".jpg", thresh1)
#             #
#     		# 	thresh2 = cv2.erode(img2,kernel,iterations=2)
#     		# 	thresh2 = cv2.dilate(thresh2,kernel,iterations=2)
#     		# 	ret,thresh2 = cv2.threshold(thresh2,127,255,cv2.THRESH_BINARY_INV)
#     		# 	# cv2.imwrite("resultad/thresh2_" + str(i) + ".jpg", thresh2)
#             #
#             #
#             #
#     		# 	img3 = cv2.absdiff(thresh1, thresh2)
#     		# 	kernel3 = np.ones((5,5),np.uint8)
#     		# 	erosion3 = cv2.erode(img3,kernel3,iterations = 2)
#     		# 	dilation3 = cv2.dilate(erosion3,kernel3,iterations = 1)
#             #
#     		# 	# dirname="resultt"
#     		# 	# os.mkdir(dirname)
#     		# 	#cv2.imwrite("resultt/resultttt_" + str(i) + ".jpg", dilation3)
#             #
#             #
#             #
#             #
#     		# 	cv2.imwrite("RUN/result/resultt" + str(i) + "/result1"+".png", dilation3)
#
#
#
#
#
#
# def components():
# 	for j in range(1, 10):
# 		# if((j!=2)and(j!=4)and(j!=6)and(j!=9)):
# 			# if((j!=4)and(j!=9)and(j!=11)):
# 			#inputs = cv2.imread("resultt/resultttt_" + str(j) + ".jpg",0)
# 			inputs = cv2.imread("RUN/result/resultt" + str(j) + "/result0.png",0)
# 			#inputs = cv2.imread("result.png",0)
# 			kernel3 = np.ones((5,5),np.uint8)
# 			erosion3 = cv2.erode(inputs,kernel3,iterations = 3)
# 			dilation3 = cv2.dilate(erosion3,kernel3,iterations = 3)
# 			# cv2.imwrite("result_edited/result_edited_" + str(j) + ".jpg", dilation3)
# 			# print(dilation3.shape)
# 			cropped = dilation3[50:1950, 70:860] # cropping should not be fixed, try it to be automatic kinda?
# 			# cv2.imwrite("result_edited/cropped_" + str(j) + ".jpg", cropped)
# 			ret, thresh = cv2.threshold(cropped, 150, 255, cv2.THRESH_BINARY_INV)
#
# 			img = cv2.bitwise_not(thresh)
# 			_, markers = cv2.connectedComponents(img)
# 			# print(markers)
# 			count0 = np.amax(markers)
# 			# print(count)
#
# 			inputs = cv2.imread("RUN/result/resultt" + str(j) + "/result1.png",0)
# 			#inputs = cv2.imread("result.png",0)
# 			kernel3 = np.ones((5,5),np.uint8)
# 			erosion3 = cv2.erode(inputs,kernel3,iterations = 3)
# 			dilation3 = cv2.dilate(erosion3,kernel3,iterations = 3)
# 			# cv2.imwrite("result_edited/result_edited_" + str(j) + ".jpg", dilation3)
# 			# print(dilation3.shape)
# 			cropped = dilation3[50:1950, 70:860] # cropping should not be fixed, try it to be automatic kinda?
# 			# cv2.imwrite("result_edited/cropped_" + str(j) + ".jpg", cropped)
# 			ret, thresh = cv2.threshold(cropped, 150, 255, cv2.THRESH_BINARY_INV)
#
# 			img = cv2.bitwise_not(thresh)
# 			_, markers = cv2.connectedComponents(img)
# 			# print(markers)
# 			count = np.amax(markers)
#
# 			scor=10-count
# 			score=count0-scor
# 			score=score/2
# 			score=count-score
# 			print(count0)
# 			print(count)
# 			# score = abs(int((count/2)-10))
# 			print("Score of roll number",j, " is ",score," out of 10")
#
# # dirname = "cropped"
# # os.mkdir(dirname)
# #
# # for j in range(1,68):
# #     dirname=("cropped/rollno"+str(j))
# #     os.mkdir(dirname)

dirname="registered"
os.mkdir(dirname)
for j in range(1,68):
    dirname=("registered/rollno"+str(j))
    os.mkdir(dirname)

dirname="difference"
os.mkdir(dirname)

for j in range (1,68):
    dirname=("difference/rollno"+str(j))
    os.mkdir(dirname)

# for j in range(1,68):
#     if j!=26 and j!=48:
#         box_extraction("data/image_"+str(j)+".jpg","./cropped/rollno"+str(j)+"/")
# registration()
