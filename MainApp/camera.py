import cv2
import os
import datetime

cap = None  # Global variable to hold the camera capture object

def save_frame_camera_cycle(device_num, dir_path, basename, cycle, ext='jpg', delay=1, window_name='frame'):
    global cap
    cap = cv2.VideoCapture(device_num)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    while True:
        should_break = False
        for _ in range(cycle):
            ret, frame = cap.read()
            cv2.imshow(window_name, frame)
            if cv2.waitKey(delay) & 0xFF == ord('q'):
                should_break = True
                break
        if should_break:
            break
        cv2.imwrite('{}_{}.{}'.format(base_path, "default", ext), frame)

    cap.release()
    cv2.destroyAllWindows()

def release_camera():
    global cap
    if cap is not None:
        cap.release()
