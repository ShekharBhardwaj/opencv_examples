import cv2
import numpy as np

image = cv2.imread("brazil.jpg")
cv2.imshow("original", image)
# sobel
sobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)

cv2.imshow("sobel_x", sobel_x)
cv2.imshow("sobel_y", sobel_y)

sobel_OR = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow("sobel_OR", sobel_OR)
# laplacian
laplacian = cv2.Laplacian(image, cv2.CV_64F)
cv2.imshow("laplacian", laplacian)

# Canny
canny = cv2.Canny(image, 20, 170)
cv2.imshow('canny', canny)

cv2.waitKey(30000)
cv2.destroyAllWindows()
