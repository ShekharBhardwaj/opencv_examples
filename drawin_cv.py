import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)

image1 = np.zeros((512, 512), np.uint8)

cv2.rectangle(image, (100, 100), (250, 250), (127, 50, 127), -1)

cv2.imshow('3Layer', image)


cv2.waitKey(5000)

cv2.destroyAllWindows()
