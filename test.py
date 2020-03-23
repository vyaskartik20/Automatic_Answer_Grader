import cv2
import numpy as np

input=cv2.imread("OMR_phone.jpg")
cv2.imshow("input",input)
cv2.waitKey(0)
cropped=input[20:int(.98*len(input)),20:int(98*len(input[0]))]
cv2.imshow("cropped",cropped)
cv2.waitKey(0)
