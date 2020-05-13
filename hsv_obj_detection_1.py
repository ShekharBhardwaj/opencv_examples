import cv2 as cv
import numpy as np

def nothing(x):
    pass


#cv.namedWindow("Tracking")



while True:
    frame = cv.imread('smarties.png')
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # lower hue, saturation and value


    # lower boundary and upper boundary
    # change these values to mask and unmask the color using bitwise and
    l_b = np.array([150, 50, 50])
    u_b = np.array([130, 255, 255])

    mask = cv.inRange(hsv, l_b, u_b)

    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    key = cv.waitKey(1)
    if key == 27:
        break

cv.destroyAllWindows()