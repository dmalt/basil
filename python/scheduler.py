import schedule
from time import sleep
from api import (
    get_humidity,
    get_temperature,
    turn_off_lamp,
    turn_on_lamp,
    turn_on_pump,
)


def blink():
    turn_on_lamp()
    sleep(1)
    turn_off_lamp()


schedule.every().day.at("15:20").do(turn_on_lamp)


while True:
    schedule.run_pending()
    sleep(1)
