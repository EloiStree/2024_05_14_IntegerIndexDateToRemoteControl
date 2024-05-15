import time
import keyboard
import random
import socket

ip = "127.0.0.1" # localhost
port = 5648  # UDP port number
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_integer_to_port_of_application(number_to_push): 
    data = number_to_push.to_bytes(4, 'little')
    print(f"Pushing {number_to_push} to port {port}")
    sock.sendto(data, ('localhost', 5648))

def press_and_release_integer( press , release):
    send_integer_to_port_of_application(press)
    time.sleep(2.1)
    send_integer_to_port_of_application(release) 

for index in range(0,10):
    #Tab
    press_and_release_integer(124,224)

    for attack_index in range(0,5):
        #Press release 1
        press_and_release_integer(105,205)

    if random.randint(0, 2) ==0:
        print("Jump")
        #Jump Space
        press_and_release_integer(125,225) 

sock.close()

