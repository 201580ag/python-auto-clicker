import time
import threading
import keyboard
from pynput.mouse import Button, Controller

def get_valid_cps():
    while True:
        try:
            cps = int(input("Enter CPS (Clicks Per Second) (1 to 200): "))
            if 1 <= cps <= 200:
                return cps
            else:
                print("Please enter a value between 1 and 200.")
        except ValueError:
            print("Please enter a valid integer.")

def click_action(cps, stop_event):
    mouse = Controller()
    interval = 1 / cps

    while not stop_event.is_set():
        x, y = mouse.position
        mouse.click(Button.left, 1)
        time.sleep(interval)

def main():
    cps = get_valid_cps()
    print(f"CPS has been set to {cps}.")

    print("Press F6 key to start the program.")
    keyboard.wait('F6')

    stop_event = threading.Event()
    click_thread = threading.Thread(target=click_action, args=(cps, stop_event))
    click_thread.start()

    print("The program is running.")
    print("Press F7 key to exit the program.")
    keyboard.wait('F7')

    print("Exiting the program.")
    stop_event.set()
    click_thread.join()

if __name__ == "__main__":
    main()
