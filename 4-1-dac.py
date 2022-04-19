import RPi.GPIO as GPIO
dac = (26, 19, 13, 6, 5, 11, 9, 10)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    print("Enter number 0 to 255: ")
    while True:
        answer = input()
        if answer == 'q':
            break

        try:
            answer = int(answer)
        except:
            print("Incorrect!")
            continue

        if answer > 255:
            print("Number is too big")
            continue
        elif answer < 0:
            print("Number is too small")
            continue

        voltage = 3.3/256 * answer
        number = decimal2binary(answer)
        GPIO.output(dac, number)
        print(voltage)
    
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

        
