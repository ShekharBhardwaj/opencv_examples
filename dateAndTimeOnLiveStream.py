import cv2 as cv
from datetime import datetime as dt

def capture_video(src=0, frame_rate=None):
    """
    :param frame_rate:
    :param src:
    :return: cv2.VideoCapture
    """
    print('Starting the Vid capture.')
    if frame_rate is None:
        frame_rate = {'3': 640, '4': 480}
    try:
        if src is 0:
            print('Source is 0')
            cap_vid = cv.VideoCapture(0)
            # cap_vid.set(3, frame_rate['3'])
            # cap_vid.set(4, frame_rate['4'])
            return cap_vid
        else:
            print(f'Source is {src}')
            cap_vid = cv.VideoCapture(src)
            # cap_vid.set(3, frame_rate['3'])
            # cap_vid.set(4, frame_rate['4'])
            return cap_vid
    except Exception as e:
        print(f'Error while init, Vid capture: {e.message}')
        print(e)


def apply_gray_filter(src):
    try:
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
        return gray
    except Exception as e:
        print(f'Error while applying Gray on the frames:{e.message}')
        print(e)


def display_the_frames(cap_vid, win_name='default'):
    try:
        print('Starting the Vid stream.')
        while cap_vid.isOpened():
            ret, frame = cap_vid.read()
            if ret:
                date_time = str(dt.now())
                font = cv.FONT_HERSHEY_COMPLEX
                #gray = apply_gray_filter(frame)
                cv.putText(frame, date_time, (10, 50), font, 1, (0, 255, 255), 2, cv.LINE_AA)
                cv.imshow(win_name, frame)
                k = cv.waitKey(1) & 0xFF
                print(f"User input k: {k}")
                if k == ord("q"):
                    print('Interrupting the Vid stream.')
                    break
            else:
                print(f'Error: Frame not found, stopping the Vid stream, ret is {ret}')
                break
    except Exception as e:
        print(f'Error occured while displaying the Vid Capture: {e.message}')
        print(e)
    finally:
        print('Releasing the cap and destroying all the windows')
        cap_vid.release()
        cv.destroyAllWindows()
        print('Done.')


if __name__ == "__main__":
    cap = capture_video()
    display_the_frames(cap, "newStream")
