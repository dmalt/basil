#include "pump.h"
#define PUMP_PIN 13
#define MAX_COMMAND_BYTES 7
Pump pump(PUMP_PIN);


void setup() {
    Serial.begin(9600);
    Serial.setTimeout(5);
    /* Serial.println("<Arduino is ready>"); */
    pinMode(PUMP_PIN, OUTPUT);
}

void loop() {
    char key;
    uint16_t val;
    receiveCommand(key, val);
    switch (key) {
        case 'w':
            if (pump.isReady()) {
                Serial.println(val);
                pump.turnOn(val);
            }
            else Serial.print("Pump is busy");
            break;
        case 's':
            pump.turnOff();
            break;
        case 'a':
            Serial.println(key);
            Serial.print("Value = ");
            Serial.print(val);
            Serial.print("\n");
        default:
            break;
    }
    pump.update();
}

void receiveCommand(char &key, uint16_t &val) {
    char serialIn[MAX_COMMAND_BYTES];
    if (Serial.available()) {
        int nBytes = Serial.readBytesUntil(';', serialIn, MAX_COMMAND_BYTES);
        serialIn[nBytes] = NULL;
        key = serialIn[0];
        val = atol(serialIn + 1);
    }
    else {
        key = '\0';
        val = 0;
    }
}

void showNewData(char receivedChar) {
    Serial.println(receivedChar);
}
