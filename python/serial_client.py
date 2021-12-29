"""
Try sending some data to arduino via serial port.

Adopted from
https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0

"""
from __future__ import annotations
import time
from serial import Serial  # type: ignore

from setup_serial import port, BAUDRATE, TIMEOUT


def write_read(arduino: Serial, x: str) -> list[str]:
    arduino.write(bytes(x, "utf-8"))
    time.sleep(0.05)
    data = arduino.readlines()
    return data


with Serial(port=port.device, baudrate=BAUDRATE, timeout=TIMEOUT) as arduino:
    while True:
        command = input("Enter command (<ctrl-c> for exit): ")
        value = write_read(arduino, command)
        print(value)
