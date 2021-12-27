#include "pump.h"

char receivedChar;

void setup() {
 Serial.begin(9600);
 Serial.println("<Arduino is ready>");
 pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
 recvOneChar();
 if (receivedChar == 'b') blink(5000);
 else showNewData();
}

void recvOneChar() {
 if (Serial.available() > 0) {
 receivedChar = Serial.read();
 newData = true;
 }
}

void showNewData() {
 if (newData == true) {
 Serial.print("This just in ... ");
 Serial.println(receivedChar);
 newData = false;
 }
}
