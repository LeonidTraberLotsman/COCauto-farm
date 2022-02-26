import cv2 as cv2
import numpy as np
import time

file_path='D:\\Unity\\Repos\\COCauto-farm\\'

def CheckResources():
    time.sleep(2)
    #screen=pg.screenshot()
    screen=cv2.imread(file_path+'example.png')
    y=150
    h=200
    x=100
    w=314
    img = screen[y:h, x:w]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #---------------
    hsv_min = np.array((0, 125, 0), np.uint8)
    hsv_max = np.array((255, 255, 255), np.uint8)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)
    cv2.imshow("thresh", thresh)
    #---------------
    #ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
    img_erode = cv2.erode(thresh, np.ones((3, 3), np.uint8), iterations=1)

# Get contours
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    output = img.copy()

    for idx, contour in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(contour)
    # print("R", idx, x, y, w, h, cv2.contourArea(contour), hierarchy[0][idx])
    # hierarchy[i][0]: the index of the next contour of the same level
    # hierarchy[i][1]: the index of the previous contour of the same level
    # hierarchy[i][2]: the index of the first child
    # hierarchy[i][3]: the index of the parent
        if hierarchy[0][idx][3] == 0:
            cv2.rectangle(output, (x, y), (x + w, y + h), (255, 0, 0), 1)


    
    cv2.imshow("Enlarged", img_erode)
    cv2.imshow("Output", output)
    cv2.waitKey(0)



CheckResources()