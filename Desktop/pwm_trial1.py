import RPi.GPIO as GPIO     # Importing the GPIO library 
from time import sleep      # Import sleep module from time library 
servo_pin = 12 # GPIO Pin where sero is connected
GPIO.setmode(GPIO.BCM)      # Define the Pin numbering type. Here we are using BCM type
# Defing Servo Pin as output pin
GPIO.setup(servo_pin, GPIO.OUT)     
p = GPIO.PWM(servo_pin, 2000)  # PWM channel at 50 Hz frequency
p.start(0) # Zero duty cycle initially

while True:
    for i in range(0,100,1):
        p.ChangeDutyCycle(i)
    #print(float(slider))
        sleep(1)
        #print("i",i)            
        if(i>=99):
            for j in range(100,0,-1):
                p.ChangeDutyCycle(j)
            #print(float(slider))
                sleep(1)
                #print("J",j)
        

