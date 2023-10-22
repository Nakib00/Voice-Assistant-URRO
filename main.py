import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
from independent_data import club_info, depermant_info, admission_info


listener = sr.Recognizer()
urro = pyttsx3.init()
voices = urro.getProperty('voices')
urro.setProperty('voice',voices[1].id)


def talk(text):
    urro.say(text)
    urro.runAndWait()

def take_commend():
    commend = "" 
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            commend = listener.recognize_google(voice)
            commend = commend.lower()
            print("You:"+commend)

            if "independent" in commend:
                commend = commend.replace("independent", "")
    except:
        pass
    return commend

def run_urro():
    commend = take_commend()
    if 'time' in commend:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'play' in commend:
        song = commend.replace('play', '')
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in commend:
        try:
            look_for = commend.replace('tell me about','')
            about = wikipedia.summary(look_for, 2)
            print(about)
            talk(about)
        except:
            pt = 'Not found in Wikipedia'
            print(pt)
            talk(pt)
    elif 'department' in commend:
            if ('department' and 'how') in commend:
                pt = depermant_info['department']
                print(pt)
                talk(pt)
            elif 'cse department' in commend:
                pt = depermant_info['cse']
                print(pt)
                talk(pt)
            elif 'bba department' in commend:
                pt = depermant_info['bba']
                print(pt)
                talk(pt)
            elif 'pharmacy department' in commend:
                pt = depermant_info['pharmacy']
                print(pt)
                talk(pt)
    elif 'admission' in commend:
            if 'graduate' in commend:
                pt = admission_info['graduate']
                print(pt)
                talk(pt)
            else:
                pt = admission_info['Undergraduate']
                print(pt)
                talk(pt)
    elif 'club' in commend:
            if 'cse club' in commend:
                pt = club_info['cse club']
                print(pt)
                talk(pt)
            elif 'bba club' in commend:
                pt = club_info['bba club']
                print(pt)
                talk(pt)
            elif 'Pharmacy club' in commend:
                pt = club_info['Pharmacy club']
                print(pt)
                talk(pt)
            elif ('club' and 'how') in commend:
                pt = club_info['club']
                print(pt)
                talk(pt)
    elif 'financial' in commend:
        pt = club_info['Financial discount']
        print(pt)
        talk(pt)
    elif 'stop' in commend:
        exit()
    else:
        pt = "Please say it again i don't understand"
        print(pt)
        talk(pt)

while True:
    run_urro()