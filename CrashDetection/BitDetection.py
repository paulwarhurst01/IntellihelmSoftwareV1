import RPi.GPIO as GPIO


def crash_detected():
    GPIO.setwarnings(False) 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 21 to be an input pin and set initial value to be pulled low (off)

    while True:
        if GPIO.input(21) == GPIO.HIGH:
            print("Bit detected")
            return True
        else:
            return False