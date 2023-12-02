import RPi.GPIO as GPIO
import time


# Set the GPIO pin numbers
PINS = [4, 5, 6]
BTN_PIN = 2
GPIO.setwarnings(False)


# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PINS, GPIO.OUT)
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Sequence of LED pin lighting
PINS_ORDER = [4, 5, 6, 5]

GPIO.output(PINS, GPIO.LOW)
time.sleep(3)

print("******* HELLO *******")
print(" ")
# Light 3 leds
GPIO.output(PINS, GPIO.HIGH)
time.sleep(1)
GPIO.output(PINS, GPIO.LOW)

print("****** Waiting for button press ******")
# Keep leds off & wait for button press
GPIO.wait_for_edge(BTN_PIN, GPIO.FALLING)


# When button pressed: light led 1 & turn off other leds
GPIO.output(PINS, GPIO.LOW)
print("****** Button pressed ******")
print("")

# Wait for debounce
time.sleep(0.2)
GPIO.output(PINS[0], GPIO.HIGH)

# Wait for debounce
time.sleep(0.2)


led_counter = 0
try:
    while True:

        # Wait for button then turn off all leds
        GPIO.wait_for_edge(BTN_PIN, GPIO.FALLING)
        GPIO.output(PINS, GPIO.LOW)
        print("****** Button pressed ******")
        print("")

        #Debouncing time
        time.sleep(0.2)

        led_counter = (led_counter + 1) % len(PINS_ORDER)

        # Light the next LED in the sequence
        GPIO.output(PINS_ORDER[led_counter], GPIO.HIGH)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
