import socket
port = 3614  
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def push_bytes_on_udp_port( int_value):
        data = int_value.to_bytes(4, 'little')
        sock.sendto(data, ('localhost', port))




while True:
        try:
                int_value = int(input("Enter an integer: "))
                print("Integer:", int_value)
                push_bytes_on_udp_port(int_value)
        except ValueError:
                print("Invalid input. Please enter an integer.")