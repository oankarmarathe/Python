1  # pir_webcam_interface.py
2  # Detect movement using a PIR module
3  # Take a photo with webcam on detecting a motion
4  # Webcam is attached to a USB port of the Raspberry Pi
5  #
6  # Import required Python libraries
7  import RPi.GPIO as GPIO
8  import time
9  import datetime
10  
11  # Use BCM GPIO references
12  # instead of physical pin numbers
13  GPIO.setmode(GPIO.BCM)
14  
15  # Define GPIO to use on Pi
16  GPIO_PIR = 7
17  
18  print "PIR Module Test (CTRL-C to exit)"
19  
20  # Set pin as input
21  GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo
22 
23  Current_State  = 0
24  Previous_State = 0
25  x = 1
26  
27  try:
28  
29    print "Waiting for PIR to settle ..."
30    # Wait for one second
31    time.sleep(1)
32  
33    # Loop until PIR output is 0
34    while GPIO.input(GPIO_PIR)==1:
35      Current_State  = 0    
36  
37    print "  Ready"     
38      
39    # Loop until users quits with CTRL-C
40    while True :
41     
42      # Read PIR state
43      Current_State = GPIO.input(GPIO_PIR)
44     
45      if Current_State==1 and Previous_State==0:
46        # PIR is triggered
47        print "  Motion detected!"
48        import commands
49        CMD = "fswebcam -r 320x240 -d /dev/video0 -F0 --save /home/pi/01Dec2014/image"+str(x)+".png"
50        status, output = commands.getstatusoutput(CMD)
51        print output
52        x = x + 1
53   
54        # Record previous state
55        Previous_State=1
56        elif Current_State==0 and Previous_State==1:
57        # PIR has returned to ready state
58        print "  Ready"
59        Previous_State=0
60        
61      # Wait for 10 milliseconds
62      time.sleep(0.01)      
63        
64  except KeyboardInterrupt:
65    print "  Quit" 
66    # Reset GPIO settings
67    GPIO.cleanup()