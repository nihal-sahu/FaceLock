#include <LiquidCrystal_I2C.h>
#include <Servo.h>
#define servoPin 3

//ADD THE INCLUDED LCD DISPLAY LIBRARY AS A .ZIP FILE
LiquidCrystal_I2C lcd(0x27, 16, 2);
Servo servo;

int pos = 0;    //position of servo motor
bool unlocked = false; //tells state of door lock
int buttonPin = 8;

void setup() {
  // beginning UART communications baud rate 9600
  Serial.begin(9600);
  lcd.init(); // initialize the lcd
  lcd.backlight(); // Turn on backlight
  pinMode(buttonPin, INPUT_PULLUP);


}

void loop() {
  //checking if there is UART data to receive
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    lcd.setCursor(0, 0);
    
    if (data == "Nihal" && !unlocked)
    {
      unlocked = true;
      lcd.clear();
      lcd.print("Welcome Nihal!");
      delay(3000);
      servo_unlock();

      lcd.setCursor(0, 0);

      lcd.clear();
      lcd.print("Unlocked.\n");

      data = " ";
      
      lcd.clear();
      lcd.print("Locking in: 30 s");
      delay(30 * 1000);
      servo_lock();
      unlocked = false;
    }
    else if (!unlocked)
    {
      lcd.clear();
      lcd.print("Restricted access.");
    }
    
  }
}

void servo_unlock()
{
   servo.attach(servoPin);
   for (pos = 0; pos <= 180; pos += 1) { 
    servo.write(pos); 
    delay(15);
   }
   servo.detach();
}

void servo_lock()
{
   servo.attach(servoPin);
   for (pos = 180; pos >= 0; pos -= 1) { 
    servo.write(pos); 
    delay(15);
   }
   servo.detach();
}
