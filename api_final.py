import numpy as np
import cv2
import json
from flask import Flask,request,Response,jsonify
import os
from matplotlib import pyplot as plt
from PIL import Image
import shutil

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello():
    return "hello"


@app.route('/upload',methods=['GET','POST'])
def upload():
    dirname="SAVED"
    os.mkdir(dirname)
    images=request.files.to_dict()
    j=0
    for image in images:
        print(images[image])
        file_name = images[image].filename
        images[image].save("SAVED/"+str(j)+".jpg")
        j=j+1
    dirname = "RUN"
    os.mkdir(dirname)

    dirname = "RUN/Cropped"
    os.mkdir(dirname)

    dirname="RUN/Cropped/OMR"
    os.mkdir(dirname)
    dirname="RUN/Cropped/ANSWER_KEY"
    os.mkdir(dirname)

    dirname="RUN/Registered"
    os.mkdir(dirname)
    dirname="RUN/Difference"
    os.mkdir(dirname)


    for j in range(1,2):
        dirname=("RUN/Cropped/ROLLNO_"+str(j))
        os.mkdir(dirname)

        dirname=("RUN/Registered/ROLLNO_"+str(j))
        os.mkdir(dirname)
        dirname="RUN/Registered/ROLLNO_"+ str(j) +"/Filled"
        os.mkdir(dirname)
        dirname="RUN/Registered/ROLLNO_"+ str(j) +"/Empty"
        os.mkdir(dirname)

        dirname=("RUN/Difference/ROLLNO_"+str(j))
        os.mkdir(dirname)
        dirname="RUN/Difference/ROLLNO_"+ str(j) +"/Filled"
        os.mkdir(dirname)
        dirname="RUN/Difference/ROLLNO_" + str(j) + "/Empty"
        os.mkdir(dirname)
    box_extraction("SAVED/0.jpg","./RUN/Cropped/OMR/")
    box_extraction("SAVED/2.jpg","./RUN/Cropped/ANSWER_KEY/")
    box_extraction("SAVED/1.jpg","./RUN/Cropped/ROLLNO_"+str(1)+"/")
    registration()
    list=components()
    # print(list)
    cattempted=list[0]
    cunattempt=list[1]
    wrong=list[2]
    score=list[3]

    shutil.rmtree('RUN/Difference')

    shutil.rmtree('RUN/Registered')
  
    shutil.rmtree('RUN/Cropped')
    shutil.rmtree('RUN')
    shutil.rmtree('SAVED')

    return jsonify(attempted=str(int(cattempted)),unattemped=str(int(cunattempt)),wrong=str(int(wrong)),score=str(score))

def sort_contours(cnts, method="left-to-right"):
    reverse = False
    i = 0

    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True

    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1

    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b: b[1][i], reverse=reverse))

    return (cnts, boundingBoxes)

def box_extraction(img_for_box_extraction_path, cropped_dir_path):

    img = cv2.imread(img_for_box_extraction_path, 0)  # Read the image
    img2 = cv2.imread(img_for_box_extraction_path, 0)
    img3 = cv2.imread(img_for_box_extraction_path, 0)
    font = cv2.FONT_HERSHEY_COMPLEX
    (thresh, img_bin) = cv2.threshold(img, 128, 255,
                                      cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # Thresholding the image
    img_bin = 255-img_bin  # Invert the image

    img = cv2.blur(img,(20,20))

    kernel_length = np.array(img).shape[1]//400

    verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
    hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=3)
    verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=3)

    img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=3)
    horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=3)
   
    alpha = 0.50
    beta = 1.0 - alpha
    img_final_bin = cv2.addWeighted(verticle_lines_img, alpha, horizontal_lines_img, beta, 0.0)
    img_final_bin = cv2.erode(~img_final_bin, kernel, iterations=2)
    (thresh, img_final_bin) = cv2.threshold(img_final_bin, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)


    contours, hierarchy = cv2.findContours(
        img_final_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    (contours, boundingBoxes) = sort_contours(contours, method="left-to-right")

    x1=-100
    y1=0
    # check=0
    idx = 0
    for c in contours:
            x, y, w, h = cv2.boundingRect(c)
          
            # if(cv2.contourArea(c)>50):
            if(cv2.contourArea(c)>50000):
                if (w > 300 and h > 400 and((h<(4*w))and(h>(0.6*w))) and(x!=0)):
                    if ((x>(x1+100))): #outer
                    # if ((x<(x1+50))): #inner
                        idx += 1



                        itr=0

                        approx = cv2.approxPolyDP(c, 0.009 * cv2.arcLength(c, True), True)

    # draws boundary of contours.
                        cv2.drawContours(img3, [approx], 0, (0, 0, 255), 5)

                        nq = approx.ravel()
                        iq = 0

                        for jq in nq :
                            if(iq % 2 == 0):
                                xq = nq[iq]
                                yq = nq[iq + 1]

                                string = str(xq) + " " + str(yq)

                                cv2.putText(img3, string, (xq, yq),
                                font, 0.5, (255, 255, 0))

                                if(itr==1):
                                    extTop="(%s, %s)" %(xq, yq)
                                if(itr==2):
                                    extRight="(%s, %s)" %(xq, yq)
                                if(itr==3):
                                    extBot="(%s, %s)" %(xq, yq)
                                if(itr==0):
                                    extLeft="(%s, %s)" %(xq, yq)

                                itr = itr + 1

                            iq = iq + 1


                        coords="[%s, %s, %s, %s]" %(extTop,extRight,extBot,extLeft)

                        pts = np.array(eval(coords), dtype = "float32")


                        new_img = four_point_transform(img2,pts)
                        cv2.imwrite(cropped_dir_path+str(idx) + '.png', new_img)
                        # print(x)



                    # x1=x #inner

                    # x1=x #inner

                    # y1=y
                        x1=x  #outer
                        # y1=y
                    # print(x)


def registration():

    for k in range(1,2):
        if k!=26 and k!=48:
            #for 3
            for p in range(1,4):

                img1_color = cv2.imread("RUN/Cropped/ROLLNO_"+str(k) + "/" +str(p)+ ".png")
                img2_color = cv2.imread("RUN/Cropped/ANSWER_KEY/"+str(p)+".png")

                img1 = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY)
                img2 = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY)
                height, width = img2.shape

                p1=box_extractionqw("RUN/Cropped/ROLLNo_"+str(k) + "/" +str(p)+ ".png")
                p2=box_extractionqw("RUN/Cropped/ANSWER_KEY/"+str(p)+".png")

                homography, mask = cv2.findHomography(np.float32(p1), np.float32(p2), cv2.RANSAC)
                transformed_img = cv2.warpPerspective(img1_color, homography, (width, height))
                img2 = cv2.imread("RUN/Cropped/ANSWER_KEY/"+str(p)+".png")
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
                cropped=dilation3[20:int(.98*len(dilation3)),20:int(.98*(len(dilation3[0])))]
                cv2.imwrite("RUN/Difference/ROLLNO_"+ str(k) +"/Filled/" +str(p)+".png", cropped)
                cv2.imwrite("RUN/Registered/ROLLNO_"+ str(k) +"/Filled/" +str(p)+".png", transformed_img)




                img1_color = cv2.imread("RUN/Cropped/ROLLNO_"+str(k) + "/" +str(p)+ ".png")
                img2_color = cv2.imread("RUN/Cropped/OMR/"+str(p)+".png")

                img1 = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY)
                img2 = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY)
                height, width = img2.shape

                p1=box_extractionqw("RUN/Cropped/ROLLNo_"+str(k) + "/" +str(p)+ ".png")
                p2=box_extractionqw("RUN/Cropped/OMR/"+str(p)+".png")

                homography, mask = cv2.findHomography(np.float32(p1), np.float32(p2), cv2.RANSAC)
                transformed_img = cv2.warpPerspective(img1_color, homography, (width, height))
                img2 = cv2.imread("RUN/Cropped/OMR/"+str(p)+".png")
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
                cropped=dilation3[20:int(.98*len(dilation3)),20:int(.98*(len(dilation3[0])))]
                cv2.imwrite("RUN/Difference/ROLLNO_"+ str(k) +"/Empty/" +str(p)+".png", cropped)
                cv2.imwrite("RUN/Registered/ROLLNO_"+ str(k) +"/Empty/" +str(p)+".png", transformed_img)


def components():

    for j in range(1,2):

        if j!=26 and j!=48:
            cans=0
            cattempted=0
            c1ans=0
            c1attempted=0
            #for 3
            for p in range(1,4):
            #for 2
            # for p in range(1,3):

                inputs = cv2.imread("RUN/Difference/ROLLNO_"+ str(j) +"/Filled/" + str(p) + ".png",0)
                kernel3 = np.ones((5,5),np.uint8)
                erosion3 = cv2.erode(inputs,kernel3,iterations = 3)
                dilation3 = cv2.dilate(erosion3,kernel3,iterations = 3)
                ret, thresh = cv2.threshold(dilation3, 150, 255, cv2.THRESH_BINARY_INV)
                img = cv2.bitwise_not(thresh)
                _, markers = cv2.connectedComponents(img)
                c1ans = np.amax(markers) #total number of connected components with filled anwerkey
                #print(c1ans)
                cans=c1ans+cans



                inputs = cv2.imread("RUN/Difference/ROLLNO_"+ str(j) +"/Empty/" + str(p) + ".png",0)
                kernel3 = np.ones((5,5),np.uint8)
                erosion3 = cv2.erode(inputs,kernel3,iterations = 3)
                dilation3 = cv2.dilate(erosion3,kernel3,iterations = 3)
                ret, thresh = cv2.threshold(dilation3, 150, 255, cv2.THRESH_BINARY_INV)
                img = cv2.bitwise_not(thresh)
                _, markers = cv2.connectedComponents(img)
                c1attempted = np.amax(markers) #total number of connected components with empty OMR
                #print(c1attempted)
                cattempted=c1attempted+cattempted
                # print("kartik")




            cunattempt=30-cattempted  

            wrongattempt=cans-cunattempt 
            wrongattempt=wrongattempt/2
            score=cattempted-wrongattempt
            # print(count_1)
            # score2=c2attempted-wrong2attempt/2
            # print(score1)
            # print(score2)
            # print(The marks of RollNO")
            #print(cans)
            #print(cattempted)
            # print("Score of roll number",j, " is ",score," out of 30")
            return [cattempted,cunattempt,wrongattempt,score];


def order_points(pts):
	rect = np.zeros((4, 2), dtype = "float32")

	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]

	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]

	return rect

def four_point_transform(image, pts):
	rect = order_points(pts)
	(tl, tr, br, bl) = rect

	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))

	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))

	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")

	M = cv2.getPerspectiveTransform(rect, dst)
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

	return warped

def box_extractionqw(img_for_box_extraction_path):

    img = cv2.imread(img_for_box_extraction_path, 0)  # Read the image
    img2 = cv2.imread(img_for_box_extraction_path, 0)
    img3 = cv2.imread(img_for_box_extraction_path, 0)
    font = cv2.FONT_HERSHEY_COMPLEX
    # img = cv2.blur(img,(10,10))
    (thresh, img_bin) = cv2.threshold(img, 128, 255,
                                      cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # Thresholding the image
    img_bin = 255-img_bin  # Invert the image

 
    img = cv2.blur(img,(20,20))

    kernel_length = np.array(img).shape[1]//400

    verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
    hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=3)
    verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=3)

    img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=3)
    horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=3)

    alpha = 0.50
    beta = 1.0 - alpha
    img_final_bin = cv2.addWeighted(verticle_lines_img, alpha, horizontal_lines_img, beta, 0.0)
    img_final_bin = cv2.erode(~img_final_bin, kernel, iterations=2)
    (thresh, img_final_bin) = cv2.threshold(img_final_bin, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    contours, hierarchy = cv2.findContours(
        img_final_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    (contours, boundingBoxes) = sort_contours(contours, method="left-to-right")

    x1=0
    y1=0
    # check=0
    idx = 0
    for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            # check+=1



            # if ((x==x1)):

            if(cv2.contourArea(c)>30000):
            # if ((x>(x1+100))): #outer
                if (w > 300 and h > 400 and((h<(6*w))and(h>(0.3*w)))):
                    if ((x<(x1+100))): #inner
                        idx += 1


                        itr=0

                        approx = cv2.approxPolyDP(c, 0.009 * cv2.arcLength(c, True), True)

                        cv2.drawContours(img3, [approx], 0, (0, 0, 255), 5)
                        
                        nq = approx.ravel()
                        #print(nq)
                        iq = 0

                        for jq in nq :
                            if(iq % 2 == 0):
                                xq = nq[iq]
                                yq = nq[iq + 1]

                                string = str(xq) + " " + str(yq)


                                cv2.putText(img3, string, (xq, yq),
                                font, 0.5, (255, 255, 0))

                                if(itr==1):
                                    extTop=[xq,yq]
                                if(itr==2):
                                    extRight=[xq,yq]
                                if(itr==3):
                                    extBot=[xq,yq]
                                if(itr==0):
                                    extLeft=[xq,yq]

                                itr = itr + 1

                            iq = iq + 1

                        coords=[extTop,extRight,extBot,extLeft]
                        sum0=coords[0][0]+coords[0][1]
                        sum1=coords[1][0]+coords[1][1]
                        sum2=coords[2][0]+coords[2][1]
                        sum3=coords[3][0]+coords[3][1]
                        dif0=coords[0][0]-coords[0][1]
                        dif1=coords[1][0]-coords[1][1]
                        dif2=coords[2][0]-coords[2][1]
                        dif3=coords[3][0]-coords[3][1]
                        smin=min(sum0,sum1,sum2,sum3)
                        smax=max(sum0,sum1,sum2,sum3)
                        dmin=min(dif0,dif1,dif2,dif3)
                        dmax=max(dif0,dif1,dif2,dif3)
                        if smin==sum0:
                            tl=[coords[0][0],coords[0][1]]
                        elif smin==sum1:
                            tl=[coords[1][0],coords[1][1]]
                        elif smin==sum2:
                            tl=[coords[2][0],coords[2][1]]
                        elif smin==sum3:
                            tl=[coords[3][0],coords[3][1]]
                        #print(tl)
                        if smax==sum0:
                            br=[coords[0][0],coords[0][1]]
                        elif smax==sum1:
                            br=[coords[1][0],coords[1][1]]
                        elif smax==sum2:
                            br=[coords[2][0],coords[2][1]]
                        elif smax==sum3:
                            br=[coords[3][0],coords[3][1]]
                        #print(br)
                        if dmin==dif0:
                            bl=[coords[0][0],coords[0][1]]
                        elif dmin==dif1:
                            bl=[coords[1][0],coords[1][1]]
                        elif dmin==dif2:
                            bl=[coords[2][0],coords[2][1]]
                        elif dmin==dif3:
                            bl=[coords[3][0],coords[3][1]]
                        #print(bl)
                        if dmax==dif0:
                            tr=[coords[0][0],coords[0][1]]
                        elif dmax==dif1:
                            tr=[coords[1][0],coords[1][1]]
                        elif dmax==dif2:
                            tr=[coords[2][0],coords[2][1]]
                        elif dmax==dif3:
                            tr=[coords[3][0],coords[3][1]]
                        #print(tr)
                        rect=[tl,tr,bl,br]

                        return rect


                        print (coords)

                        x1=x #inner




if __name__ == '__main__':

	app.run(debug = True)
