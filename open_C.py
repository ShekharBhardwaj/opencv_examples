import cv2
import numpy as np


input = cv2.imread('input.jpg')

grey_scale = cv2.cvtColor(input, cv2.COLOR_RGB2GRAY)

cv2.imshow('grayScaled', grey_scale)

cv2.waitKey(5000)

# print(input.shape)
# print(input.shape[0])
# print(input.shape[1])


# cv2.imshow('Hello World', input)

# cv2.waitKey(10000)
cv2.destroyAllWindows()
