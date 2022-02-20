void setup() {
  // beginning UART communications baud rate 9600
  Serial.begin(9600);
  lcd.init(); // initialize the lcd
  lcd.backlight(); // Turn on backlight

}

void loop() {
  //checking if there is UART data to receive
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    lcd.setCursor(0, 1);
    lcd.print(data);
  }

}
