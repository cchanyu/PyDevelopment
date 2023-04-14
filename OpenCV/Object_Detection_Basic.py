# pip install opencv-python
# pip install mss
import keyboard
import mss
import cv2
import numpy as np
from time import time, sleep
import pyautogui

def main():

    print("Press 's' to start playing.")
    print("Once started press 'q' to quit.")
    keyboard.wait('s')

    source_img = cv2.imread('source_img.png', cv2.IMREAD_UNCHANGED)
    target_img = cv2.imread('target_img.png', cv2.IMREAD_UNCHANGED)

    cv2.imshow('Source_img', source_img)
    cv2.waitKey()
    cv2.destroyAllWindows()

    cv2.imshow('Target_img', target_img)
    cv2.waitKey()
    cv2.destroyAllWindows()

    result = cv2.matchTemplate(source_img, target_img, cv2.TM_CCOEFF_NORMED)

    # a heat map of where the best matches are
    cv2.imshow('Result', result)
    cv2.waitKey()
    cv2.destroyAllWindows()

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    max_loc # x, y coord in source_img of the best match to target_img
    max_val # how much source_img object % it matches to the target

    # width and height to get the exact location of matching target
    w = target_img.shape[1]
    h = target_img.shape[0]
    cv2.rectangle(source_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)

    threshold = 60
    yloc, xloc = np.where(result >= threshold)
    len(xloc) # shows the # of matching locations

    for (x, y) in zip(xloc, yloc):
          cv2.rectangle(source_img, (x, y), (x + w, y + h), (0,255,255), 2)

    rectangles = []
    for (x, y) in zip(xloc, yloc):
          rectangles.append([int(x), int(y), int(w), int(h)])
          rectangles.append([int(x), int(y), int(w), int(h)])

    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

    for (x, y, w, h) in rectangles:
        cv2.rectangle(source_img, (x, y), (x + w, y + h), (0,255,255), 2)

    pyautogui.moveTo(x, y)
    pyautogui.click()
    

if __name__ == "__main__":
	main()