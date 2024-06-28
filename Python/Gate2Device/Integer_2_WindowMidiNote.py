import socket
import struct
import keyboard
import time
import mido
import socket
import struct
import keyboard
import time
import mido
import socket

# List MIDI device inputs and outputs
input_names = mido.get_input_names()
output_names = mido.get_output_names()

listen_port = 7005

# Display local IP addresses

def display_local_ips():
    hostname = socket.gethostname()
    ip_addresses = socket.gethostbyname_ex(hostname)[-1]
    print("Local IP addresses:")
    for ip_address in ip_addresses:
        print(ip_address)

display_local_ips()

print("")

print("Listent Port is ", listen_port)

print("")

print("MIDI Device Inputs:")
for input_name in input_names:
    print(input_name)

print("MIDI Device Outputs:")
for output_name in output_names:
    print(output_name)

server_address = ('', listen_port)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

example=1215100121
request_offset_to_move=11
#midi_out = mido.open_output('MPK mini play 3')
midi_out = mido.open_output('Microsoft GS Wavetable Synth 0')

def change_default_midi_out_channel(channel):
    control_change = mido.Message('control_change', channel=channel, control=0)
    midi_out.send(control_change)

# Rest of the code...

def play_note_on_default_midi_out(note, velocity):
    note_on = mido.Message('note_on', note=note, velocity=velocity)
    midi_out.send(note_on)

def turn_off_note_on_default_midi_out(note):
    note_off = mido.Message('note_off', note=note)
    midi_out.send(note_off)
    
previous_channel=0

def parse_integer_mouse_move(integer_value):
    global previous_channel
    type_offset= int(integer_value/100000000)
    if(type_offset==12):
        channel= int( ((integer_value/1000000)%100))
        note= int(integer_value/1000%1000)
        velocity= int(integer_value%1000)
        note = max(0, min(note, 127))
        velocity = max(0, min(velocity, 127))
        print(f"Channel {channel} Note {note} Velocity {velocity}")
        if (previous_channel!=channel):
            change_default_midi_out_channel(channel)
            previous_channel=channel

        if(velocity>0):
            play_note_on_default_midi_out(note,velocity)
        else:
            turn_off_note_on_default_midi_out(note)
        

def test_all_notes():
    for i in range(0, 127):
        parse_integer_mouse_move(1201000121+i*1000)
        time.sleep(0.4)
        parse_integer_mouse_move(1201000000+i*1000)
    parse_integer_mouse_move(example)

def integer_to_keyboard_input(int_value):
    parse_integer_mouse_move(int_value)



# test_all_notes()

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

          