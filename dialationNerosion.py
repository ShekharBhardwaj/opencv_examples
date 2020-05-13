import cv2
import numpy as np

try:
    image = cv2.imread("opencv_inv.png")
    cv2.imshow("Original", image)

    kernel = np.ones((5, 5))
    # erosion
    erosion = cv2.erode(image, kernel, iterations=1)
    cv2.imshow("erosion", erosion)
    # dialation
    dialation = cv2.dilate(image, kernel, iterations=1)
    cv2.imshow("dialation", dialation)
    # opening
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    cv2.imshow("opening", opening)
    # closing
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("closing", closing)
    cv2.waitKey(20000)
except Exception as e:
    print(e.message)
finally:
    cv2.destroyAllWindows()
