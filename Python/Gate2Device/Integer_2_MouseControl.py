import socket
import struct
import keyboard
import time
import pyautogui

server_address = ('', 7004)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

example=1188889999
request_offset_to_move=11
screen_size=pyautogui.size()
print(f"Screen Size {screen_size[0]} x {screen_size[1]}")

mouse_left_down= 86000
mouse_left_up= 87000
mouse_right_down= 86001
mouse_right_up= 87001


def parse_integer_mouse_move(integer_value):
    type_offset= int(integer_value/100000000)
    if(type_offset==11):
        x= int( ((integer_value/10000)%10000))
        y= int(integer_value%10000)
        print(f"offset_ {integer_value} | type_offset {type_offset} | x {x} | y {y}")
        percent_x= x/9999
        percent_y= y/9999
        pyautogui.moveTo(screen_size[0]*percent_x,screen_size[1]*(1.0-percent_y))
    if integer_value==mouse_left_down:
        pyautogui.mouseDown(button='left')
    if integer_value==mouse_left_up:
        pyautogui.mouseUp(button='left')
    if integer_value==mouse_right_down:
        pyautogui.mouseDown(button='right')
    if integer_value==mouse_right_up:
        pyautogui.mouseUp(button='right')


parse_integer_mouse_move(example)
time.sleep(1)
parse_integer_mouse_move(1155555555)
time.sleep(1)
parse_integer_mouse_move(mouse_left_down)
time.sleep(1)
parse_integer_mouse_move(mouse_left_up)
time.sleep(1)
parse_integer_mouse_move(mouse_right_down)
time.sleep(1)
parse_integer_mouse_move(mouse_right_up)


def integer_to_keyboard_input(int_value):
    parse_integer_mouse_move(int_value)

# Listen for incoming data
while True:
    byte_received, address = sock.recvfrom(1024)  # Adjust the buffer size as needed
    print(f'Received {len(byte_received)} bytes from {address}: {byte_received}')
    if byte_received is not None:
        if len(byte_received) == 16:
            index = struct.unpack('<i', byte_received[0:4])[0]
            value = struct.unpack('<i', byte_received[4:8])[0]
            ulong_milliseconds = struct.unpack('<q', byte_received[8:16])[0]
            print(f"Received Bytes {index} | {value} | { ulong_milliseconds}")
            integer_to_keyboard_input(value)

          