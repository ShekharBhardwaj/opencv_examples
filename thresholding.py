import cv2
import numpy as np


image = cv2.imread("gradient.jpg")
cv2.imshow("original", image)

ret, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
print(type(ret), ret)
cv2.imshow("binary", binary)

cv2.waitKey(20000)
cv2.destroyAllWindows()
