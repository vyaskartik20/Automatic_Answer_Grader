# USAGE
# python image_diff.py --first images/original_01.png --second images/modified_01.png

# import the necessary packages
from skimage.measure import compare_ssim
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-f", "--first", required=True,
# 	help="first input image")
# ap.add_argument("-s", "--second", required=True,
# 	help="second")
# args = vars(ap.parse_args())

# load the two input images
imageA = cv2.imread("image.png")
imageB = cv2.imread("ref.png")

(H, W, B) = imageA.shape
# # to resize and set the new width and height
# print (imageA.shape)
# print (imageB.shape)
imageB = cv2.resize(imageB, (W, H))

cv2.imwrite("B2.png", imageB)

# imageA=cv2.resize(imageA,imageB.shape)


# convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))

# threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
thresh = cv2.threshold(diff, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

count=0

# loop over the contours
for c in cnts:
	# compute the bounding box of the contour and then draw the
	# bounding box on both input images to represent where the two
	# images differ
	(x, y, w, h) = cv2.boundingRect(c)
	cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
	if(cv2.contourArea(c)>2000):
		count+=1


# show the output images
print(count)
cv2.imwrite("Original.png", imageA)
cv2.imwrite("Modified.png", imageB)
cv2.imwrite("Diff.png", diff)
cv2.imwrite("Thresh.png", thresh)
cv2.waitKey(0)
