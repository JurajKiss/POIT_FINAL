import serial
import time

ser=serial.Serial("/dev/ttyUSB0",9600)
ser.baudrate=9600

while True:
        read_ser=ser.readline()
        #print(read_ser)
        decoded = read_ser.decode("utf-8")
        #print(decoded)
        cleaned = decoded.strip()
        print(cleaned)
        parts = cleaned.split()
        #print(parts)
        value = int(parts[1])
        #print(value)
        
        if value>=50:
            print("Bigger")
            message = "Light"
            byte_message = message.encode("utf-8")
            ser.write(byte_message)