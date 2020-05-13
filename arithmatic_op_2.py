import cv2
import numpy as np

# create a square on an image
# black image for square to be drawn on
square = np.zeros((300, 300), np.uint8)
cv2.rectangle(square, (50, 50), (250, 250), 255, -2)
#cv2.imshow("square", square)


# create a elipse
# black image for ellipse to be drawn on
elipse = np.zeros((300, 300), np.uint8)
cv2.ellipse(elipse, (150, 150), (150, 150), 30, 0, 180, 255, -1)

# bit wise

And = cv2.bitwise_and(square, elipse)
cv2.imshow('And', And)

Or = cv2.bitwise_or(square, elipse)
cv2.imshow('Or', Or)

Xor = cv2.bitwise_xor(square, elipse)
cv2.imshow('Xor', Xor)

Not = cv2.bitwise_not(elipse)
cv2.imshow('Not', Not)

cv2.waitKey(20000)
cv2.destroyAllWindows()
