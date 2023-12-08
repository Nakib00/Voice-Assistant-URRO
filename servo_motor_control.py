import RPi.GPIO as GPIO
import time

# Define the GPIO pin connected to the servo
SERVO_PIN = 18

def setup_servo():
    # Set up GPIO mode and set warnings to false
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Set up servo control pin as output
    GPIO.setup(SERVO_PIN, GPIO.OUT)

    # Create PWM instance with a frequency of 50Hz
    global servo_pwm
    servo_pwm = GPIO.PWM(SERVO_PIN, 50)
    servo_pwm.start(0)  # Start PWM with duty cycle 0

def set_servo_angle(angle):
    # Set the servo angle (angle should be between 0 and 180)
    duty_cycle = angle / 18.0 + 2.5
    servo_pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)  # Allow time for the servo to reach the desired position

def cleanup_servo():
    # Clean up GPIO
    servo_pwm.stop()
    GPIO.cleanup()

# Example usage
try:
    setup_servo()

    # Move the servo to 0 degrees
    set_servo_angle(0)
    time.sleep(1)

    # Move the servo to 90 degrees
    set_servo_angle(90)
    time.sleep(1)

    # Move the servo to 180 degrees
    set_servo_angle(180)
    time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    cleanup_servo()
