import cv2
import numpy as np

image = cv2.imread("input.jpg")

B, G, R = cv2.split(image)

# cv2.imshow('Red', B)
# cv2.waitKey(5000)
# cv2.destroyAllWindows()
# cv2.imshow('Red', G)
# cv2.waitKey(5000)
# cv2.destroyAllWindows()
# cv2.imshow('Red', R)
# cv2.waitKey(5000)
# cv2.destroyAllWindows()
merged = cv2.merge([B + 100, G, R])
cv2.imshow('merged', merged)
cv2.waitKey(5000)
cv2.destroyAllWindows()

print(B.shape)
