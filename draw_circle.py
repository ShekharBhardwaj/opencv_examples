import cv2
import numpy as np

image = np.eye(512)

cv2.circle(image, (350, 350), 100, (15, 75, 50), -1)

cv2.imshow('circle', image)
cv2.waitKey(5000)
cv2.destroyAllWindows()
