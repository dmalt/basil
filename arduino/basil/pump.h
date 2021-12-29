#pragma once 
#include <Arduino.h>

#define WORKING false
#define IDLE true
#define MAX_WATER_SEC 300  // 5 min


class Pump {
    public:
        Pump(byte pin) { _pin = pin; }
        void turnOn(uint16_t seconds) {
            if (seconds > MAX_WATER_SEC) {
                Serial.println("Max watering time exceeded. Aborting.");
                return;
            }
            digitalWrite(_pin, HIGH);
            _state = WORKING;
            _period = seconds * 1000;
            _start = millis();
        }
        void turnOff() {
            digitalWrite(_pin, LOW);
            _state = IDLE;
        }
        void update() {
            if (_state == IDLE) return;
            if (millis() - _start >= _period) turnOff();
        }
        char getState() {
            if (_state == WORKING) return 'w';  // working
            else return 'i';  // idle
        }

    private:
        byte _pin;
        bool _state = IDLE;
        uint32_t _period;
        uint32_t _start;
};
