import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7, 50)
p.start(7.5)

try: 
	while True:
			# Neutral
			p.ChangeDutyCycle(7.5)
			time.sleep(1)
			# 180
			p.ChangeDutyCycle(12.5)
			time.sleep(1)
			# 0
			p.ChangeDutyCycle(2.5)
			time.sleep(1)

excwpt KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()

	 