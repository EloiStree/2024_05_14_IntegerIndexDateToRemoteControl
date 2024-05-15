
import socket
import struct
import time


# Code not tested by time missing but should work in the idea.

server_address = ('', 6998)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)


dico_to_int_up_AI_push={}
dico_to_int_down_AI_push={}
dico_to_int_up_client={}
dico_to_int_down_client={}

dico_to_int_up_AI_push = { 'up': 101, 'down': 102, 'left': 103, 'right': 104,'space': 105,
                    'a': 111, 'z': 112, 'e': 113, 'r': 114,'t': 115,
                    'q': 116, 's': 117, 'd': 118, 'f': 119,
                    }
dico_to_int_down_AI_push = { 'up': 201, 'down': 202, 'left': 203, 'right': 204,'space': 205,
                        'a': 211, 'z': 212, 'e': 213, 'r': 214,'t': 215,
                        'q': 216, 's': 217, 'd': 218, 'f': 219
                    }

dico_to_int_up_client = { 'up': 301, 'down': 302, 'left': 303, 'right': 304,'space': 305,
                    'a': 311, 'z': 312, 'e': 313, 'r': 314,'t': 315,
                    'q': 316, 's': 317, 'd': 318, 'f': 319,
                    }
dico_to_int_down_client = { 'up': 401, 'down': 402, 'left': 403, 'right': 404,'space': 405,
                        'a': 411, 'z': 412, 'e': 413, 'r': 414,'t': 415,
                        'q': 416, 's': 417, 'd': 418, 'f': 419
                        }


print(f"Listening on {server_address}")


def integer_to_action_indexed_with_date(int_index, int_value,ulong_milliseconds):

    date_type_digit = round(ulong_milliseconds / 1000000000000000000)
    date_without_type= ulong_milliseconds%1000000000000000000
   
    for key, value in dico_to_int_up_AI_push.items():
        if int_value==value:
            print(f"AI Push Arrow {key} key pressed{value}")

    for key, value in dico_to_int_down_AI_push.items():
        if int_value==value:
            print(f"AI Push Arrow {key} key released {value}")

    for key, value in dico_to_int_up_client.items():
        if int_value==value:
            print(f"Client Arrow {key} key pressed{value}")

    for key, value in dico_to_int_down_client.items():
        if int_value==value:
            print(f"Client Arrow {key} key released {value}")
 
   

while True:
    byte_received, address = sock.recvfrom(1024) 
    print(f'Received {len(byte_received)} bytes from {address}: {byte_received}')
    if byte_received is not None:
        if len(byte_received) == 16:
            index = struct.unpack('<i', byte_received[0:4])[0]
            value = struct.unpack('<i', byte_received[4:8])[0]
            ulong_milliseconds = struct.unpack('<Q', byte_received[8:16])[0]
            print(f"Received Bytes {index} | {value} | { ulong_milliseconds}")
            integer_to_action_indexed_with_date(index,value,ulong_milliseconds)

