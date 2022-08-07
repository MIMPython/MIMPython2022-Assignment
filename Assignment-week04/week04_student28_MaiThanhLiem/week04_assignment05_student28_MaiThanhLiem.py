"""
Morse code is a method used in telecommunication to encode text characters 
as standardized sequences of two different signal durations, called dots and dashes, 
or dits and dahs.
"""
from turtle import dot


morseDictionary = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}
with open(".\\additionalFolder\\data.txt", "r") as file:
    data = file.read().split(" ")

message = ""
for word in data:
    for key, value in morseDictionary.items():
        if word == value:
            message += key

# for index in message:
#     if message[index : index + 3] == "dot":
#         message[index : index + 3] = "."
#     if message[index : index + 4] == "dash":
#         message[index : index + 4] = "-"
#     if message[index : index + 5] == "space":
#         message[index : index + 5] = " "

# for word in message:
#     for key, value in morseDictionary.items():
#         if word == value:
#             message += key
