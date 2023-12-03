## say "hello" to enable bangla language each time.....
import speech_recognition as sr
import openai
from gtts import gTTS
import os
from gpiozero import Servo
from time import sleep

servo = Servo(25)

# Define servo control functions
def set_servo_rest_position():
    """Set the servo to its rest position."""
    rest_position = 0  # Adjust this value based on your servo's rest position
    servo.value = rest_position

def servo_sweep():
    """Perform a sweep with the servo."""
    val = -1
    for _ in range(6):
        servo.value = val
        sleep(0.2)
        val = -val
    set_servo_rest_position()  # Reset to rest position after the sweep

# Load OpenAI API key directly (not recommended for production use)
openai.api_key = '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'

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Set the initial language for recognition
current_language = 'en-US'

# Define the admission information
admission_info = {
    'Undergraduate': "Admission Requirements,Combined GPA of 7 in SSC and HSC with a minimum GPA of 3 in each O'Level in minimum 5 subjects with a GPA of 2.50 and A'Level in 2 subjects with a minimum GPA of 2.00 International Baccalaureate or U.S. High School Diploma Other 12 years equivalent degree (must have the equivalence certificate from Ministry of Education)",
    'graduate': "Bachelor's degree from a recognized university with a minimum CGPA of 3.00 GRE or GMAT scores (optional)",
}

def listen():
    """Capture and recognize speech, returning the recognized text."""
    global current_language
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        try:
            text = recognizer.recognize_google(audio, language=current_language)
            print(f"You said: {text}")

            if current_language == 'en-US' and 'hello' in text.lower():
                current_language = 'bn-BD'
                print("Switched to Bengali language")
                return None  # Do not send 'hello' to GPT API
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

def reply(response, lang):
    """Use Google Text-to-Speech to reply with the given response."""
    servo_sweep()  # Perform servo sweep before replying
    print(f"Bot: {response}")
    tts = gTTS(text=response, lang=lang)
    tts.save("response.mp3")
    os.system("mpg123 response.mp3")

def get_chatgpt_response(user_input):
    """Get a response from OpenAI's ChatGPT model."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error communicating with OpenAI: {e}")
        return None

# Set the initial rest position of the servo
set_servo_rest_position()

while True:
    user_input = listen()
    if user_input:
        if user_input.lower() == 'admission':
            reply(admission_info['Undergraduate'], 'en')  # Speak undergraduate admission info
        else:
            chatgpt_reply = get_chatgpt_response(user_input)
            if chatgpt_reply:
                reply(chatgpt_reply, 'bn' if current_language == 'bn-BD' else 'en')
                if current_language == 'bn-BD':
                    current_language = 'en-US'  # Switch back to English after processing Bengali command
                    print("Switched back to English language")
            else:
                print("No response from ChatGPT or an error occurred.")