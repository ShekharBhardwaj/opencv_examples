import cv2
import numpy as np


img = cv2.imread("input.jpg")

M = np.ones(img.shape, dtype="uint8") * 75


added = cv2.add(img, M)
cv2.imshow('Added', added)

subtracted = cv2.subtract(img, M)
cv2.imshow('Subtract', subtracted)

cv2.waitKey(20000)
cv2.destroyAllWindows()
