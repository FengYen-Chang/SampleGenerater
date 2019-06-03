import cv2
import numpy as np
import argparse

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def parsing():
    parser = argparse.ArgumentParser(add_help = False)
    parser.add_argument('-d', '--device', default='ipcam', type=str)
    parser.add_argument('-m', '--mode', default='press', type=str)

    return parser

def main() :
    args = parsing().parse_args()

    dir = './data/%04d.jpg'
    i = 0

    if (args.device == 'ipcam') :
        cap = cv2.VideoCapture("rtsp://admin:admin@192.168.0.12:8554/CH001.sdp")
    else :
        cap = cv2.VideoCapture(0)

    while(True):
        _, frame = cap.read()
        cv2.imshow("img", frame)

        if (args.mode == 'press') :
            k = cv2.waitKey(1)
            if k == 66 or k == 99:  # C or c
                cv2.imwrite(dir%(i), frame)
                i += 1

        if k ==  27:
            break

    cap.release()
    cv2.destroyAllWindows()

if "__main__":
    main()

