import cv2 as cv
import numpy as np

img = cv.imread('gradient.png', 0)

cv.imshow("img", img)

_, thresh_hold1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, thresh_hold2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)

cv.imshow("thresh_hold1", thresh_hold1)
cv.imshow("thresh_hold2", thresh_hold2)
cv.waitKey(0)

cv.destroyAllWindows()
