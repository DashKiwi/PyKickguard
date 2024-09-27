import keyboard
import time
import random
import os

def stay_active(movement_time):
    try:
        while True:
            # start the timer till begining
            time.sleep(movement_time)
            print("Strafing...")

            # Brefly press the 'a' key
            keyboard.press('a')
            time.sleep(random.randrange(1, 4) / 10)
            keyboard.release('a')
            
            # small gap inbetween
            time.sleep(random.randrange(1, 2) / 10)
            
            # Brefly press the 'd' key
            keyboard.press('d')
            time.sleep(random.randrange(1, 4) / 10)
            keyboard.release('d')

    except KeyboardInterrupt:
        print("Script stopped.")
os.system("cls||clear")
print("welcome to PyKickGuard\n\nA program made to stop you from being kicked for innactivity\nProgram by DashKiwi\n")

while True:
    try:
        movement_time = int(input("How often do you want to strafe? (s)\n"))
        print(f"Program has begun and will strafe every {movement_time} seconds")
        break
    except:
        print("Please enter a vaild movement time in seconds")
stay_active(movement_time)
