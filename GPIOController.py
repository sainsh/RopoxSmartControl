import RPi.GPIO as GPIO

down = 37
up = 35

GPIO.setmode(GPIO.BOARD)
GPIO.setup(down, GPIO.OUT)
GPIO.setup(up, GPIO.OUT)

def goUp():
    GPIO.output(up, GPIO.HIGH)

def goDown():
    GPIO.output(down, GPIO.HIGH)

def stop():
    GPIO.output(up, GPIO.LOW)
    GPIO.output(down, GPIO.LOW)

def cleanUp():
    GPIO.cleanup()