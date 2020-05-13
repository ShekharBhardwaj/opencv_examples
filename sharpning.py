import cv2
import numpy as np

image = cv2.imread("brazil.jpg")

kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])

sharpened = cv2.filter2D(image, -1, kernel=kernel)
cv2.imshow("sharpened", sharpened)
cv2.waitKey(20000)
cv2.destroyAllWindows()

