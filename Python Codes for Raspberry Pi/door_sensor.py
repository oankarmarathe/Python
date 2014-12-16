
import RPi.GPIO as GPIO
import time

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO pin to use
GPIO_DOOR = 7

# Set pin as input
GPIO.setup(GPIO_DOOR,GPIO.IN)

try:


 while True :

  # Read sensor state
  if GPIO.input(GPIO_DOOR) == 0:
     print " DOOR OPEN"	

  # Wait for 3 second
  time.sleep(0.3)

  if GPIO.input(GPIO_DOOR) == 1:
     print " DOOR CLOSED"

  # Wait for 3 second
  time.sleep(0.3)  
	
except KeyboardInterrupt:
  print "  Quit" 
  # Reset GPIO settings
  GPIO.cleanup()