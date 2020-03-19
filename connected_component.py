import cv2
import numpy as np

def components():
	for j in range(1, 10):
		# if((j!=2)and(j!=4)and(j!=6)and(j!=9)):
			# if((j!=4)and(j!=9)and(j!=11)):
			#inputs = cv2.imread("resultt/resultttt_" + str(j) + ".jpg",0)
			inputs = cv2.imread("RUN/result/resultt" + str(j) + "/result0.png",0)
			#inputs = cv2.imread("result.png",0)
			kernel3 = np.ones((5,5),np.uint8)
			erosion3 = cv2.erode(inputs,kernel3,iterations = 3)
			dilation3 = cv2.dilate(erosion3,kernel3,iterations = 3)
			# cv2.imwrite("result_edited/result_edited_" + str(j) + ".jpg", dilation3)
			# print(dilation3.shape)
			cropped = dilation3[50:1950, 70:860] # cropping should not be fixed, try it to be automatic kinda?
			# cv2.imwrite("result_edited/cropped_" + str(j) + ".jpg", cropped)
			ret, thresh = cv2.threshold(cropped, 150, 255, cv2.THRESH_BINARY_INV)

			img = cv2.bitwise_not(thresh)
			_, markers = cv2.connectedComponents(img)
			# print(markers)
			count0 = np.amax(markers)
			# print(count)

			inputs = cv2.imread("RUN/result/resultt" + str(j) + "/result1.png",0)
			#inputs = cv2.imread("result.png",0)
			kernel3 = np.ones((5,5),np.uint8)
			erosion3 = cv2.erode(inputs,kernel3,iterations = 3)
			dilation3 = cv2.dilate(erosion3,kernel3,iterations = 3)
			# cv2.imwrite("result_edited/result_edited_" + str(j) + ".jpg", dilation3)
			# print(dilation3.shape)
			cropped = dilation3[50:1950, 70:860] # cropping should not be fixed, try it to be automatic kinda?
			# cv2.imwrite("result_edited/cropped_" + str(j) + ".jpg", cropped)
			ret, thresh = cv2.threshold(cropped, 150, 255, cv2.THRESH_BINARY_INV)

			img = cv2.bitwise_not(thresh)
			_, markers = cv2.connectedComponents(img)
			# print(markers)
			count = np.amax(markers)

			scor=10-count
			score=count0-scor
			score=score/2
			score=count-score
			print(count0)
			print(count)
			# score = abs(int((count/2)-10))
			print("Score of roll number",j, " is ",score," out of 10")
