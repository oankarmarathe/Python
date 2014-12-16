
import RPi.GPIO as GPIO
import time

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO pin to use
GPIO_DOOR = 7
GPIO_PIR = 25

# Set pin as input
GPIO.setup(GPIO_DOOR,GPIO.IN)
GPIO.setup(GPIO_PIR,GPIO.IN)

Current_State = 0
Previous_State = 0

try:

    # Loop until user quits with CTRL+C
   while True :

    
     # Read sensor state
    if GPIO.input(GPIO_DOOR) == 0:
         print " DOOR OPEN"

   # Wait for 3 seconds
    time.sleep(0.3) 

    if GPIO.input(GPIO_DOOR) == 1:
           print " DOOR CLOSED"

   # Wait for 3 seconds
    time.sleep(0.3) 

    #Loop until user quits with CTRL+C
   #while True :
     
     # Loop until PIR Output is 0
    while GPIO.input(GPIO_PIR) == 1:
     Current_State = 0


     # Read PIR State
     Current_State = GPIO.input(GPIO_PIR)
   
     if Current_State == 1 and Previous_State ==0:
	# PIR is triggered
	print " Motion detected!"

	# Record previous state
	Previous_State = 1

     elif Current_State == 0 and Previous_State == 1:
	# PIR has returned to ready state
	print " Ready"
	
	Previous_State = 0	

       # Wait for 1 second
        time.sleep(0.1)  
	
except KeyboardInterrupt:
  print "  Quit" 
  # Reset GPIO settings
  GPIO.cleanup()