from pynput import keyboard
import sys

option = ''


def on_press(key):
    global option
    if key == keyboard.Key.esc:
        print('Esc')
        option = 'q'
        sys.exit('Esc was pressed')
    try:
        option = key.char
        if key.char == 'q':
            print('q')
            sys.exit('q was pressed')
    except:
        option = ''
        pass


def Menu() -> None:
    print("Welcome to the Piano Tile Machine. Please select an option.\n")

    validOption = False
    global option

    while not validOption:
        validOption = True

        print("1. Select screen window.")
        print("2. Play game.")
        print("3. Loop game.")
        print("\nPress q to quit at any time.\n")

        print("Select your option.")
        option = ''
        while(option == ''):
            pass

        if(option == '1'):
            print("Select screen window")
        elif(option == '2'):
            print("Play game")
        elif(option == '3'):
            print("Loop game")
        elif(option == 'q'):
            print("Force quit")
            break
        else:
            validOption = False
            print("Wrong parameter, select a number from the options.\n")


if __name__ == "__main__":
    keyboardListener = keyboard.Listener(on_press=on_press)
    keyboardListener.start()
    Menu()
