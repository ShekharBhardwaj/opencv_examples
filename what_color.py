import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img [x, y, 1]
        red = img [x, y, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        my_color_image = np.zeros((2000, 2000, 3), np.uint8)
        my_color_image[:] = [blue, green, red]
        cv2.imshow("color", my_color_image)



img = cv2.imread('test_1.jpeg')
print(img.shape)
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()