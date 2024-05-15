
import socket
import struct
import time

server_address = ('', 6999)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)
print(f"Listening on {server_address}")


def integer_to_action_anonyme(int_value):
    print(f"Add code here for Value {int_value}")


def integer_to_action_indexed(int_index, int_value):
    print(f"Add code here for Index {int_index} Value {int_value}")

def integer_to_action_indexed_with_date(int_index, int_value,ulong_milliseconds):

    date_type_digit = round(ulong_milliseconds / 1000000000000000000)
    date_without_type= ulong_milliseconds%1000000000000000000
    print(f"Date Type Digit {date_type_digit}")
    if(date_type_digit==0):
        print(f"Date type is unknow and probably DateTime UTC of the machine")
    if(date_type_digit==17):
        print(f"Date type is a request to be executed at date {date_without_type} in milliseconds in NTP format should by the client")
    if(date_type_digit==16):
        print(f"Date type is a when integer send at {date_without_type} in milliseconds in NTP format should by the client")


    print(f"Add code here for Index {int_index} Value {int_value} Date Ulong {ulong_milliseconds}({date_type_digit}-{date_without_type}) ")


while True:
    byte_received, address = sock.recvfrom(1024) 
    print(f'Received {len(byte_received)} bytes from {address}: {byte_received}')
    if byte_received is not None:
        if len(byte_received) == 16:
            index = struct.unpack('<i', byte_received[0:4])[0]
            value = struct.unpack('<i', byte_received[4:8])[0]
            ulong_milliseconds = struct.unpack('<Q', byte_received[8:16])[0]
            print(f"Received Bytes {index} | {value} | { ulong_milliseconds}")
            integer_to_action_anonyme(value)
            integer_to_action_indexed(index,value)
            integer_to_action_indexed_with_date(index,value,ulong_milliseconds)

