import time
import keyboard
import random

def launch_spell_with_keyboard(char_to_press):
    keyboard.press(char_to_press)
    time.sleep(2.1)
    keyboard.release(char_to_press)
    time.sleep(0.1)
    

for index in range(0,10):
    # print("Hello World ! " + str(index))
    # print(f"Hello World {index}! " )

    launch_spell_with_keyboard('tab') 
    for attack_index in range(0,5):
        launch_spell_with_keyboard('&')

    if random.randint(0, 45) ==0:
        print("Jump")
        launch_spell_with_keyboard('space') 



