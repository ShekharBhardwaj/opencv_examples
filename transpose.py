import cv2
import numpy as np

img = cv2.imread("input.jpg")

transpose_img = cv2.transpose(img)
# x, y = img.shape[:2]

# rotation_matrix = cv2.getRotationMatrix2D((y / 2, x / 2), 90, 1)

# rotated_img = cv2.warpAffine(img, rotation_matrix, (x, y))

cv2.imshow('rotated_img', transpose_img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
