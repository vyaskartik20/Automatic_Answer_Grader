import cv2
import numpy as np
import sys

if __name__ == "__main__":
    if(len(sys.argv)) < 2:
        file_path = "sample.png"
    else:
        file_path = sys.argv[1]

    # read image
    src = cv2.imread(file_path, 1)
    src2 = cv2.imread(file_path, 1)
    # show source image
    # cv2.imshow("Source", src)

    # convert image to gray scale
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    # blur the image
    blur = cv2.blur(gray, (10, 10))

    # binary thresholding of the image
    ret, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)

    # find contours
    # im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, \
    #         cv2.CHAIN_APPROX_SIMPLE)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
    color_contours = (0, 255, 0) # color for contours
    color = (255, 255, 255) # color for convex hull

    # create hull array for convexHull points
    hull = []

    # calculate points for each contour
    for i in range(len(contours)):
        hull.append(cv2.convexHull(contours[i], False))
        cv2.drawContours(drawing, contours, i, color_contours, 2, 8, hierarchy)
        # draw convex hull
        cv2.drawContours(drawing, hull, i, color, 2, 8)
        if((cv2.contourArea(contours[i]))>5000):
            print("yes")
            cv2.drawContours(src2, contours,  i, (255,0,0), 2)
            cv2.imwrite('src22.png',src2)
        #     # cv2.drawContours(drawing, contours[i], i, color_contours, 2, 8, hierarchy)
        #     # # draw convex hull
        #     # cv2.drawContours(drawing, hull[i], i, color, 2, 8)
        #     print(cv2.contourArea(contours[i]))
        # print("yes")
        #     print(hull[i])


        # mask = np.zeros_like(src) # Create mask where white is what we want, black otherwise
        # cv2.drawContours(mask, contours, i, 255, -1) # Draw filled contour in mask
        # out = np.zeros_like(src) # Extract out the object and place into output image
        # out[mask == 255] = src[mask == 255]
        #
        # # Now crop
        # (y, x) = np.where(mask == 255)
        # (topy, topx) = (np.min(y), np.min(x))
        # (bottomy, bottomx) = (np.max(y), np.max(x))
        # out = out[topy:bottomy+1, topx:bottomx+1]
        #
        # # Show the output image
        # cv2.imwrite('Output.png', out)

    # contour_list = []
    # for contour in contours:
    #     # approximte for circles
    #     approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    #     area = cv2.contourArea(contour)
    #     if ((len(approx) > 8) & (area > 30) ):
    #         contour_list.append(contour)
    #
    # # Draw contours on the original image
    # cv2.drawContours(src, contour_list,  -1, (255,0,0), 2)
    #
    #
    # # there is an outer boundary and inner boundary for each eadge, so contours double
    # print('Number of found circles: {}'.format(int(len(contour_list)/2)))
    #
    # #Displaying the results
    # # cv2.imshow('Objects Detected', clone)
    # cv2.imwrite("Treshed.png", gray_threshed)



    # create an empty black image

    # draw contours and hull points
    # for i in range(len(contours)):
    #
    #     # draw contours
    #     cv2.drawContours(drawing, contours, i, color_contours, 2, 8, hierarchy)
    #     # draw convex hull
    #     cv2.drawContours(drawing, hull, i, color, 2, 8)

    cv2.imwrite("Output.png", drawing)
    # cv2.imwrite(cropped_dir_path+str(idx) + '.png', new_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
