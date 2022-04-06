import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2: ].zfill(8)]


dac = (26, 19, 13, 6, 5, 11, 9, 10)

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    number = 0
    isRising = True
    print("Введите период: ")
    period = int(input())
    ps = period/(256*2)
    while True:
        time.sleep(ps)
        binary = dec2bin(number)
        GPIO.output(dac, binary)

        if number == 255:
            isRising = False
        elif number == 0:
            isRising = True

        if isRising:
            number += 1
        else:
            number -= 1

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()