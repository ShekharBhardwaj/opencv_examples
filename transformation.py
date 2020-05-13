import cv2
import numpy as np

image = cv2.imread('input.jpg')

print(image)

cv2.imshow('Real', image)
print(type(image))
height, width = image.shape[:2]

# Shift in image psotion
quarter_h, quarter_w = height / 4, width / 4

#       | 1  0  Tx |
# T =   | 0  1  Ty |

# T is our Transalation matrix
T = np.float32([[1, 0, quarter_h], [0, 1, quarter_w]])

# cv2.waroAffine to translate the image using translation matrix T
#(image, translation matrix, (current height and width => w, h)
img_translation = cv2.warpAffine(image, T, (width, height))
cv2.imshow('Transalation', img_translation)
cv2.waitKey(20000)
cv2.destroyAllWindows()
