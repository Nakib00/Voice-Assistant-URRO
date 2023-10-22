import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
from independent_data import club_info, depermant_info, admission_info, lab_info, school_info,bilding_info


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
        time_handler()
    elif 'play' in commend:
        play_handler(commend)
    elif 'tell me about' in commend:
        wikipedia_handler(commend)
    elif 'department' in commend:
        department_handler(commend)
    elif 'admission' in commend:
        admission_handler(commend)
    elif 'club' in commend:
        club_handler(commend)
    elif 'financial' in commend:
        financial_handler(commend)
    elif 'lab' in commend:
        lab_handler(commend)
    elif 'school' in commend:
        school_handler(commend)
    elif 'building' in commend:
        bilding_handler(commend)
    elif 'stop' in commend:
        exit()
    else:
        unknown_handler()

def time_handler():
    time = datetime.datetime.now().strftime('%H:%M %p')
    print(time)
    talk('Current time is' + time)

def play_handler(commend):
    song = commend.replace('play', '')
    talk("playing" + song)
    pywhatkit.playonyt(song)

def wikipedia_handler(commend):
    try:
        look_for = commend.replace('tell me about','')
        about = wikipedia.summary(look_for, 2)
        print(about)
        talk(about)
    except:
        pt = 'Not found in Wikipedia'
        print(pt)
        talk(pt)

def department_handler(commend):
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

def admission_handler(commend):
    if 'graduate' in commend:
        pt = admission_info['graduate']
        print(pt)
        talk(pt)
    else:
        pt = admission_info['Undergraduate']
        print(pt)
        talk(pt)

def financial_handler(commend):
    pt = club_info['Financial discount']
    print(pt)
    talk(pt)

def club_handler(commend):
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

def school_handler(commend):
    if ('school' and 'how') in commend:
        pt = school_info['school']
        print(pt)
        talk(pt)
    elif 'engineering' in commend:
        pt = school_info['sets']
        print(pt)
        talk(pt)
    elif ('business' or 'entrepreneurship') in commend:
        pt = school_info['sbe']
        print(pt)
        talk(pt)
    elif ('pharmacy' or ('public' and 'health')) in commend:
        pt = school_info['spph']
        print(pt)
        talk(pt)
    elif (('social' and 'science') or ('aiberal' and 'art')) in commend:
        pt = school_info['slass']
        print(pt)
        talk(pt)
    elif ('environment' or ('life' and 'science')) in commend:
        pt = school_info['sels']
        print(pt)
        talk(pt)

def lab_handler(commend):
    if ('lab' and 'how') in commend:
        pt = lab_info['lab']
        print(pt)
        talk(pt)

def bilding_handler(commend):
    if ('where' or 'c') in commend:
        pt = bilding_info['c']
        print(pt)
        talk(pt)

def unknown_handler():
    pt = "Please say it again i don't understand"
    print(pt)
    talk(pt)

while True:
    run_urro()