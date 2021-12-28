#pragma once 
#include <Arduino.h>

#define BUSY false
#define READY true
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
            _state = BUSY;
            _period = seconds * 1000;
            _start = millis();
        }
        void turnOff() {
            digitalWrite(_pin, LOW);
            _state = READY;
        }
        void update() {
            if (_state == READY) return;
            if (millis() - _start >= _period) turnOff();
        }
        bool isReady() { return _state; }

    private:
        byte _pin;
        bool _state = READY;
        uint32_t _period;
        uint32_t _start;
};
