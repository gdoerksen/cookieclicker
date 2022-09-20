from PIL import ImageGrab
from functools import partial
from time import time, sleep
import cv2 
import numpy as np
import json
import pyautogui
from pathlib import Path
pyautogui.FAILSAFE = True

from cookieclicker.utilities import printMousePositionLive

from cookieclicker.building import Building


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

class NiaveAgent:
    def __init__(self):
        self.cookieClicker = Clicker(3728, 432)

        self.BuildingList = []
        self.building_x = 5200
        self.cursorClicker = Clicker(self.building_x, 191)
        self.grandmaClicker = Clicker(self.building_x, 264)
        self.farmClicker = Clicker(self.building_x, 324)
        self.mineClicker = Clicker(self.building_x, 389)
        self.factoryClicker = Clicker(self.building_x, 453)
        self.bankClicker = Clicker(self.building_x, 518)
        self.templeClicker = Clicker(self.building_x, 577)
        self.wizardClicker = Clicker(self.building_x, 648)
        self.shipmentClicker = Clicker(self.building_x, 706)
        self.alchemyClicker = Clicker(self.building_x, 776)
        # self.portalClicker = Clicker(, )
        # self.timeClicker = Clicker(, )
        # self.antimatterClicker = Clicker(, )

        self.BuildingList.append(self.cursorClicker)
        self.BuildingList.append(self.grandmaClicker)
        self.BuildingList.append(self.farmClicker)
        self.BuildingList.append(self.mineClicker)
        self.BuildingList.append(self.factoryClicker)
        self.BuildingList.append(self.bankClicker)
        self.BuildingList.append(self.templeClicker)
        self.BuildingList.append(self.wizardClicker)
        self.BuildingList.append(self.shipmentClicker)
        self.BuildingList.append(self.alchemyClicker)
        # self.BuildingList.append(self.portalClicker)
        # self.BuildingList.append(self.timeClicker)
        # self.BuildingList.append(self.antimatterClicker)

    def run(self):
        pyautogui.FAILSAFE = True

        counter = 0
        while True:
            counter += 1
            self.cookieClicker.click()
            
            if counter % 50 == 0:
                for building in reversed(self.BuildingList):
                    building.click()
                counter=0


def buildingFactory()->list[Building]:
    """instantiate building Classes from the Buildiings.json file"""
    buildingClassList = []
    file_path = Path(__file__).parent / 'game_data' / 'Buildings.json'
    with open(file_path) as f:
        buildingList = json.load(f)
        for building in buildingList:
            buildingClassList.append(Building(**building))
    return buildingClassList

if __name__ == '__main__':
    pyautogui.PAUSE = 0.05

    # redefine the ImageGrab.grab function to use just my second monitor
    first_monitor_width = 3440
    first_monitor_height = 1440
    second_monitor = (first_monitor_width, 0, first_monitor_width+1920, 1080)

    ImageGrab.grab = partial(ImageGrab.grab, bbox=second_monitor, all_screens=True)

    # printMousePositionLive()

    # windowCaptureRealtime()
    # cookieClicker = Clicker(3728, 432)
    # cookieClicker.click_n_times(100)
    # cookieClicker.click_forever()

    # agent = NiaveAgent()
    # agent.run()

    buildingObjects = buildingFactory()

   

    

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

* prune actions that are infeasible
    * if we can't afford a building or upgrade, we need to calculate
    the time it will take to get enough cookies to buy it and how 
    other actions would have affected the cps

* select the best action
    * maximize the increase in cookies per second divided by the cost of the action

"""