import RPi.GPIO as GPIO
import time

while True:
    GPIO.setmode(GPIO.BOARD)

    TRIG=35
    ECHO=37
    rTRIG=16
    rECHO=18

    print ("Distance Measurement In Progress")

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(rTRIG, GPIO.OUT)
    GPIO.setup(rECHO, GPIO.IN)

    GPIO.output(TRIG, False)
    GPIO.output(rTRIG, False)
    print ("Waiting For Sensor To Settle")
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start=time.time()

    while GPIO.input(ECHO)==1:
        pulse_end=time.time()

    GPIO.output(rTRIG, True)
    time.sleep(0.00001)
    GPIO.output(rTRIG, False)

    while GPIO.input(rECHO)==0:
        pulse_start2=time.time()

    while GPIO.input(rECHO)==1:
        pulse_end2=time.time()

    pulse_duration = pulse_end - pulse_start
    pulse_duration2 = pulse_end2 - pulse_start2

    distance = pulse_duration * 17150
    distance = round(distance, 2)
    distance2 = pulse_duration2 * 17150
    distance2 = round(distance2, 2)
    print ("Left Distance:", distance, "cm", "Right Distance:", distance2, "cm")
    GPIO.cleanup()

