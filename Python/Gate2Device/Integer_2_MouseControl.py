# pip install pyautogui pynput
import socket
import struct
import keyboard
import time
import pyautogui
#from pynput.mouse import Button, Controller

server_address = ('', 7150)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

mouse = pynput.mouse.Controller()

example=1588889999
request_offset_to_move=15
screen_size=pyautogui.size()
print(f"Screen Size {screen_size[0]} x {screen_size[1]}")

mouse_left_down= 1260
mouse_left_up= 2260
mouse_middle_down= 1261
mouse_middle_up= 2261
mouse_right_down= 1262
mouse_right_up= 2262

# Not in Pyautogui
mouse_button4_down= 1263
mouse_button4_up= 2263
# Not in Pyautogui
mouse_button5_down= 1264
mouse_button5_up= 2264


bool_allow_mouse_click=True
bool_allow_mouse_left_click=True
bool_allow_mouse_right_click=True
bool_allow_mouse_midddle_click=True
bool_allow_secondary_click=True

bool_use_debug_log=True



def parse_integer_mouse_move(integer_value):
    type_offset= int(integer_value/100000000)
    if(type_offset==15):
        x= int( ((integer_value/10000)%10000))
        y= int(integer_value%10000)
        if bool_use_debug_log:
            print(f"offset_ {integer_value} | type_offset {type_offset} | x {x} | y {y}")
        percent_x= x/9999
        percent_y= y/9999
        pyautogui.moveTo(screen_size[0]*percent_x,screen_size[1]*(1.0-percent_y))
    else :
        if bool_allow_mouse_click:
            if integer_value==mouse_left_down and bool_allow_mouse_left_click:
                pyautogui.mouseDown(button='left')
            elif integer_value==mouse_left_up:
                pyautogui.mouseUp(button='left' and bool_allow_mouse_left_click)
            elif integer_value==mouse_right_down:
                pyautogui.mouseDown(button='right' and bool_allow_mouse_right_click)
            elif integer_value==mouse_right_up:
                pyautogui.mouseUp(button='right'and bool_allow_mouse_right_click)
            elif integer_value==mouse_middle_down:
                pyautogui.mouseDown(button='middle'and bool_allow_mouse_midddle_click)
            elif integer_value==mouse_middle_up:
                pyautogui.mouseUp(button='middle'and bool_allow_mouse_midddle_click)
            # elif integer_value==mouse_button4_down and bool_allow_secondary_click:
                # mouse.press(Button.x1)
            # elif integer_value==mouse_button4_up and bool_allow_secondary_click:
                # mouse.release(Button.x1)
            # elif integer_value==mouse_button5_down and bool_allow_secondary_click:
                # mouse.press(Button.x2)
            # elif integer_value==mouse_button5_up and bool_allow_secondary_click:  
                # mouse.release(Button.x2)
            



bool_use_mouse_testing=False
if bool_use_mouse_testing:
    for i in range(2):
        time.sleep(0.01)
        parse_integer_mouse_move(1555555555)
        time.sleep(0.01)
        parse_integer_mouse_move(1510009000)
        time.sleep(0.01)
        parse_integer_mouse_move(1590009000)
        time.sleep(0.01)
        parse_integer_mouse_move(1590001000)
        time.sleep(0.01)
        parse_integer_mouse_move(1510001000)
    # time.sleep(1)
    # parse_integer_mouse_move(mouse_left_down)
    # time.sleep(1)
    # parse_integer_mouse_move(mouse_left_up)
    # time.sleep(1)
    # parse_integer_mouse_move(mouse_right_down)
    # time.sleep(1)
    # parse_integer_mouse_move(mouse_right_up)
    # time.sleep(1)
    # parse_integer_mouse_move(mouse_middle_down)
    # time.sleep(1)
    # parse_integer_mouse_move(mouse_middle_up)


while True:
    byte_received, address = sock.recvfrom(1024)  # Adjust the buffer size as needed
    print(f'Received {len(byte_received)} bytes from {address}: {byte_received}')
    if byte_received is not None:

        if len(byte_received) == 4:
            value = struct.unpack('<i', byte_received[0:4])[0]
            if bool_use_debug_log:
              print(f"Received Bytes {value}")
            parse_integer_mouse_move(value)

        if len(byte_received) == 8:
            index = struct.unpack('<i', byte_received[0:4])[0]
            value = struct.unpack('<i', byte_received[4:8])[0]
            if bool_use_debug_log:
              print(f"Received Bytes {index} | {value}")
            parse_integer_mouse_move(value)

        if len(byte_received) == 16:
            index = struct.unpack('<i', byte_received[0:4])[0]
            value = struct.unpack('<i', byte_received[4:8])[0]
            ulong_milliseconds = struct.unpack('<q', byte_received[8:16])[0]
            if bool_use_debug_log:
              print(f"Received Bytes {index} | {value} | { ulong_milliseconds}")
            parse_integer_mouse_move(value)

