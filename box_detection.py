import cv2
import numpy as np
import os
# from transform_example import transfer
from pyimagesearch.transform import four_point_transform

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
    img2 = cv2.imread(img_for_box_extraction_path, 0)
    img3 = cv2.imread(img_for_box_extraction_path, 0)
    font = cv2.FONT_HERSHEY_COMPLEX
    # img = cv2.blur(img,(10,10))
    (thresh, img_bin) = cv2.threshold(img, 128, 255,
                                      cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # Thresholding the image
    img_bin = 255-img_bin  # Invert the image

    # img = np.full((100,80,3), 12, np.uint8)


    # threshold image
    # ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                    # 127, 255, cv2.THRESH_BINARY)
    img = cv2.blur(img,(20,20))

    cv2.imwrite("Methodology/Image_bin.jpg",img_bin)

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
    cv2.imwrite("Methodology/verticle_lines.jpg",verticle_lines_img)

    # Morphological operation to detect horizontal lines from an image
    img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=3)
    horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=3)
    cv2.imwrite("Methodology/horizontal_lines.jpg",horizontal_lines_img)

    # Weighting parameters, this will decide the quantity of an image to be added to make a new image.
    alpha = 0.50
    beta = 1.0 - alpha
    # This function helps to add two image with specific weight parameter to get a third image as summation of two image.
    img_final_bin = cv2.addWeighted(verticle_lines_img, alpha, horizontal_lines_img, beta, 0.0)
    img_final_bin = cv2.erode(~img_final_bin, kernel, iterations=2)
    (thresh, img_final_bin) = cv2.threshold(img_final_bin, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # For Debugging
    # Enable this line to see verticle and horizontal lines in the image which is used to find boxes
    cv2.imwrite("Methodology/img_final_bin.jpg",img_final_bin)
    # Find contours for image, which will detect all the boxes
    contours, hierarchy = cv2.findContours(
        img_final_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # print(len(contours))
    # Sort all the contours by top to bottom.
    (contours, boundingBoxes) = sort_contours(contours, method="left-to-right")

    x1=-100
    y1=0
    # check=0
    idx = 0
    for c in contours:
        # if check!=3:
            # Returns the location and width,height for every contour
            x, y, w, h = cv2.boundingRect(c)
            # check+=1



            # if ((x==x1)):
            if (w > 400 and h > 60) and (h > 1.3*w):
            # if(cv2.contourArea(c)>50):
                # if ((x>(x1+300))):
                if ((x<(x1+50))):
                    idx += 1

                    # rect = cv2.minAreaRect(c)
                    # box = cv2.boxPoints(rect)
                    #
                    # box = np.int0(box)
                    # # draw a red 'nghien' rectangle
                    # cv2.drawContours(img, [box], 0, (0, 0, 255))
                    # cv2.imwrite("contour1.png", img)
                    # # finally, get the min enclosing circle


                    # hull = cv.c(points[, hull[, clockwise[, returnPoints]]
                    # hull = cv2.convexHull(c)
                    # print(hull)



                    itr=0

                    approx = cv2.approxPolyDP(c, 0.009 * cv2.arcLength(c, True), True)

# draws boundary of contours.
                    cv2.drawContours(img3, [approx], 0, (0, 0, 255), 5)

                    # Used to flatted the array containing
                    # the co-ordinates of the vertices.
                    nq = approx.ravel()
                    iq = 0

                    for jq in nq :
                        if(iq % 2 == 0):
                            xq = nq[iq]
                            yq = nq[iq + 1]

                    # String containing the co-ordinates.
                            string = str(xq) + " " + str(yq)

                    #if(i == 0):
                    # text on topmost co-ordinate.
                    # cv2.putText(img2, "Arrow tip", (x, y),
                    # font, 0.5, (255, 0, 0))
                    #else:
                    # text on remaining co-ordinates.
                            cv2.putText(img3, string, (xq, yq),
                            font, 0.5, (255, 255, 0))

                            if(itr==1):
                                # xq=xq-16
                                # yq=yq-16
                                extTop="(%s, %s)" %(xq, yq)
                            if(itr==2):
                                # xq=xq+16
                                # yq=yq-16
                                extRight="(%s, %s)" %(xq, yq)
                            if(itr==3):
                                # xq=xq+16
                                # yq=yq+16
                                extBot="(%s, %s)" %(xq, yq)
                            if(itr==0):
                                # xq=xq-16
                                # yq=yq+16
                                extLeft="(%s, %s)" %(xq, yq)

                            itr = itr + 1

                            # print(xq, yq)
                        iq = iq + 1

                    # Showing the final image.

                    # cv2.imwrite('image2.png', img3)

                    coords="[%s, %s, %s, %s]" %(extTop,extRight,extBot,extLeft)


                    # extLeft = tuple(c[c[:, :, 0].argmin()][0])
                    # extRight = tuple(c[c[:, :, 0].argmax()][0])
                    # extTop = tuple(c[c[:, :, 1].argmin()][0])
                    # extBot = tuple(c[c[:, :, 1].argmax()][0])

                    # hull = []
                    #
                    # # calculate points for each contour
                    #
                    # hull.append(cv2.convexHull(c, False))
                    #
                    # # create an empty black image
                    # drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
                    #
                    # # draw contours and hull points
                    #
                    # color_contours = (0, 255, 0) # color for contours
                    # color = (255, 255, 255) # color for convex hull
                    # # draw contours
                    # cv2.drawContours(drawing, contours, i, color_contours, 2, 8, hierarchy)
                    # # draw convex hull
                    # cv2.drawContours(drawing, hull, i, color, 2, 8)


                    # extTop="(%s, %s)" %(box[1][0],box[1][1])
                    # extRight="(%s, %s)" %(box[2][0],box[2][1])
                    # extBot="(%s, %s)" %(box[3][0],box[3][1])
                    # extLeft="(%s, %s)" %(box[0][0],box[0][1])

                    # extTop="(%s, %s)" %(box[1][0],box[1][1])
                    # extRight="(%s, %s)" %(box[2][0],box[2][1])
                    # extBot="(%s, %s)" %(box[3][0],box[3][1])
                    # extLeft="(%s, %s)" %(box[0][0],box[0][1])


                    coords="[%s, %s, %s, %s]" %(extTop,extRight,extBot,extLeft)

                    pts = np.array(eval(coords), dtype = "float32")


                    new_img = four_point_transform(img2,pts)
                    cv2.imwrite(cropped_dir_path+str(idx) + '.png', new_img)
                    # print(x)



                    # box = np.int0(box)
                    # # draw a red 'nghien' rectangle
                    # cv2.drawContours(img, [box], 0, (0, 0, 255))
                    # cv2.imwrite("contour1.png", img)
                    # coords="[(189.96536, 1084.9089), (822.29297, 1050.0603), (990.5377, 2167.3167), (328.2101, 2246.1653)]"
                    # [(189.96536, 1084.9089), (852.29297, 1006.0603), (990.5377, 2167.3167), (328.2101, 2246.1653)]
                x1=x
            # print(x)
                y1=y
                    # x1=x
                    # y1=y

                    # print(coords)

                    # img1 = cv2.imread(img_for_box_extraction_path, 0)  # Read the image
                    # cv2.drawContours(img1,c, -1, (0, 255, 255), 2)
                    # cv2.circle(img1, (189,1084) , 8, (0, 0, 255), -1)
                    # cv2.circle(img1, (852,1006) , 8, (0, 255, 0), -1)
                    # cv2.circle(img1, (990,2167) , 8, (255, 0, 0), -1)
                    # cv2.circle(img1, (328,2246) , 8, (255, 255, 0), -1)
                    # cv2.imwrite('new.png', img1)


                    # if((extLeft[1])>(extBot[1])):
                    #     coords="[%s, %s, %s, %s]" %(extLeft,extTop,extRight,extBot)
                    #
                    # else:
                    #     coords="[%s, %s, %s, %s]" %(extTop,extRight,extBot,extLeft)

                    # print (extLeft)
                    # print ("    ")
                    # print(extRight)
                    # print ("    ")
                    # print (extTop)
                    # print ("    ")
                    # print(extBot)
                    # print ("\n")

                    # box = cv2.boxPoints(c)

                    # coords=(str1+ (extLeft) + str3 + (extTop)+ str3 +(extRight)+ str3 + (extBot)+str2)


                    # print(coords)

                    # print (x1)
                    # print ("    ")
                    # print(w)
                    # print ("\n")
                    # print (h)
                    # print ("\n")




            # If the box height is greater then 20, widht is >80, then only save it as a box in "cropped/" folder.
            # if (w > 40 and h > 60) and (w<1000) and (h > 1.5*w):


    # For Debugging
    # Enable this line to see all contours.
    # cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
    # cv2.imwrite("./Temp/img_contour.jpg", img)

#
dirname = "test15"
os.mkdir(dirname)

for j in range(1, 15):
    dirname =("test15/Cropped"+ str(j))
    os.mkdir(dirname)

dirname = "result"
os.mkdir(dirname)

for j in range(1, 15):
    dirname =("result/resultt"+ str(j))
    os.mkdir(dirname)

# box_extraction("set/image_"+".jpg", "")

for j in range(1,15):
    # if((j!=26)and(j!=48)):
    box_extraction("set/image_"+str(j)+".jpg", "./test15/Cropped"+str(j)+"/")



# box_extraction("image_312.jpg", "./Cropped/")
