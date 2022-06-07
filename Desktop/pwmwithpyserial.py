import RPi.GPIO as GPIO
import time
import serial
ser = serial.Serial('/dev/ttyUSB0',9600)
s = [0]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
p=GPIO.PWM(12,2000)
p.start(0)

global i        

    
def serialdata():
     read_serial=ser.readline()
     s[0] = int (ser.readline())
     global i
     i=s[0]
     return 
        
while True:
    serialdata()
   
    p.ChangeDutyCycle(i)
    
    print(i)
    
    
                      

    
	
	