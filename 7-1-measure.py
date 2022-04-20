import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import time

measured_data = []

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12 ,7, 8, 25, 24]
troyka = 17
comp = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(leds,GPIO.OUT, initial = 0)
GPIO.setup(troyka, GPIO.OUT, initial = 0)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(decimal):
    return [int(elem) for elem in bin(decimal)[2:].zfill(8)]

def bin2dac(value):
    b = decimal2binary(value)
    GPIO.output(dac,b)
    return b

def adc():
    i = 0
    num = [0,0,0,0,0,0,0,0]
    value = 0
    while (i != 7):
        num[i] = 1
        GPIO.output(dac,num)
        time.sleep(0.01)
        comparatorValue = GPIO.input(comp)
        if comparatorValue == 0:
            num [i] = 0
        else:
            value += 2**(7-i)
        i += 1

    return value

try:
    start = time.time()

    decimal = 0
    GPIO.output(troyka, 1)

    while decimal <= 248:
        decimal = adc()
        i = 0
        volume = int(8*decimal/250)
        bin = [0,0,0,0,0,0,0,0]
        for i in range (volume):
            bin[i] = 1
        GPIO.output(leds, bin)
        measured_data.append(decimal)
        print(decimal)
    
    GPIO.output(troyka, 0)

    while decimal >= 7:
        decimal = adc()
        i = 0
        volume = int(8*decimal/250)
        bin = [0,0,0,0,0,0,0,0]
        for i in range (volume):
            bin[i] = 1
        GPIO.output(leds, bin)
        measured_data.append(decimal)
        print(decimal)
    
    finish = time.time()

    experiment_time = finish - start
    T = experiment_time/(len(measured_data) - 1)
    nu = 1 / T
    

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)
    GPIO.cleanup(leds)

plt.plot(measured_data)
plt.show()

print(format(experiment_time))
print(format(0.01))
print(format(100))
print(format(3.3/256))

measured_data_str = [str(item) for item in measured_data]

with open ("data.txt", "w") as data_outfile:
        data_outfile.write("\n".join(measured_data_str))

with open ("settings.txt", "w") as settings_outfile:
        
        settings_outfile.write('time =' + str(experiment_time) + '\n')
        settings_outfile.write('T =' + str(T) + '\n')
        settings_outfile.write('nu =' + str(nu) + '\n')
        settings_outfile.write('a =' + format(3.3/256))



