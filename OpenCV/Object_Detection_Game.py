import keyboard
import mss
import cv2
import numpy
from time import time, sleep
import pyautogui

pyautogui.PAUSE = 0

print("Press 'w' to start playing.")
print("Once started press 'q' to quit.")
keyboard.wait('w')

sct = mss.mss()
x, y = pyautogui.position()
width, height = 200, 200

dimensions = {
    'left': 860,
    'top': 100,
    'width': 200,
    'height': 200
}
monitor = {
    "top": y - height // 2,
    "left": x - width // 2,
    "width": width,
    "height": height
}

target = cv2.imread('a2.png')
w = target.shape[1]
h = target.shape[0]

fps_time = time()
while True:
    scr = numpy.array(sct.grab(monitor))

    with mss.mss() as sct:
        sct_img = sct.grab(monitor)
    img = numpy.array(sct_img)
    cv2.imshow("Screenshot", img)

    # Cut off alphaq
    scr_remove = scr[:,:,:3]

    result = cv2.matchTemplate(scr_remove, target, cv2.TM_CCOEFF_NORMED)
    
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    print(f"Max Val: {max_val} Max Loc: {max_loc}")
    
    if max_val > 0.35:
        pyautogui.press('space')
        print("SPACE PRESSED")

    sleep(.10)
    if keyboard.is_pressed('q'):
        break

    print('FPS: {}'.format(1 / (time() - fps_time)))
    fps_time = time()