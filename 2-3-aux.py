import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [2, 3, 14, 15, 18, 27, 23, 22]
GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

while True:
    for i in range(8):
        GPIO.output(leds[i], GPIO.input(aux[i]))
    time.sleep(1.0)