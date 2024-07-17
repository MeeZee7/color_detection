import cv2 
print(cv2.__version__)

cap= cv2.VideoCapture(0)
#in a while loop to make it stay 
while True:
    _,frame=cap.read()
    hsv_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#for creating an hsv frame
    height, width, _ = frame.shape

    cx=int(width/2)
    cy=int(height/2)

    #pick pixel value 
    pixel_center= hsv_frame[cy,cx]
    hue_value= pixel_center[0]

    color = "Undefined"
    if hue_value<5:
        color="RED"
    elif hue_value<22:
        color="ORANGE"
    elif hue_value<33:
        color="YELLOW"
    elif hue_value<78:
        color="GREEN"
    elif hue_value<131:
        color="BLUE"
    elif hue_value<170:
        color="VIOLET"
    else:
        color= "RED"

    print(pixel_center)
    pixel_center_BGR=frame[cy,cx]
    b,g,r= int(pixel_center_BGR[0]), int(pixel_center_BGR[1]), int(pixel_center_BGR[2])
    cv2.putText(frame, color, (10,70), 3,1,(b,g,r),2)
    cv2.circle(frame,(cx,cy),5,(25,25,25),3)

    


    cv2.imshow("Frame",frame)


    key=cv2.waitKey(1)
    if key==27:
        break
cap.release()