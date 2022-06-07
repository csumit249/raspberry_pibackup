from flask import Flask, render_template_string, request   # Importing the Flask modules 
import RPi.GPIO as GPIO     # Importing the GPIO library 
from time import sleep      # Import sleep module from time library 
servo_pin = 12 # GPIO Pin where sero is connected
GPIO.setmode(GPIO.BCM)      # Define the Pin numbering type. Here we are using BCM type
# Defing Servo Pin as output pin
GPIO.setup(servo_pin, GPIO.OUT)     
p = GPIO.PWM(servo_pin, 2000)  # PWM channel at 50 Hz frequency
p.start(0) # Zero duty cycle initially
app = Flask(__name__)
 
# Store HTML code
TPL = '''
<html>
    <head><title>Web Application to control Servos </title></head>
    <body>
    <h2> Web Application to Control Servos</h2>
        <form method="POST" action="test">
            <p>Left side<input type="range" min="1" max="50" name="slider1" /> </p>
            <p>Right side<input type="range" min="50" max="100" name="slider1" /> </p>
            <input type="submit" value="submit" />
        </form>
    </body>
</html>
'''
 
# which URL should call the associated function.
@app.route("/")
def home():
    return render_template_string(TPL)
 
@app.route("/test", methods=["POST"])
def test():
    # Get slider Values
    slider1 = request.form["slider1"]
    slider1 = request.form["slider1"]
    print(float(slider1));
    # Change duty cycle
    p.ChangeDutyCycle(float(slider1))

    # Give servo some time to move
    sleep(1)
    # Pause the servo


    return render_template_string(TPL);
 
# Run the app on the local development server
if __name__ == "__main__":
    app.run()