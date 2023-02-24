import cv2
import threading
import time


def webcam_capture_display(webcam_dev):
    print("Preparing webcam[{}] . . . . ".format(webcam_dev))
    webcam = cv2.VideoCapture(webcam_dev)
    # check webcam
    ret, vframe = webcam.read()
    if ret == False:
        print("Error in reading webcam[{}]".format(webcam_dev))
        return
    else:
        print("Webcam[{}] is correctly working now ...".format(webcam_dev))
        fr_width, fr_height = webcam.get(3), webcam.get(4)
        fps = webcam.get(cv2.CAP_PROP_FPS)
        print("Webcam cam frame width ({}), height({})".format(fr_width, fr_height))
        print(" frame-per-sec = {}".format(fps))
        print("Enter ESC to quit")
    while True:
        ret, vframe = webcam.read()
        if ret == False:
            continue
        resized_fr = cv2.resize(vframe, (int(vframe.shape[1]/2), int(vframe.shape[0]/2)))
        cv2.imshow('Webcam[{}]'.format(webcam_dev), resized_fr)
        key = cv2.waitKey(1)
        if key == 27: # if ESC key is input, then exit
            break
        time.sleep(0.1)


if __name__ == "__main__":
    webcam_no = int(input("Input webcam No (0 or 1) : "))
    print('Starting webcam_capture_dispaly')
    thrd_webcamCapDisp = threading.Thread(target=webcam_capture_display, args=(webcam_no,))
    thrd_webcamCapDisp.start()
    thrd_webcamCapDisp.join()