from setup_serial import port, BAUDRATE, TIMEOUT
from serial import Serial  # type: ignore
import logging


def turn_on_lamp():
    with Serial(port.device, baudrate=BAUDRATE, timeout=TIMEOUT) as arduino:
        arduino.write(bytes("l1", "utf-8"))
        response = arduino.readline().decode("utf-8")
        assert response == "Turning on the lamp\r\n"
        logging.info(response)


def turn_off_lamp():
    with Serial(port.device, baudrate=BAUDRATE, timeout=TIMEOUT) as arduino:
        arduino.write(bytes("l0", "utf-8"))
        response = arduino.readline().decode("utf-8")
        assert response == "Turning off the lamp\r\n"
        logging.info(response)


def turn_on_pump(n_seconds: int):
    assert n_seconds > 0
    with Serial(port.device, baudrate=BAUDRATE, timeout=TIMEOUT) as arduino:
        arduino.write(bytes(f"p{n_seconds}", "utf-8"))
        response = arduino.readline().decode("utf-8")
        assert response == "Turning on the pump\r\n"
        logging.info(response)


def turn_off_pump():
    with Serial(port.device, baudrate=BAUDRATE, timeout=TIMEOUT) as arduino:
        arduino.write(bytes("p0", "utf-8"))
        response = arduino.readline().decode("utf-8")
        assert response == "Turning off the pump\r\n"
        logging.info(response)


def get_humidity() -> float:
    with Serial(port.device, baudrate=BAUDRATE, timeout=TIMEOUT) as arduino:
        arduino.write(bytes("h", "utf-8"))
        response = arduino.readline().decode("utf-8")
    return float(response)


def get_temperature() -> float:
    with Serial(port.device, baudrate=BAUDRATE, timeout=TIMEOUT) as arduino:
        arduino.write(bytes("t", "utf-8"))
        response = arduino.readline().decode("utf-8")
    return float(response)


if __name__ == "__main__":
    from time import sleep
    turn_on_lamp()
    sleep(1)
    turn_off_lamp()
    sleep(1)
    turn_on_lamp()
    sleep(1)
    turn_on_pump(5)
    sleep(1)
    turn_off_pump()
    print(f"h = {get_humidity()}%")
    print(f"t = {get_temperature()}C")
