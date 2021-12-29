#include "pump.h"
#define PUMP_PIN 13
Pump pump(PUMP_PIN);

#include <DHT.h>
#define DHT_PIN 2
DHT dht(DHT_PIN, DHT11);

#define RELAY_PIN 4

#define MAX_COMMAND_BYTES 7

void setup() {
    Serial.begin(9600);
    Serial.setTimeout(5);
    /* Serial.println("<Arduino is ready>"); */
    pinMode(PUMP_PIN, OUTPUT);
    pinMode(RELAY_PIN, OUTPUT);
    dht.begin();
}

void loop() {
    char key;
    uint16_t val;
    receiveCommand(key, val);
    switch (key) {
        case 'w':
            if (!val) {
                pump.turnOff();
                break;
            }
            if (pump.isReady()) {
                Serial.println(val);
                pump.turnOn(val);
            }
            else Serial.print("Pump is busy");
            break;
        case 'a':
            Serial.println(key);
            Serial.print("Value = ");
            Serial.print(val);
            Serial.print("\n");
        case 't':
            Serial.println(dht.readTemperature());
            break;
        case 'h':
            Serial.println(dht.readHumidity());
            break;
        case 'r':
            if (val) digitalWrite(RELAY_PIN, HIGH);
            else digitalWrite(RELAY_PIN, LOW);
            break;
        case '\0':
            break;
        default:
            Serial.print("Unknown command ");
            Serial.println(key);
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
