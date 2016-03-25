import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
        if(GPIO.input(12)==1):
                print 'Motion Detected'
        else:
                print 'Motion Undetected'
        time.sleep(.1)
