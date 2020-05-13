import cv2
import numpy as np

image = np.zeros((3000, 3000, 3), dtype=np.uint8)
image = cv2.arrowedLine(image, (0, 0), (255, 255), (0, 0, 255), 3)
image = cv2.rectangle(image, (30, 30), (100, 100), (0, 0, 255), 3)
image = cv2.circle(image, (100, 100), 50, (0, 0, 255), -1)
image = cv2.putText(image, 'Hello World!',(300,300), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 10, cv2.LINE_4)
cv2.imshow("xvz", image)
cv2.waitKey(10000)
cv2.destroyAllWindows()

