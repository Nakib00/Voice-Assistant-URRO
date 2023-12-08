import RPi.GPIO as GPIO
import time

# Define the GPIO pins connected to the L298N motor driver
IN1 = 17  # Input 1
IN2 = 18  # Input 2
IN3 = 22  # Input 3
IN4 = 23  # Input 4

def setup():
    # Set up GPIO mode and set warnings to false
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Set up motor control pins as output
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)

def stop():
    # Stop the motors
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

def forward():
    # Move the motors forward
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def backward():
    # Move the motors backward
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

def turn_left():
    # Turn the motors to the left
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def turn_right():
    # Turn the motors to the right
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

# Example usage
try:
    setup()

    # Move forward for 2 seconds
    forward()
    time.sleep(2)

    # Move backward for 2 seconds
    backward()
    time.sleep(2)

    # Turn left for 2 seconds
    turn_left()
    time.sleep(2)

    # Turn right for 2 seconds
    turn_right()
    time.sleep(2)

    # Stop the motors
    stop()

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()
