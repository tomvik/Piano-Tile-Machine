import numpy as np
import cv2
import pyautogui
from pyscreeze import Box, Point

import Common


def FindCoordinates():
    print("Enter this link: https://gameforge.com/en-US/littlegames/magic-piano-tiles/# and don't click anything")
    print("Press 's' when ready to take the screenshot")

    while Common.option != "s":
        pass

    try:
        playButton: Box = pyautogui.locateOnScreen('data/img/Play.png')

        playButtonCenter: Point = pyautogui.center(playButton)

        pyautogui.click(playButtonCenter)

        pyautogui.sleep(4)

        pyautogui.screenshot("data/runtime_img/afterPlayButton.png")
    except:
        print("Play button was not there")

    gameWindow: Box = None

    try:
        startButton: Box = pyautogui.locateOnScreen(
            'data/img/Start.png', confidence=0.8)

        pyautogui.screenshot(
            "data/runtime_img/startButton.png", region=startButton)

        startButtonCenter = pyautogui.center(startButton)

        gameWindow = (startButtonCenter.x - 350,
                      startButtonCenter.y - 600, 700, 1200)

        pyautogui.screenshot(
            "data/runtime_img/gameWindow.png", region=gameWindow)
    except:
        print("Start button was not there")

    if gameWindow:
        print("Found the window box. Writing to file.")
        file = open("data/gameWindow.txt", "w")
        file.write(','.join(map(str, gameWindow)))
