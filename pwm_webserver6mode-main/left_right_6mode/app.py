from flask import Flask, render_template, request
import RPi.GPIO as GPIO     # Importing the GPIO library 
from time import sleep      # Import sleep module from time library 
servo_pin = 12# GPIO Pin where sero is connected
GPIO.setmode(GPIO.BCM)      # Define the Pin numbering type. Here we are using BCM type
# Defing Servo Pin as output pin
GPIO.setup(servo_pin, GPIO.OUT)     
p = GPIO.PWM(servo_pin, 2000)  # PWM channel at 50 Hz frequency
p.start(0) # Zero duty cycle initially
app = Flask(__name__)

@app.route('/', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        STRAIGHT = request.form.get('STRAIGHT')  # access the data inside 
      
        LEFT_60= request.form.get('LEFT_60')
        LEFT_90= request.form.get('LEFT_90')
        LEFT_180= request.form.get('LEFT_180')
        RIGHT_60= request.form.get('RIGHT_60')
        RIGHT_90= request.form.get('RIGHT_90')
        RIGHT_180= request.form.get('RIGHT_180')

        if STRAIGHT== 'STRAIGHT':
             message = "TRACTOR STRAIGHT PATH FOLLOWING"
             print("STRAIGHT IS pressed")
             
        #-------------LEFT SIDE ---------
        elif LEFT_60 == 'LEFT_60':
             message = "TRACTOR IS  60° LEFT SIDE"
             p.ChangeDutyCycle(63)
             sleep(0.1)
             p.ChangeDutyCycle(65)
             print("LEFT IS 60° pressed")
        elif LEFT_90 == 'LEFT_90':
             message = "TRACTOR IS 90° LEFT SIDE"
             p.ChangeDutyCycle(63)
             sleep(0.3)
             p.ChangeDutyCycle(65)
             print("LEFT IS  90° pressed")
        elif LEFT_180 == 'LEFT_180':
             message = "TRACTOR IS 180° LEFT SIDE"
             p.ChangeDutyCycle(63)
             sleep(0.7)
             p.ChangeDutyCycle(65)
        
             print("LEFT IS  180° pressed")
             #RIGHT SIDE _____------------------------
        elif RIGHT_60 == 'RIGHT_60':
             message = "TRACTOR IS  60° RIGHT SIDE"
             p.ChangeDutyCycle(77)
             sleep(0.1)
             p.ChangeDutyCycle(74)
             print("RIGHT IS 60° pressed")
        elif RIGHT_90 == 'RIGHT_90':
             message = "TRACTOR IS 90° RIGHT SIDE"
             p.ChangeDutyCycle(77)
             sleep(0.5)
             p.ChangeDutyCycle(74)
             print("RIGHT IS  90° pressed")
        elif RIGHT_180 == 'RIGHT_180':
             message = "TRACTOR IS 180° RIGHT SIDE"
             p.ChangeDutyCycle(77)
             sleep(0.7)
             p.ChangeDutyCycle(74)
             print("RIGHT IS  180° pressed")
    
        else:
            message = "WRONG BUTTON IS PRESSED"
            print("no button is pressed")

    return render_template('tractor.html', message=message)

if __name__ == "__main__":
    app.run()
