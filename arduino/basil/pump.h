#pragma once 
#include <Arduino.h>

boolean newData = false;

void blink(int msec) {
  if (newData == true){
    Serial.print("in blink");
    digitalWrite(LED_BUILTIN, HIGH);
    delay(msec);
    digitalWrite(LED_BUILTIN, LOW);
    newData = false;
  }
}
