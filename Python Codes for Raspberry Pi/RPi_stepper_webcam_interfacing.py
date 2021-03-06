#!/usr/bin/env python

# Import required libraries
import time
import RPi.GPIO as GPIO
import commands

GPIO.cleanup() # cleaning up in case GPIOS have been preactivated

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# be sure you are setting pin accordingly
# GPIO10,GPIO9,GPIO11,GPIO25
StepPins = [10,9,11,25]

# Set all pin as output
for pin in StepPins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, False)

# variable fro webcam oputput images
x = 1

# variable to count no. of rotations
r = 1

# wait some time to start
time.sleep(0.5)

# Define some settings
StepCounter = 0
WaitTime = 0.0015

# Define simple sequence
StepCount1 = 4
Seq1 = []
Seq1 = range(0, StepCount1)
#Seq1[0] = [1,0,0,0]
#Seq1[1] = [0,1,0,0]
#Seq1[2] = [0,0,1,0]
#Seq1[3] = [0,0,0,1]

Seq1[0] = [0,0,0,1]
Seq1[1] = [0,0,1,0]
Seq1[2] = [0,1,0,0]
Seq1[3] = [1,0,0,0]

# Define advanced Sequence
# as shown in manufacturers datasheet
StepCount2 = 8
Seq2 = []
Seq2 = range(0, StepCount2)
#Seq2[0] = [1,0,0,0]
#Seq2[1] = [1,1,0,0]
#Seq2[2] = [0,1,0,0]
#Seq2[3] = [0,1,1,0]
#Seq2[4] = [0,0,1,0]
#Seq2[5] = [0,0,1,1]
#Seq2[6] = [0,0,0,1]
#Seq2[7] = [1,0,0,1]

Seq2[0] = [1,0,0,1]
Seq2[1] = [0,0,0,1]
Seq2[2] = [0,0,1,1]
Seq2[3] = [0,0,1,0]
Seq2[4] = [0,1,1,0]
Seq2[5] = [0,1,0,0]
Seq2[6] = [1,1,0,0]
Seq2[7] = [1,0,0,0]

# full Torque
StepCount3 = 4  
Seq3 = []
Seq3 = [3,2,1,0]
#Seq3[0] = [0,0,1,1]
#Seq3[1] = [1,0,0,1]
#Seq3[2] = [1,1,0,0]
#Seq3[3] = [0,1,1,0]

Seq3[0] = [0,1,1,0]
Seq3[1] = [1,1,0,0]
Seq3[2] = [1,0,0,1]
Seq3[3] = [0,0,1,1]

# set
Seq = Seq2
StepCount = StepCount2
# Start main loop
try:
       while 1==1:
		for pin in range(0,4):
			xpin = StepPins[pin]
			if Seq[StepCounter][pin]!=0:
				print " Step %i Enable %i" %(StepCounter,xpin)
				GPIO.output(xpin, True)
			else:
				GPIO.output(xpin, False)
		StepCounter += 1
		
	# If we reach end of the sequence
	# Start again
		if (StepCounter == StepCount):
			StepCounter = 0
			r += 1
		
			if (r == 85):
				time.sleep(1)

				#print" Wait for some time "

				CMD = "fswebcam -r 320x240 -d /dev/video0 -F0 --save /home/pi/05Dec2014/image"+str(x)+".png"
				satus, output = commands.getstatusoutput(CMD)
				print output 
				x = x + 1

				time.sleep(1)

			if (r == 86):
				r = 1 
		
		if (StepCounter < 0):
			StepCounter = StepCount
			
		# Wait before moving on
		time.sleep(WaitTime)

		
except:
	GPIO.cleanup();
finally: # cleaning up and setting pins to low again (motors can get hot if you want)
	GPIO.cleanup();
	for pin in StepPins:
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, False)

		