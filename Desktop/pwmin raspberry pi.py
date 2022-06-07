import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
p=GPIO.PWM(12,2000)
p.start()

while True:
    for i in range(0,101,1):
        p.ChangeDutyCycle(i)
        time.sleep(0.1)
    time.sleep(0.5)    
     for i in range(100):
        p.ChangeDutyCycle(i)
        time.sleep(0.1)
   time.sleep(0.5)