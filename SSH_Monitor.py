import subprocess
import time
from subprocess import check_output
import RPi.GPIO as GPIO

pins = [12,13]

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

def timeStop():
    time.sleep(.5)

def loop():
    while True:
        tst = subprocess.check_output(["w"])

        new = tst.splitlines()
        new.pop(0)
        new.pop(0)
        new.pop(0)
        new.pop(0)

        size = len(new)

        if size > 0:
            print("Connection is active")
            GPIO.output(pins[0], GPIO.HIGH)
            timeStop()
            GPIO.output(pins[0], GPIO.LOW)
        else:
            print("No connection active")
            GPIO.output(pins[1], GPIO.HIGH)
            timeStop()
            GPIO.output(pins[1], GPIO.LOW)
        
        timeStop()
        GPIO.output(pins[1], GPIO.HIGH)
        GPIO.output(pins[0], GPIO.HIGH)
def destroy():
    for pin in pins:
        GPIO.output(pin, GPIO.HIGH)
    GPIO.cleanup()

if True:
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
