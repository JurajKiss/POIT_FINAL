const int trigPin = 12;
const int echoPin = 14;

//define sound velocity in cm/uS
#define SOUND_VELOCITY 0.034
#define CM_TO_INCH 0.393701



void setup() {
  Serial.begin(9600); // Starts the serial communication
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW); 
}

void loop() {

  digitalWrite(LED_BUILTIN, HIGH);
  int randomValue = random(100);
                   
  Serial.print("Sending ");
  Serial.println(randomValue);

  if (Serial.available() > 0) { // Check if there's any data available to read
    String inputMessage = Serial.readString(); // Read the incoming message as a String

    if (inputMessage.indexOf("Light") >= 0) { // Check if the message contains "Light"
      functionA(); // Call function A if "Light" is found
    } else if (inputMessage.indexOf("Sensor") >= 0) { // Check if the message contains "Sensor"
      functionB(); // Call function B if "Sensor" is found
    }
  }

  delay(1000); // Small delay to allow for stable serial communication
}

void functionA() {
  Serial.println("Function A is running"); // Placeholder for what Function A does
  // Add your code for Function A here
}

void functionB() {
  Serial.println("Function B is running"); // Placeholder for what Function B does
  // Add your code for Function B here
}
