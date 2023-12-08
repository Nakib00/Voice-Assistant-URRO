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

# Load OpenAI API key from an environment variable (recommended for security)
openai.api_key = os.getenv("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")

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Set the initial language for recognition
current_language = 'en-US'

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
        chatgpt_reply = get_chatgpt_response(user_input)
        if chatgpt_reply:
            reply(chatgpt_reply, 'bn' if current_language == 'bn-BD' else 'en')
            if current_language == 'bn-BD':
                current_language = 'en-US'  # Switch back to English after processing Bengali command
                print("Switched back to English language")
        else:
            print("No response from ChatGPT or an error occurred.")
