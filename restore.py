import cv2
import numpy as np


def loadOrginal(path):
    try:
        print('Loading the image as np array')
        original = cv2.imread(path)
        return original
    except Exception as e:
        print(f'Error occured: {e}')
        print('Caused by:', e)


def showImage(image_name, np_arr):
    try:
        print(f'Displaying the image: {image_name}')
        cv2.imshow(image_name, np_arr)
    except Exception as e:
        print(f'Error occured: {e}')
        print('Caused by:', e)


def applyErosion(image_name, np_arr):
    kernel = np.ones((5, 5), np.uint8)
    try:
        print(f'Applying Erosion on {image_name}')
        restored = cv2.erode(np_arr, kernel=kernel, iterations=1)
        return restored
    except Exception as e:
        print(f'Error occured: {e}')
        print('Caused by:', e)


def applyDialation(image_name, np_arr):
    kernel = np.ones((5, 5), np.uint8)
    try:
        print(f'Applying Dialation on {image_name}')
        restored = cv2.dilate(np_arr, kernel=kernel, iterations=1)
        return restored
    except Exception as e:
        print(f'Error occured: {e}')
        print('Caused by:', e)


def applySharpening(image_name, np_arr):
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    try:
        print(f'Applying shapening on {image_name}')
        sharpened = cv2.filter2D(np_arr, -1, kernel=kernel)
        return sharpened
    except Exception as e:
        print(f'Error occured: {e}')
        print('Caused by:', e)


def wait_n_destroy(waitTime):
    try:
        finish = False
        if waitTime is None:
            print('Keyboard interruption opted')
            while not finish:
                if cv2.waitKey(1) == 13:
                    break
        else:
            print(f'Wait time {waitTime}ms opted')
            cv2.waitKey(waitTime)
    except Exception as e:
        print(f'Error occured: {e}')
        print('Caused by:', e)
    finally:
        print("Finally ran to remove all the lurking images")
        cv2.destroyAllWindows()


if __name__ == "__main__":
    path = "07.jpg"
    original = loadOrginal(path)
    showImage("original", original)
    sharpened = applySharpening("original", original)
    showImage("sharpened", sharpened)
    erosed = applyErosion('sharpened', sharpened)
    showImage("erosion", erosed)
    dialted = applyDialation("erosed", erosed)
    showImage("dialted", dialted)
    wait_n_destroy(None)
