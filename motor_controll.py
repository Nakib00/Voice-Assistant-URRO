import speech_recognition as sr
import pyttsx3
import RPi.GPIO as GPIO
import time

word_dict = {
    'hello': 'Hi there!',
    'how are you': 'I am doing well, thank you!',
    'move forward': 'Moving forward...',
    'move backward': 'Moving backward...',
    'turn left': 'Turning left...',
    'turn right': 'Turning right...',
    'stop': 'Stopping...',
    'exit': 'Goodbye!',
    'bc': 'FUCK you.'
    # Add more commands as needed
}

# Motor GPIO pins
motor1A = 17
motor1B = 18
motor2A = 22
motor2B = 23

# PWM GPIO pins
enable1 = 27
enable2 = 24

# Initialize PWM for motor speed control
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1A, GPIO.OUT)
GPIO.setup(motor1B, GPIO.OUT)
GPIO.setup(motor2A, GPIO.OUT)
GPIO.setup(motor2B, GPIO.OUT)
GPIO.setup(enable1, GPIO.OUT)
GPIO.setup(enable2, GPIO.OUT)

motor_pwm1 = GPIO.PWM(enable1, 100)  # 100 Hz frequency
motor_pwm2 = GPIO.PWM(enable2, 100)  # 100 Hz frequency

motor_pwm1.start(0)  # Start with 0% duty cycle
motor_pwm2.start(0)  # Start with 0% duty cycle

def move_forward(speed=50):
    GPIO.output(motor1A, GPIO.HIGH)
    GPIO.output(motor1B, GPIO.LOW)
    GPIO.output(motor2A, GPIO.HIGH)
    GPIO.output(motor2B, GPIO.LOW)

    motor_pwm1.ChangeDutyCycle(speed)
    motor_pwm2.ChangeDutyCycle(speed)

def move_backward(speed=50):
    GPIO.output(motor1A, GPIO.LOW)
    GPIO.output(motor1B, GPIO.HIGH)
    GPIO.output(motor2A, GPIO.LOW)
    GPIO.output(motor2B, GPIO.HIGH)

    motor_pwm1.ChangeDutyCycle(speed)
    motor_pwm2.ChangeDutyCycle(speed)

def turn_left(speed=50):
    GPIO.output(motor1A, GPIO.LOW)
    GPIO.output(motor1B, GPIO.HIGH)
    GPIO.output(motor2A, GPIO.HIGH)
    GPIO.output(motor2B, GPIO.LOW)
    
    motor_pwm1.ChangeDutyCycle(speed)
    motor_pwm2.ChangeDutyCycle(speed)

def turn_right(speed=50):
    GPIO.output(motor1A, GPIO.HIGH)
    GPIO.output(motor1B, GPIO.LOW)
    GPIO.output(motor2A, GPIO.LOW)
    GPIO.output(motor2B, GPIO.HIGH)
    
    motor_pwm1.ChangeDutyCycle(speed)
    motor_pwm2.ChangeDutyCycle(speed)

def stop_movement():
    GPIO.output(motor1A, GPIO.LOW)
    GPIO.output(motor1B, GPIO.LOW)
    GPIO.output(motor2A, GPIO.LOW)
    GPIO.output(motor2B, GPIO.LOW)

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio).lower()
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

def lookup_command(command):
    return word_dict.get(command, "Command not recognized.")

def speak(text, rate=150):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def execute_movement():
    speak(word_dict['bc'], rate=150)
    move_backward(speed=50)
    time.sleep(5)
    turn_right(speed=50)
    time.sleep(1)
    move_forward(speed=50)
    stop_movement()
    
    
    
def main():
    while True:
        command = recognize_speech()

        if command is not None:
            if 'bc' in command:
                execute_movement()
            elif command == 'exit':
                stop_movement()
                speak("Goodbye!")
                break
            else:
                response = lookup_command(command)
                speak(response, rate=100)
                print(response)

if __name__ == "__main__":
    main()
    GPIO.cleanup()  # Cleanup GPIO on program exit