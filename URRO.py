import speech_recognition as sr
import pyttsx3
import RPi.GPIO as GPIO
import datetime
import wikipedia
import time

# Datadase
word_dict = {
    'hello': 'Hi there!',

    'how are you': 'I am doing well, thank you!',

    'move forward': 'Moving forward...',

    'move backward': 'Moving backward...',

    'turn left': 'Turning left...',

    'turn right': 'Turning right...',

    'stop': 'Stopping...',

    'exit': 'Goodbye!',

    'bc': 'This is BC Building. Go straight, and you will find the entrance on your right for BC Building.',
    
    'dmk':"Proceed to your right, and you will encounter an alleyway close to the swimming pool. Take a left turn in the alley, and you'll come across the elevator leading to the DMK Building.",
    
    'jublee': "Turn right, and you will come across an alleyway near the swimming pool. Continue straight, then make a right turn again. You will find the elevator for Jubilee Building.",
    
    'Undergraduate': "Admission Requirements, Combined GPA of 7 in SSC and HSC with a minimum GPA of 3 in each O'Level in minimum 5 subjects with a GPA of 2.50 and A'Level in 2 subjects with a minimum GPA of 2.00 International Baccalaureate or U.S. High School Diploma Other 12 years equivalent degree (must have the equivalence certificate from Ministry of Education)",

    'Graduate': "Bachelor's degree from a recognized university with a minimum CGPA of 3.00 GRE or GMAT scores (optional)",
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

# Speech recognition functionality
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

# If not registered the speach running this function
def lookup_command(command):
    return word_dict.get(command, "Command not recognized.")

# speak functionality speak anything send by command
def speak(text, rate=150):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

# Moving functionality for robot move for bulding
def execute_movement_bc():
    speak(word_dict['bc'], rate=150)
    move_forward(speed=50)
    time.sleep(5)
    turn_right(speed=50)
    time.sleep(1)
    move_forward(speed=50)
    time.sleep(5)
    stop_movement()

def execute_movement_dmk():
    speak(word_dict['dmk'], rate=150)
    # Adjust the duration of movement as needed
    move_backward(speed=50)
    time.sleep(5)
    turn_left(speed=50)
    time.sleep(1)
    move_forward(speed=50)
    stop_movement()
    
def execute_movement_jublee():
    speak(word_dict['jublee'], rate=150)
    # Adjust the duration of movement as needed
    turn_left(speed=50)
    time.sleep(5)
    move_forward(speed=50)
    time.sleep(7)
    stop_movement()

def admission_handler():
    speak(word_dict['Undergraduate'], rate=150)
def wikipedia_handler(command):
    try:
        look_for = command.replace('tell me about','')
        about = wikipedia.summary(look_for, 2)
        speak(about)
    except:
        pt = 'Not found in Wikipedia'
        speak(pt)

# main function
def main():
    while True:
        command = recognize_speech()

        if command is not None:
            if 'bc' in command:
                execute_movement_bc()
            elif 'dmk' in command:
                execute_movement_dmk()
            elif 'jubilee' in command:
                execute_movement_jublee()
            elif 'admission' in command:
                admission_handler()
            elif 'tell me about' in command:
                wikipedia_handler(command)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%H:%M %p')
                speak('Current time is' + time)
            elif command == 'exit':
                speak("Goodbye!")
                break
            else:
                response = lookup_command(command)
                speak(response, rate=100)
                print(response)

if __name__ == "__main__":
    main()
    GPIO.cleanup()  # Cleanup GPIO on program exit