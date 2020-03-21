import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
from PIL import Image
# from transform_example import transfer
from pyimagesearch.transform import four_point_transform
from connected_component import components
from image_regg import registration

def registration():
    for k in range(1,68):
        if k!=26 and k!=48:
            img1_color = cv2.imread("cropped/rollno"+str(k) + "/" +str(1)+ ".png")
            img2_color = cv2.imread("cropped/rollno3/"+str(1)+".png")
            p1 = np.zeros((4, 2))
            p2 = np.zeros((4, 2))
            img1 = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY)
            contours, _= cv2.findContours(img1, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
                n = approx.ravel()
                i = 0
                for j in n:
                    if i%2==0:
                        p1[i][0] = n[i]
                        p1[i][1] = n[i + 1]
                        i = i + 1
            print(n)
            img2 = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY)
            height, width = img2.shape
            contours, _= cv2.findContours(img2, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
                n = approx.ravel()
                i=0
                for j in n:
                    if i%2==0:
                        p2[i][0]=n[i]
                        p2[i][1]=n[i+1]
                        i=i+1
            homography, mask = cv2.findHomography(np.float32(p1), np.float32(p2), cv2.RANSAC)
            transformed_img = cv2.warpPerspective(img1_color, homography, (width, height))
            img2 = cv2.imread("cropped/rollno3/"+str(1)+".png")
            img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
            img1 = cv2.cvtColor(transformed_img,cv2.COLOR_BGR2GRAY)

            kernel = np.ones((2,2), np.uint8)
            thresh1 = cv2.erode(img1,kernel,iterations=2)
            thresh1 = cv2.dilate(thresh1,kernel,iterations=2)
            ret,thresh1 = cv2.threshold(thresh1,127,255,cv2.THRESH_BINARY_INV)

            thresh2 = cv2.erode(img2,kernel,iterations=2)
            thresh2 = cv2.dilate(thresh2,kernel,iterations=2)
            ret,thresh2 = cv2.threshold(thresh2,127,255,cv2.THRESH_BINARY_INV)

            img3 = cv2.absdiff(thresh1, thresh2)
            kernel3 = np.ones((5,5),np.uint8)
            erosion3 = cv2.erode(img3,kernel3,iterations = 2)
            dilation3 = cv2.dilate(erosion3,kernel3,iterations = 1)
            cv2.imwrite("registered/rollno"+str(k)+"/"+str(1)+".png", transformed_img)
            cv2.imwrite("difference/rollno"+str(k)+"/"+str(1)+".png", dilation3)


            img1_color = cv2.imread("cropped/rollno"+str(k) + "/" +str(2)+ ".png")
            img2_color = cv2.imread("cropped/rollno3/"+str(2)+".png")
            p1 = np.zeros((4, 2))
            p2 = np.zeros((4, 2))
            img1 = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY)
            contours, _= cv2.findContours(img1, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
                n = approx.ravel()
                i = 0
                for j in n:
                    if i%2==0:
                        p1[i][0] = n[i]
                        p1[i][1] = n[i + 1]
                        i = i + 1
            print(n)
            img2 = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY)
            height, width = img2.shape
            contours, _= cv2.findContours(img2, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
                n = approx.ravel()
                i=0
                for j in n:
                    if i%2==0:
                        p2[i][0]=n[i]
                        p2[i][1]=n[i+1]
                        i=i+1
            homography, mask = cv2.findHomography(np.float32(p1), np.float32(p2), cv2.RANSAC)
            transformed_img = cv2.warpPerspective(img1_color, homography, (width, height))
            img2 = cv2.imread("cropped/rollno3/"+str(2)+".png")
            img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
            img1 = cv2.cvtColor(transformed_img,cv2.COLOR_BGR2GRAY)

            kernel = np.ones((2,2), np.uint8)
            thresh1 = cv2.erode(img1,kernel,iterations=2)
            thresh1 = cv2.dilate(thresh1,kernel,iterations=2)
            ret,thresh1 = cv2.threshold(thresh1,127,255,cv2.THRESH_BINARY_INV)

            thresh2 = cv2.erode(img2,kernel,iterations=2)
            thresh2 = cv2.dilate(thresh2,kernel,iterations=2)
            ret,thresh2 = cv2.threshold(thresh2,127,255,cv2.THRESH_BINARY_INV)

            img3 = cv2.absdiff(thresh1, thresh2)
            kernel3 = np.ones((5,5),np.uint8)
            erosion3 = cv2.erode(img3,kernel3,iterations = 2)
            dilation3 = cv2.dilate(erosion3,kernel3,iterations = 1)
            cv2.imwrite("registered/rollno"+str(k)+"/"+str(2)+".png", transformed_img)
            cv2.imwrite("difference/rollno"+str(k)+"/"+str(2)+".png", dilation3)
registration()
