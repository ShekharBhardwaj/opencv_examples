import cv2
import numpy as np

image = cv2.imread("brazil.jpg")
cv2.imshow("Original", image)


kernel_3x3 = np.ones((3, 3), np.float32) / 9
blurred_3x3 = cv2.filter2D(image, -1, kernel_3x3)
cv2.imshow("blurred_3x3", blurred_3x3)

kernel_7x7 = np.ones((7, 7), np.float32) / 49
blurred_7x7 = cv2.filter2D(image, -1, kernel_7x7)
cv2.imshow("blurred_7x7", blurred_7x7)

gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow("gaussian", gaussian)

median = cv2.medianBlur(image, 9)
cv2.imshow("medianBlur", median)

bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('bilateral', bilateral)

fastMeanDenoising = cv2.fastNlMeansDenoisingColored(image, None, 6, 6, 7, 21)
cv2.imshow('fastMeanDenoising', fastMeanDenoising)


cv2.waitKey(20000)
cv2.destroyAllWindows()
