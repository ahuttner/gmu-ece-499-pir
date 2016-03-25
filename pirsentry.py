import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def Attack():
        print 'Motion Detected'
        os.system("python sendwheel.py " + 'x')
        time.sleep(3)
        os.system("python sendwheel.py " + 's')
        time.sleep(3)
        if (GPIO.input(12)==1):
                time.sleep(3)
                if (GPIO.input(12)==1):
                        Attack()

while True:
        os.system("python sendwheel.py " + 'a')
        time.sleep(0.5)
        os.system("python sendwheel.py " + 's')
        time.sleep(3.5)
        if (GPIO.input(12)==1):
                time.sleep(3)
                if (GPIO.input(12)==1):
                        Attack()
