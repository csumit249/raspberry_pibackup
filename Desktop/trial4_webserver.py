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
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initialscale=1.0">
<title>Document</title>
<link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/fontawesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
<input id=demoInput type=number min=1 max=100>
<button onclick="increment()">+</button>
<button onclick="decrement()">-</button>
<script>
   function increment() {
      document.getElementById('demoInput').stepUp();
   }
   function decrement() {
      document.getElementById('demoInput').stepDown();
   }
</script>
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
    slider1 = request["slider1"]
 
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