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
    'bc': 'Executing movement command...'
    # Add more commands as needed
}

# Motor GPIO pins
motor1A = 17
motor1B = 18
motor2A = 22
motor2B = 23

def initialize_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(motor1A, GPIO.OUT)
    GPIO.setup(motor1B, GPIO.OUT)
    GPIO.setup(motor2A, GPIO.OUT)
    GPIO.setup(motor2B, GPIO.OUT)

def move_forward():
    GPIO.output(motor1A, GPIO.HIGH)
    GPIO.output(motor1B, GPIO.LOW)
    GPIO.output(motor2A, GPIO.HIGH)
    GPIO.output(motor2B, GPIO.LOW)

def move_backward():
    GPIO.output(motor1A, GPIO.LOW)
    GPIO.output(motor1B, GPIO.HIGH)
    GPIO.output(motor2A, GPIO.LOW)
    GPIO.output(motor2B, GPIO.HIGH)

def turn_left():
    GPIO.output(motor1A, GPIO.LOW)
    GPIO.output(motor1B, GPIO.HIGH)
    GPIO.output(motor2A, GPIO.HIGH)
    GPIO.output(motor2B, GPIO.LOW)

def turn_right():
    GPIO.output(motor1A, GPIO.HIGH)
    GPIO.output(motor1B, GPIO.LOW)
    GPIO.output(motor2A, GPIO.LOW)
    GPIO.output(motor2B, GPIO.HIGH)

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
    move_forward()
    time.sleep(10)  # Adjust the duration of movement as needed
    stop_movement()
    turn_right()

def main():
    initialize_gpio()

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

if _name_ == "_main_":
    main()
    GPIO.cleanup()  # Cleanup GPIO on program exit