import logging
import schedule
from time import sleep
from api import (
    turn_off_lamp,
    turn_on_lamp,
    turn_on_pump,
)

logging.basicConfig(level=logging.INFO)


def blink():
    turn_on_lamp()
    sleep(1)
    turn_off_lamp()


def water():
    turn_on_pump(15)


logging.info("Starting...")
schedule.every().day.at("08:00").do(turn_on_lamp)
schedule.every().day.at("20:00").do(turn_off_lamp)
schedule.every(6).hours.do(water)
logging.info("Scheduled lamp and watering")


while True:
    schedule.run_pending()
    sleep(1)
