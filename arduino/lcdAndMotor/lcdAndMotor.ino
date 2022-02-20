#include <LiquidCrystal_I2C.h>
#include <Servo.h>
#define servoPin 3

//ADD THE INCLUDED LCD DISPLAY LIBRARY AS A .ZIP FILE
LiquidCrystal_I2C lcd(0x27, 16, 2);
Servo servo;

int pos = 0;

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
    lcd.setCursor(0, 0);

    if (data == "Nihal")
    {
      servo_unlock();
      lcd.print("Welcome Nihal!");
    }
    else
    {
      lcd.print("Restricted access.");
    }
    
  }
}

void servo_unlock()
{
   for (pos = 0; pos <= 180; pos += 1) { 
    servo.write(pos); 
   }
}

void servo_lock()
{
   for (pos = 180; pos >= 0; pos -= 1) { 
    servo.write(pos); 
 }
}
