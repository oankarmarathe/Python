	
import RPi.GPIO as GPIO
import time
import datetime 

# Use BCM GPIO reference
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO pin to use
GPIO_DOOR = 7
GPIO_LED = 25

# Set pin as input
GPIO.setup(GPIO_DOOR,GPIO.IN)
GPIO.setup(GPIO_LED,GPIO.OUT)

def glow (): 
  GPIO.output(GPIO_LED, 1)
  time.sleep(0.01)
  GPIO.output(GPIO_LED, 0)
  time.sleep(0.01)
  return


try:

 while True :
   
  # Read sensor state
  if GPIO.input(GPIO_DOOR) == 0:
  
   start_time = time.time()
      
   while GPIO.input(GPIO_DOOR) == 0 :
    print " DOOR OPEN"
   
    # Wait for 5 seconds
    time.sleep(0.5)

    current_time = time.time()
       

    if current_time - start_time >= 5:  
       
       glow ()

  if GPIO.input(GPIO_DOOR) ==1:
      print " DOOR CLOSED"
    
     # Wait for 5 seconds
      time.sleep(0.5)

except KeyboardInterrupt:
  print " Quit"
  # Reset GPIO settings
  GPIO.cleanup()