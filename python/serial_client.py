"""
Try sending some data to arduino via serial port.

Adopted from
https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0
"""
# Importing Libraries
import serial  # type: ignore
import time

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readlines()
    return data


while True:
    num = input("Enter a number: ")  # Taking input from user
    value = write_read(num)
    print(value)  # printing the value
