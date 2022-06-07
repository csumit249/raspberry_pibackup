#pwm in raspberry final pwm eith webserver updated on 30-5


from flask import Flask, render_template_string, request   # Importing the Flask modules 
import RPi.GPIO as GPIO     # Importing the GPIO library 
from time import sleep      # Import sleep module from time library 
servo_pin = 13 # GPIO Pin where sero is connected
GPIO.setmode(GPIO.BCM)      # Define the Pin numbering type. Here we are using BCM type
# Defing Servo Pin as output pin
GPIO.setup(servo_pin, GPIO.OUT)     
p = GPIO.PWM(servo_pin, 2000)  # PWM channel at 50 Hz frequency
p.start(0) # Zero duty cycle initially
app = Flask(__name__)
#HTML Code 
TPL = '''
<html>
    
<head><title>Web Page Tractor control UNIT</title></head>
              <script>
    function updateSlider(slideAmount) {
        const data = { slider: slideAmount };
fetch('/test', {
  method: 'POST',
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
    let num=0;
    
    function increment(){
    let value=document.getElementById('value');
    num=parseInt(value.value)
    if(num+1<100){
    value.value=num+1;
    updateSlider(num+1)
    }
    
    
    }
    function decrement(){
    let value=document.getElementById('value');
    num=parseInt(value.value)
    if(num-1>0)
    {
    value.value=num-1;
    updateSlider(num-1)
    }
    
    }
</script>
<style>
input[type='number']:disabled{
background:red
}
</style>
    <body>
    <h2> Tractor Control Unit</h2>
        
            <div style='margin-top:15vh; margin-left:2vw;'>
            
            <button onclick='decrement()' style='height:50vh;width:35vw;background-color:green;'>Left<button>
            <input type='number' style='height:50vh;width:20vw;background-color:blanchedalmond;' value='50' id='value'></input>
            
            <button onclick='increment()' style='height:50vh;width:35vw;background-color:green;'>Right<button>
            
            
</div>
        
    </body>
</html>

'''

steer_value=0;

     

@app.route("/")
def home():                                                                                                                                                         
    return render_template_string(TPL)                        
@app.route("/test", methods=["POST"])
def test():
    # Get slider Values
    slider=request.json['slider']
    steer_value=int(slider)
    print("steer_value",steer_value)
    
    p.ChangeDutyCycle(steer_value)
        
    
    #slider = request["slider"]
    # Change duty cycle
    #print(float(slider))
#     sleep(1)
    # Pause the servo
#    p.ChangeDutyCycle(0)
     # return render_template_string(TPL)
    return 'success';
# Run the app on the local development server


    
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port =5001)

