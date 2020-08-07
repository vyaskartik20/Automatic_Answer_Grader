import cv2
import numpy as np
import os


def sort_contours(cnts, method="left-to-right"):
    # initialize the reverse flag and sort index
    reverse = False
    i = 0

    # handle if we need to sort in reverse
    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True

    # handle if we are sorting against the y-coordinate rather than
    # the x-coordinate of the bounding box
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1

    # construct the list of bounding boxes and sort them from top to
    # bottom
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b: b[1][i], reverse=reverse))

    # return the list of sorted contours and bounding boxes
    return (cnts, boundingBoxes)

def box_extraction(img_for_box_extraction_path, cropped_dir_path):

    img = cv2.imread(img_for_box_extraction_path, 0)  # Read the image
    (thresh, img_bin) = cv2.threshold(img, 128, 255,
                                      cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # Thresholding the image
    img_bin = 255-img_bin  # Invert the image

    cv2.imwrite("Image_bin.jpg",img_bin)

    # Defining a kernel length
    kernel_length = np.array(img).shape[1]//400

    # A verticle kernel of (1 X kernel_length), which will detect all the verticle lines from the image.
    verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
    # A horizontal kernel of (kernel_length X 1), which will help to detect all the horizontal line from the image.
    hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
    # A kernel of (3 X 3) ones.
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # Morphological operation to detect verticle lines from an image
    img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=3)
    verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=3)
    cv2.imwrite("verticle_lines.jpg",verticle_lines_img)

    # Morphological operation to detect horizontal lines from an image
    img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=3)
    horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=3)
    cv2.imwrite("horizontal_lines.jpg",horizontal_lines_img)

    # Weighting parameters, this will decide the quantity of an image to be added to make a new image.
    alpha = 0.50
    beta = 1.0 - alpha
    # This function helps to add two image with specific weight parameter to get a third image as summation of two image.
    img_final_bin = cv2.addWeighted(verticle_lines_img, alpha, horizontal_lines_img, beta, 0.0)
    img_final_bin = cv2.erode(~img_final_bin, kernel, iterations=2)
    (thresh, img_final_bin) = cv2.threshold(img_final_bin, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # For Debugging
    # Enable this line to see verticle and horizontal lines in the image which is used to find boxes
    cv2.imwrite("img_final_bin.jpg",img_final_bin)
    # Find contours for image, which will detect all the boxes
    contours, hierarchy = cv2.findContours(
        img_final_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # print(len(contours))
    # Sort all the contours by top to bottom.
    (contours, boundingBoxes) = sort_contours(contours, method="left-to-right")

    x1=0
    y1=0
    # check=0
    idx = 0
    for c in contours:
        # if check!=3:
            # Returns the location and width,height for every contour
            x, y, w, h = cv2.boundingRect(c)
            # check+=1



            if ((x>(x1+20))):
            # if ((x==x1)):
                if (w > 400 and h > 60) and (h > 1.3*w):
                    idx += 1

                    extLeft = tuple(c[c[:, :, 0].argmin()][0])
                    extRight = tuple(c[c[:, :, 0].argmax()][0])
                    extTop = tuple(c[c[:, :, 1].argmin()][0])
                    extBot = tuple(c[c[:, :, 1].argmax()][0])

                    print (extLeft)
                    print ("    ")
                    print(extRight)
                    print ("    ")
                    print (extTop)
                    print ("    ")
                    print(extBot)
                    print ("\n")

                    # print (x1)
                    # print ("    ")
                    # print(w)
                    # print ("\n")
                    # print (h)
                    # print ("\n")
                    new_img = img[y:y+h, x:x+w]
                    cv2.imwrite(cropped_dir_path+str(idx) + '.png', new_img)
                    x1=x
                    y1=y



            # If the box height is greater then 20, widht is >80, then only save it as a box in "cropped/" folder.
            # if (w > 40 and h > 60) and (w<1000) and (h > 1.5*w):


    # For Debugging
    # Enable this line to see all contours.
    # cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
    # cv2.imwrite("./Temp/img_contour.jpg", img)

#
dirname = "test"
os.mkdir(dirname)

for j in range(1, 68):
    dirname =("test/Cropped"+ str(j))
    os.mkdir(dirname)

# for j in range(1, 11):
# 	inputs = cv2.imread("result/result_" + str(j) + ".jpg",0)
#


# data/image_20.jpg

for j in range(1, 68):
    if((j!=26)and(j!=48)):
        box_extraction("data/image_"+str(j)+".jpg", "./test/Cropped"+str(j)+"/")


# box_extraction("image_312.jpg", "./Cropped/")
