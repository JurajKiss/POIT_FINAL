bool generate = false;

void setup() {
  Serial.begin(9600); // Starts the serial communication

  pinMode(A0, INPUT);
  
  pinMode(D0, OUTPUT);
}

void loop() {
  int potenValue = analogRead(A0); // Read the potentiometer value
  
  if (generate) {
    Serial.print("Sending ");
    Serial.println(potenValue);
  }
  
  if (Serial.available() > 0) {
    String inputMessage = Serial.readString();

    if (inputMessage.indexOf("Light") >= 0) {
      GenerateSwitch();
    }
  }
}

void GenerateSwitch() {
  generate = !generate;
  if (generate){
    digitalWrite(D0, HIGH);
  } else{
    digitalWrite(D0, LOW);
  }
}
