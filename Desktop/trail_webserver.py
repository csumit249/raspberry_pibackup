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
#HTML Code 
TPL = '''
<html>
    
    <head><title>Web Page Controlled Servo</title></head>
              <script>
    function updateSlider(slideAmount) {
        var sliderDiv = document.getElementById("sliderAmount");
        sliderDiv.innerHTML = slideAmount;
        const data = { slider: slideAmount };

fetch('/test', {
  method: 'POST', // or 'PUT'
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(data),
})
.then(response => response.json())
.then(data => {
  console.log('Success:', data);
})
.catch((error) => {
  console.error('Error:', error);
});
    }
</script>
    <body>
    <h2> Web Page to Control Servo</h2>
       
            <h3> Use the slider to rotate servo  </h3>
            <h4> left cursor </h4>
  
<input id="slide" type="range" min="1" max="100" step="1" value="10" onchange="updateSlider(this.value)">
<div id="sliderAmount"></div>
        </form>
    </body>
</html>

'''
@app.route("/")
def home():                                                                                                                                                         
    return render_template_string(TPL)                        
@app.route("/test", methods=["POST"])
def test():
    # Get slider Values
    slider=request.json['slider']
    print(slider)
    #slider = request["slider"]
    # Change duty cycle
    p.ChangeDutyCycle(float(slider))
    #print(float(slider))
    sleep(1)
    # Pause the servo
    p.ChangeDutyCycle(0)
     # return render_template_string(TPL)
    return 'success';
# Run the app on the local development server
if __name__ == "__main__":
    app.run()
