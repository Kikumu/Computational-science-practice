import time 
import cv2
from picamera import PiCamera
import matplotlib.pyplot as plt
import numpy as np
from picamera.array import PiRGBArray
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) #easiest numbering 1,2,3,4...    

#line midpoint
def acquire_midpoint(var1,var2,var3,var4):
	x = ((var1 + var3)/2)
	y = ((var2 + var4)/2)
	return x,y

#line gradient
def acquire_slope(var1,var2,var3,var4):
	grad = (var2-var4)/(var1 - var3)
	return grad
	
#remember has to be in the form of a numpy array
def vct_sub(a,b):
	val=b-a
	return val
	
#remember has to be in the form of a numpy array
def cross_vct(a,b):
	res = np.cross(a, b)
	magnitude = res[0]**2 + res[1]**2 + res[2]**2
	return res,magnitude

def  distance_between_skew_lines(var1,var2,var3,var4,var5,var6,var7,var8):
	v1 = np.array([var1,var2,0])
	v2 = np.array([var3,var4,0])
	v3 = np.array([var5,var6,0])
	v4 = np.array([var7,var8,0])
	sub_res1 = vct_sub(v1,v2)
	sub_res2 = vct_sub(v3,v4)
	crs_product,magnitude = cross_vct(sub_res1,sub_res2)
	a = sub_res1[0]
	b = sub_res2[0]
	c = crs_product[0]
	d = sub_res1[1]
	e = sub_res2[1]
	f = crs_product[1]
	g = sub_res1[2]
	h = sub_res2[2]
	i = crs_product[2]
	a = np.array([[a,-b,-c],[d,-e,-f],[g,-h,-i]])
	b = np.array([(var5-var1),(var6-var2),(-0 + 0)])
	coeff_array = np.linalg.solve(a,b)
	constant = coeff_array[2]
	resultant = constant*magnitude
	#d_1  = k(magnitude)
	return resultant
	
def subtract_x_axis(var2,var4,var):
	result = var4-var2
	return result,var
	
def hsv_color_space(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("L-H","Trackbar")
    l_s = cv2.getTrackbarPos("L-S","Trackbar")
    l_v = cv2.getTrackbarPos("L-V","Trackbar")
    u_h = cv2.getTrackbarPos("U-H","Trackbar")
    u_s = cv2.getTrackbarPos("U-S","Trackbar")
    u_v = cv2.getTrackbarPos("U-V","Trackbar")
    lower_red = np.array([l_h,l_s,l_v])
    upper_red = np.array([u_h,u_s,u_v])
    mask = cv2.inRange(hsv,lower_red,upper_red)
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.erode(mask,kernel)
    #contours
    A,contours,C = cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #image = draw_lines(image,scrn_x,scrn_y)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt,True),True)
        if area > 400:
          cv2.drawContours(image,[approx],0,(0,0,0),5)
            #scene/"shape" detector
          if(len(approx)==4):
            cv2.putText(image, "rectangle",(10,10),font,1,(0,0,0))
          elif(len(approx)==3):
            cv2.putText(image, "triangle",(10,10),font,1,(0,0,0))
          elif(len(approx)==10):
            cv2.putText(image, "10sides",(10,10),font,1,(0,0,0))
          elif(len(approx)==5):
            cv2.putText(image, "5sides",(10,10),font,1,(0,0,0))
          elif(len(approx)==7):
            cv2.putText(image, "7sven",(10,10),font,1,(0,0,0))
          elif(len(approx)==8):
            cv2.putText(image, "ate",(10,10),font,1,(0,0,0))
    return image,mask
	

def longest_line(var1,var2,var3,var4):
	line_length =  ((var1 - var3)**2 + (var2 - var4)**2)**1/2
	return line_length
def region_of_interest(width,height):
    vertices = [(0,height),(0,300),(width/2,300),(width,300),(width,height)]
    return vertices
    
def ROI_mask(image,vertices):
    mask = np.zeros_like(image)
    channel_count = image.shape[2]
    match_mask = (255,)*channel_count
    cv2.fillPoly(mask,vertices,match_mask)
    masked_img = cv2.bitwise_and(image,mask)
    return masked_img
    
def draw_lines(img,mid_x,mid_y):
    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hsv =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #cv2.imshow("hsv",hsv)
    #cv2.waitKey()
    low_yellow = np.array([119,45,0])
    up_yellow = np.array([180,110,217])
    mask = cv2.inRange(hsv,low_yellow,up_yellow)
    kernel = np.ones((6,6),np.uint8)
    mask = cv2.erode(mask,kernel)
    cv2.imshow("mask1",mask)
    #cv2.waitKey()
    edges = cv2.Canny(mask,threshold1=200,threshold2=300)
    cv2.imshow("edges",edges)
    #cv2.waitKey()
    lines = cv2.HoughLinesP(edges,1,np.pi/180,20,maxLineGap=50)
    #cv2.imshow("lines",lines)
    #cv2.waitKey()
    img = cv2.circle(img,(mid_x,mid_y),10,(0,0,0),-1) #draws circle in the middle(used to steer)
    if lines  is not None:
      for line in lines:
        coord = line[0]   #grab line
        cv2.line(img,(coord[0],coord[1]),(coord[2],coord[3]),(255,0,255),2)
        p1,p2 = acquire_midpoint(coord[0],coord[1],coord[2],coord[3]) #obtain midpoint
        gradient = acquire_slope(coord[0],coord[1],coord[2],coord[3]) #obtain gradient
        if(gradient > 0):
            img = cv2.circle(img,(int(p1),int(p2)),10,(0,255,0),-1)
            print(p1,"right")
            print(mid_x-p1,"distance right")
        elif(gradient < 0):
            img = cv2.circle(img,(int(p1),int(p2)),10,(255,255,255),-1)
            print(p1,"left")
            print(mid_x-p1,"distance left")
        else:
            print(gradient)	
    return img

def nothing(X):
	pass
	

#template setup
camera = PiCamera()
camera.resolution = (640,480)
camera.vflip = True
camera.framerate = 20
rawCapture = PiRGBArray(camera, size = (640,480))
time.sleep(0.1)
scrn_x = int(640*0.5)
scrn_y = int((480*0.5) + 100)
cv2.namedWindow("Trackbar")
cv2.createTrackbar("L-H","Trackbar",0,180, nothing)
cv2.createTrackbar("L-S","Trackbar",80,255, nothing)
cv2.createTrackbar("L-V","Trackbar",129,180, nothing)
cv2.createTrackbar("U-H","Trackbar",180,180, nothing)
cv2.createTrackbar("U-S","Trackbar",255,255, nothing)
cv2.createTrackbar("U-V","Trackbar",240,255, nothing)
font = cv2.FONT_HERSHEY_COMPLEX

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    #---------------------------------SHAPE-----------------------------------------------
    
    #---------------------------------LINES--------------------------
    #image = draw_lines(image,scrn_x,scrn_y)
    vertices = region_of_interest(640,480) # create roi skeleton
    cropped = ROI_mask(image,np.array([vertices],np.int32),) #create cropped image usiing roi
    cropped = draw_lines(cropped,scrn_x,scrn_y) #draw lines on cropped image and pass as new image to display
    
    
    image,mask = hsv_color_space(image) # shape
    cv2.imshow("Frame", cropped)
    cv2.imshow("Mask",mask)
    key = cv2.waitKey(1)&0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

