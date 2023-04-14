import mss
import pyautogui
import cv2
import numpy

# Set the dimensions of the area you want to capture around the mouse cursor
width, height = 100, 100

while True:
    # Get the current position of the mouse cursor
    x, y = pyautogui.position()

    # Define the region around the cursor to capture
    monitor = {
        "top": y - height // 2,
        "left": x - width // 2,
        "width": width,
        "height": height
    }

    # Take a screenshot of the defined region
    with mss.mss() as sct:
        sct_img = sct.grab(monitor)

    # Convert the screenshot to a numpy array and show it
    img = numpy.array(sct_img)
    cv2.imshow("Screenshot", img)

    # Check if left mouse button is clicked
    if pyautogui.mouseInfo()[2][0]:
        # Print the current mouse coordinates
        print(f"Mouse Position: ({x}, {y})")

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break 

cv2.destroyAllWindows()



# 1260 677 
# 1800 853 = 540 176q