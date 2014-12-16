	import RPi.GPIO as GPIO
import time

# Variables

delay = 0.55
steps = 50

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Enable pins for in1-4 to control step sequence

Input1_pin = 18
Input2_pin = 22
Input3_pin = 24
Input4_pin = 26

# Set pin states

GPIO.setup(Input1_pin, GPIO.OUT)
GPIO.setup(Input2_pin, GPIO.OUT)
GPIO.setup(Input3_pin, GPIO.OUT)
GPIO.setup(Input4_pin, GPIO.OUT)

# Function for step sequence

def setstep(w1, w2, w3, w4):
	GPIO.output(Input1_pin, w1)
	GPIO.output(Input2_pin, w2)
	GPIO.output(Input3_pin, w3)
	GPIO.output(Input4_pin, w4)

# Loop through step sequrnce based on no. of steps

for i in range(0, steps):
	setstep(1,0,1,0)
	time.sleep(delay)
	setstep(0,1,1,0)
	time.sleep(delay)
	setstep(0,1,0,1)
	time.sleep(delay)
	setstep(1,0,0,1)
	time.sleep(delay)

# Reverse previous step sequenxe to reverse motor direction

for i in range(0, steps):
	setstep(1,0,0,1)
	time.sleep(delay)
	setstep(0,1,0,1)
	time.sleep(delay)
	setstep(0,1,1,0)
	time.sleep(delay)
	setstep(1,0,1,0)
	time.sleep(delay)


