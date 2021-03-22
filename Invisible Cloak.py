import cv2
import numpy as np

cap = cv2.VideoCapture(0)

camimage = cv2.imread("Image.jpg")

while cap.isOpened():
    ret,cam_reading = cap.read()
    if ret:
        hsv =cv2.cvtColor(cam_reading,cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv",hsv)
        # NOW TO GET THE HSV VALUE??
        #LOWER : hue - 10,100,100 ,higher: h+10,255,255
        red = np.uint8([[[0,0,255]]])
        hsv_red =cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
        #print(hsv_red)
        l_red = np.array([0,100,100])
        u_red = np.array([10,255,255])

        mask = cv2.inRange(hsv, l_red, u_red)
        #cv2.imshow("mask", mask)

        part1 = cv2.bitwise_and(camimage, camimage, mask=mask)
        #cv2.imshow("part1", part1)

        mask = cv2.bitwise_not(mask)

        part2 = cv2.bitwise_and(cam_reading , cam_reading , mask=mask)
        #cv2.imshow("mask", part2)

        cv2.imshow("cloak",part1 +part2)



        if cv2.waitKey(5) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()


