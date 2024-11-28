import socket
import struct
import time
import keyboard
dico_to_int_up = {}
dico_to_int_down = { }

int_up_to_keyboard_value = {}
int_down_to_keyboard_value = {}


## CODE NOT TESTED AND INTERRUPETED
## NEED TO COME BACK ON IT LATER

## WARNING USING KEYBOARD IS LANGUAGE DEPENDANT
## THIS IS SHIT if you want to be sure that the code do what you want him to do.
## STILL IT IS USABLE FOR MOST KEY.
## YOU CAN FIND A WINDOW VERSION HERE:
## https://github.com/EloiStree/2024_08_29_ScratchToWarcraft/blob/main/PythonBridge/IntegerToWarcraft.py
## THERE IS AN OPTION TO USE REAL KEYBOARD INSTEAD OF FAKE.




# All new mappings from the provided list
new_mappings = {
    "backspace": (1008, 2008),
    "tab": (1009, 2009),
    "clear": (1012, 2012),
    "enter": (1013, 2013),
    "shift": (1016, 2016),
    "ctrl": (1017, 2017),
    "alt": (1018, 2018),
    "pause": (1019, 2019),
    "capslock": (1020, 2020),
    "escape": (1027, 2027),
    "space": (1032, 2032),
    "page up": (1033, 2033),
    "page down": (1034, 2034),
    "end": (1035, 2035),
    "home": (1036, 2036),
    "left": (1037, 2037),
    "up": (1038, 2038),
    "right": (1039, 2039),
    "down": (1040, 2040),
    "select": (1041, 2041),
    "print": (1042, 2042),
    "Execute": (1043, 2043),
    "print screen": (1044, 2044),
    "insert": (1045, 2045),
    "delete": (1046, 2046),
    "0": (1048, 2048),
    "1": (1049, 2049),
    "2": (1050, 2050),
    "3": (1051, 2051),
    "4": (1052, 2052),
    "5": (1053, 2053),
    "6": (1054, 2054),
    "7": (1055, 2055),
    "8": (1056, 2056),
    "9": (1057, 2057),
    "A": (1065, 2065),
    "B": (1066, 2066),
    "C": (1067, 2067),
    "D": (1068, 2068),
    "E": (1069, 2069),
    "F": (1070, 2070),
    "G": (1071, 2071),
    "H": (1072, 2072),
    "I": (1073, 2073),
    "J": (1074, 2074),
    "K": (1075, 2075),
    "L": (1076, 2076),
    "M": (1077, 2077),
    "N": (1078, 2078),
    "O": (1079, 2079),
    "P": (1080, 2080),
    "Q": (1081, 2081),
    "R": (1082, 2082),
    "S": (1083, 2083),
    "T": (1084, 2084),
    "U": (1085, 2085),
    "V": (1086, 2086),
    "W": (1087, 2087),
    "X": (1088, 2088),
    "Y": (1089, 2089),
    "Z": (1090, 2090),
    "window": (1091, 2091),
    "window": (1092, 2092),
    "menu": (1093, 2093),
    "sleep": (1095, 2095),
    "num 0": (1096, 2096),
    "num 1": (1097, 2097),
    "num 2": (1098, 2098),
    "num 3": (1099, 2099),
    "num 4": (1100, 2100),
    "num 5": (1101, 2101),
    "num 6": (1102, 2102),
    "num 7": (1103, 2103),
    "num 8": (1104, 2104),
    "num 9": (1105, 2105),
    "num *": (1106, 2106),
    "num +": (1107, 2107),
    "num .": (1108, 2108),
    "num -": (1109, 2109),
    "num .": (1110, 2110),
    "num /": (1111, 2111),
    "f1": (1112, 2112),
    "f2": (1113, 2113),
    "f3": (1114, 2114),
    "f4": (1115, 2115),
    "f5": (1116, 2116),
    "f6": (1117, 2117),
    "f7": (1118, 2118),
    "f8": (1119, 2119),
    "f9": (1120, 2120),
    "f10": (1121, 2121),
    "f11": (1122, 2122),
    "f12": (1123, 2123),
    "numlock": (1144, 2144),
    "scrolllock": (1145, 2145),
    "shift": (1160, 2160),
    "right shift": (1161, 2161),
    "ctrl": (1162, 2162),
    "right ctrl": (1163, 2163),
    "alt": (1164, 2164),
    "alt gr": (1165, 2165),
    "volum down": (1174, 2174),
    "volum up": (1175, 2175),
    "mute": (1173, 2173),
    "play": (1179, 2179),
    "play": (1250, 2250),
    "stop": (1178, 2178),
    "previous track": (1177, 2177),
    "next track": (1176, 2176),
}



# Update the dictionaries
for key, (up_code, down_code) in new_mappings.items():
    dico_to_int_up[key.lower()] = up_code
    dico_to_int_down[key.lower()] = down_code

int_up_to_dico = {v: k for k, v in dico_to_int_up.items()}
int_down_to_dico = {v: k for k, v in dico_to_int_down.items()}

# Print to verify
print("dico_to_int_up:", dico_to_int_up)
print("dico_to_int_down:", dico_to_int_down)


server_address = ('', 5648)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

offset_=1188889999


dico_previous_state = {}




def integer_to_keyboard_input(int_value):
    if int_up_to_dico.get(int_value) is not None:
        keyboard.press(int_up_to_dico[int_value])
    if int_down_to_dico.get(int_value) is not None:
        keyboard.release(int_down_to_dico[int_value])

bool_use_press_release_debug=True
if bool_use_press_release_debug:
    keyboard.on_press(lambda e: print(f"{e.name} pressed"))
    keyboard.on_release(lambda e: print(f"{e.name} released"))
    

while True:
    time.sleep(0.1)


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

          