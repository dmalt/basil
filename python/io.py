from setup_serial import port, BAUDRATE, TIMEOUT
from serial import Serial  # type: ignore


def turn_on_lamp():
    with Serial(port.device, baudrate=BAUDRATE, timeout=TIMEOUT) as arduino:
        arduino.write(bytes("r1", "utf-8"))
        print(arduino.readline())


def turn_off_lamp():
    with Serial(port.device, baudrate=BAUDRATE, timeout=TIMEOUT) as arduino:
        arduino.write(bytes("r0", "utf-8"))
        print(arduino.readline())


if __name__ == "__main__":
    from time import sleep
    turn_on_lamp()
    sleep(2)
    turn_off_lamp()
    sleep(2)
    turn_on_lamp()
