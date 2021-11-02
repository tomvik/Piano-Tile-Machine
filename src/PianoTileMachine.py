from pynput import keyboard
import sys

import Common
from ScreenWindowSelection import FindCoordinates
from Engine import PlayGame


def on_press(key):
    if key == keyboard.Key.esc:
        print('Esc')
        Common.option = 'q'
    try:
        Common.option = key.char
        if key.char == 'q':
            print('q')
    except:
        Common.option = ''
        pass


def Menu() -> None:
    print("Welcome to the Piano Tile Machine. Please select an option.\n")

    validOption = False

    while not validOption:
        validOption = True

        print("1. Select screen window.")
        print("2. Play game in slow mode. (1 click per screenshot)")
        print("3. Play game in normal mode. (many clicks click per screenshot)")
        print("4. Play game in stupidly fast mode. (no screenshots, just points)")
        print("\nPress q to quit at any time.\n")

        print("Select your option.")
        Common.option = ''
        while(Common.option == ''):
            pass

        if(Common.option == '1'):
            print("Select screen window")
            FindCoordinates()
        elif(Common.option == '2'):
            print("Play game in slow mode")
            PlayGame(1)
        elif(Common.option == '3'):
            print("Play game in normal mode")
            PlayGame(2)
        elif(Common.option == '4'):
            print("Play game in stupidly fast mode")
            PlayGame(3)
        elif(Common.option == 'q'):
            print("Force quit")
            break
        else:
            validOption = False
            print("Wrong parameter, select a number from the options.\n")


if __name__ == "__main__":
    keyboardListener = keyboard.Listener(on_press=on_press)
    keyboardListener.start()
    Menu()
