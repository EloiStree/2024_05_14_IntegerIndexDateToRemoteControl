import random
import time
import socket
import struct

def generate_random_number():
    return random.randint(1000000000, 1999999999)
def generate_random_index():
    return random.randint(0, 8)

# What is the computer you want to redirect index int cmd to
host_int_cmd = '127.0.0.1'
# What is the port (the app) that need to received those int cmd information
port_int_cmd = 8089

def send_intCmd_value(intIndex, intValue):
    # Convert text inputs to integers
    intIndex = int(intIndex)
    intValue = int(intValue)
    
    # Create a bytes array with intIndex and intValue as integers
    data = struct.pack('<ii', intIndex, intValue)
    
    print(f"Sent {host_int_cmd}:{port_int_cmd}: {intIndex} {intValue}")
    
    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # Send data via UDP
        sock.sendto(data, (host_int_cmd, port_int_cmd))
        print("Data sent successfully.")
    except Exception as e:
        print("Error occurred while sending data:", e)
    finally:
        # Close the socket
        sock.close()

while True:
    random_number = generate_random_number()
    print("Nombre aléatoire:", random_number)
    send_intCmd_value(generate_random_index(), random_number)
    time.sleep(random.uniform(0.1,0.3))
