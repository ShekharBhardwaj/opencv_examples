import numpy as np
import cv2 as cv

events = [i for i in dir(cv) if 'EVENT' in i]
print(events)

def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(f'{x}, {y}')
        strXY = f'{x}, {y}'
        font = cv.FONT_HERSHEY_COMPLEX
        cv.putText(img, strXY, (x, y), font, .3, (255, 255, 0), 1)
        cv.imshow("mouseEvent", img)

img = np.zeros((512, 512, 3), np.uint8)
cv.imshow('mouseEvent', img)

cv.setMouseCallback('mouseEvent', click_event)

cv.waitKey(0)
cv.destroyAllWindows()
