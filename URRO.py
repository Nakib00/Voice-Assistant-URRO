import speech_recognition as sr
import pyttsx3
import time
import datetime
import wikipedia
import RPi.GPIO as GPIO

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
    # Adjust the duration of movement as needed
    move_forward()
    time.sleep(10)  # Adjust the duration of movement as needed
    stop_movement()
    turn_right()
    time.sleep(10)  # Adjust the duration of movement as needed
    stop_movement()

      
def execute_movement_dmk():
    speak(word_dict['dmk'], rate=150)
    # Adjust the duration of movement as needed
    move_forward()
    time.sleep(10)  # Adjust the duration of movement as needed
    stop_movement()
    turn_right()
    time.sleep(10)  # Adjust the duration of movement as needed
    stop_movement()
    
def execute_movement_jublee():
    speak(word_dict['jublee'], rate=150)
    # Adjust the duration of movement as needed
    move_forward()
    time.sleep(10)  # Adjust the duration of movement as needed
    stop_movement()
    turn_right()
    time.sleep(10)  # Adjust the duration of movement as needed
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

# initialize
if __name__ == "__main__":
    main()
