import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3

comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = 0)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def num2dac (value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal

def adc():
    for value in range(256):
        signal = num2dac(value)
        time.sleep(0.0007)
        voltage = value / levels * maxVoltage
        comparatorValue = GPIO.input(comp)
        if comparatorValue == 0:
            print("ADC value = {:^3} ->{} input voltage = {: .2f}".format(value, signal, voltage))
            break
       
try:
    while True:
        adc()
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)



