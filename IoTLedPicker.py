import RPi.GPIO as GPIO
import random
import time


# Set the GPIO pin numbers
LED1 , LED2 = 4, 6
PINS = [LED1, LED2]
BTN_PIN = 2


# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PINS, GPIO.OUT)
GPIO.setup(BTN_PIN , GPIO.IN, pull_up_down=GPIO.PUD_UP)


def ledPicker(pickerStart, pickerIncrease, ledPicked):
    delayedTime = pickerStart
    ledOrder = [LED1, LED2]

    while delayedTime < ledPicked:
        GPIO.output(PINS[0], GPIO.HIGH)
        GPIO.output(PINS[1], GPIO.LOW)
        time.sleep(delayedTime)

        GPIO.output(PINS[0], GPIO.LOW)
        GPIO.output(PINS[1], GPIO.HIGH)
        time.sleep(delayedTime)


        delayedTime += delayedTime * pickerIncrease


    # Picks a number between 0 & 1 
    randomizedNum = random.randint(0, 1)
    
    # If the randomizer picks 0, light led 0 
    if randomizedNum == 0:
        GPIO.output(PINS[0], GPIO.HIGH)
        GPIO.output(PINS[1], GPIO.LOW)
        
    # If the randomizer picks 0, light led 1
    else:
        GPIO.output(PINS[0], GPIO.LOW)
        GPIO.output(PINS[1], GPIO.HIGH)


try:
    while True:
        
        # Set leds off as it makes the set up cleaner
        GPIO.output(PINS, GPIO.LOW)
        
        print("********** WAITING FOR BUTTON PRESS **********")
        print("")
        GPIO.wait_for_edge(BTN_PIN, GPIO.FALLING)
                
        print("********** BUTTON PRESSED - GOOD LUCK **********")
        print("")
        
        #Sets the delay time to pick a led
        ledPicker(0.05, 0.07, 0.1)
        
        time.sleep(1)  # Debouncing time

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()