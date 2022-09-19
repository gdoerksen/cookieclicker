from PIL import ImageGrab
from functools import partial
from time import time, sleep
import cv2 
import numpy as np
import pyautogui
pyautogui.FAILSAFE = True

from cookieclicker.utilities import printMousePositionLive



def windowCaptureRealtime():
    loop_time = time()
    while(True):
        
        screenshot = ImageGrab.grab()
        # screenshot = windowCapture()
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        cv2.imshow('Computer Vision', screenshot)
        print('FPS {}'.format( 1 / (time() - loop_time)))
        loop_time = time()

        # press q to quit
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            break



class Clicker:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.click = partial(pyautogui.click, x=self.x, y=self.y)

    def click(self):
        pyautogui.click(x=self.x, y=self.y, button='left')

    def click_n_times(self, n):
        for i in range(n):
            self.click() 

    def click_forever(self):
        print('Press Ctrl-C to quit.')
        try:
            while True:
                self.click()
        except KeyboardInterrupt:
            print('\n')



if __name__ == '__main__':
    pyautogui.PAUSE = 0.05

    # redefine the ImageGrab.grab function to use just my second monitor
    first_monitor_width = 3440
    first_monitor_height = 1440
    second_monitor = (first_monitor_width, 0, first_monitor_width+1920, 1080)

    ImageGrab.grab = partial(ImageGrab.grab, bbox=second_monitor, all_screens=True)

    # printMousePositionLive()

    # windowCaptureRealtime()
    cookieClicker = Clicker(3728, 432)
    # cookieClicker.click_n_times(100)
    cookieClicker.click_forever()



"""
We want to optimize and maximally increase the rate of cookie production



Thousand fingers adds 0.1 cps gain per non-cursor building owned 

* state
    * current cookies
    * current cps
    * cps per building
    * number of each building




* get all possible actions 
    * click the cookie
    * buy a building
    * buy an upgrade
    * click a golden cookie

* prune actions that are infeasible (not enough cookies)

* select the best action
    * maximize the increase in cookies per second divided by the cost of the action

"""