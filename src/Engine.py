import numpy as np
import cv2
import pyautogui
from pyscreeze import Box, Point
import Common


def ShowImg(windowTitle, img):
    cv2.imshow(windowTitle, img)
    cv2.waitKey()


def ConvertToBlackAndWhite(img):
    grayImg = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    (_, blackAndWhiteImg) = cv2.threshold(
        grayImg, 50, 255, cv2.THRESH_BINARY)
    return blackAndWhiteImg


def GetBlackTiles(binaryImg, width, height, lanes):
    # Draw a line in the center of the lane
    desiredWidth = width // (lanes * 2)

    blackTiles = []
    for i in range(4):
        lineX = (desiredWidth * 2 * i) + desiredWidth

        lineBlackTiles = []
        consecutiveBlackPixels = 0
        MinBlackPixelsForTile = 50
        inBlackTile = False
        for lineY in reversed(range(height)):
            if binaryImg[lineY][lineX] == Common.BINARY_WHITE:
                consecutiveBlackPixels = 0
                inBlackTile = False
                binaryImg[lineY][lineX] = Common.BINARY_BLACK
            else:
                consecutiveBlackPixels += 1
                binaryImg[lineY][lineX] = Common.BINARY_WHITE

            if consecutiveBlackPixels > MinBlackPixelsForTile and not inBlackTile:
                inBlackTile = True
                lineBlackTiles.append(
                    Point(lineX, lineY + MinBlackPixelsForTile))

        blackTiles += lineBlackTiles

        # print(blackTiles)
        # ShowImg("lineimg", blackAndWhiteImg)

    def sortingFunction(point: Point):
        return point.y

    blackTiles.sort(reverse=True, key=sortingFunction)
    # print(blackTiles)

    return blackTiles


def CheckIfGameOver(binaryImg, width, height):
    lineY = height // 2

    blackSpots = 0
    blackPixelsCount = 0
    for lineX in range(width // 4, (width // 4) * 3):
        if binaryImg[lineY][lineX] == Common.BINARY_BLACK:
            blackPixelsCount += 1
        else:
            blackPixelsCount = 0

        if blackPixelsCount == 5:
            blackSpots += 1

    return blackSpots == 7
    # print(blackSpots)
    # cv2.line(binaryImg, Point(desiredWidth, height//2),
    #          Point(desiredWidth * 3, height//2), (0, 255, 0), 3)
    # ShowImg("CheckIfGameOver", binaryImg)


def PlayGame():
    print("Press p to play")

    while Common.option != "p":
        pass

    print("Reading the coordinates")
    file = open(Common.WINDOW_COORDINATES_TXT, "r")
    line = file.readline()
    rawGameWindow = tuple(map(int, line.split(',')))
    gameWindow: Box = Box(
        rawGameWindow[0], rawGameWindow[1], rawGameWindow[2], rawGameWindow[3])

    print(gameWindow)
    pyautogui.screenshot('data/runtime_img/PlayGame.png', region=gameWindow)

    print("Will begin playing the game")

    count = 0
    firstClick = True
    # 3 screenshots full screen
    # 6 with only region
    # How to improve it?
    while Common.option != 'q':
        count += 1
        screenshot = pyautogui.screenshot(region=gameWindow)
        blackAndWhiteImg = ConvertToBlackAndWhite(screenshot)

        if not CheckIfGameOver(blackAndWhiteImg, gameWindow.width, gameWindow.height):
            blackTiles = GetBlackTiles(
                blackAndWhiteImg, gameWindow.width, gameWindow.height, 4)
            blackTilesPosition = [
                Point(
                    tile.x + gameWindow.left,
                    tile.y + gameWindow.top + 50
                ) for tile in blackTiles]

            if len(blackTilesPosition):
                blackTile = blackTilesPosition[0]
                if firstClick:
                    pyautogui.moveTo(blackTile.x, blackTile.y, duration=0)
                    pyautogui.mouseDown(
                        blackTile.x+40, blackTile.y, duration=0.11)
                    firstClick = False
                pyautogui.mouseDown(blackTile.x+40, blackTile.y, duration=0)
        else:
            print("Game over")
            break


if __name__ == "__main__":
    Common.option = "p"
    PlayGame()
