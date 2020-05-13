# imports
import cv2
import numpy as np


def sketch(image):
    try:
        # convert image to grey
        img_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # apply gaussian blur
        g_blurr = cv2.GaussianBlur(img_grey, (5, 5), 0)

        # apply canny edges
        can_edges = cv2.Canny(g_blurr, 10, 70)

        # do the binary inverse
        ret, mask = cv2.threshold(can_edges, 70, 255, cv2.THRESH_BINARY_INV)
        return mask
    except Exception as e:
        print(e.message)


# initilize video camera
try:
    print("Starting the cam...")
    cam = cv2.VideoCapture(0)
    print("Cam started...")
    # while loop break by return key
    while True:
        print("Reading the frames from cam capture.")
        ret, frame = cam.read()
        cv2.imshow("Liv!", sketch(frame))
        print("Live feed On")
        if cv2.waitKey(1) == 13:
            break
except Exception as e:
    print(e.message)

finally:
    cv2.destroyAllWindows()
