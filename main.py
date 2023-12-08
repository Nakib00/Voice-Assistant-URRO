import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
# from independent_data import club_info, depermant_info, admission_info, lab_info, school_info,bilding_info


# IUB Data set
club_info = {
    'club':'Independent University, Bangladesh (IUB) has a wide range of clubs and organizations that cater to the diverse interests of its students. These clubs provide a platform for students to pursue their passions, develop their skills, and connect with others who share their interests.Here are some of the most popular clubs at IUB: IUB Business Club, IUB Film Club, IUB Music Club, IUB Photography Club, IUB Sports Club, IUB Theater Club, IUB Toastmasters Club',

    'cse club': 'The Department of Computer Science and Engineering (CSE) at Independent University, Bangladesh (IUB) has three active clubs:Jukti,IUB ACM Student Chapter,IEEE Computer Society',

    'bba club': 'Here are the clubs under the School of Business and Entrepreneurship (SBE) of Independent University, Bangladesh (IUB):Business Students Society (BSS), Independent Beta Elites (IBE), Independent Economic Society (IES), Independent HR Society (IHRS),IUB E-Business Club, Independent Managerial Society (IMS), Independent Marketers Association (IMA)',

    'Pharmacy club': "The Pharmacy Department at Independent University, Bangladesh (IUB) has one active club: IUB Pharma Club, The IUB Pharma Club is a platform for students to share their knowledge and interests in pharmacy. The club organizes a variety of events throughout the year, such as seminars, workshops, competitions, and conferences. The club also publishes a biannual journal, the IUB Pharma Journal, which showcases the research work of pharmacy students at IUB.",

    'Financial discount': 'Independent University, Bangladesh (IUB) offers a variety of financial discounts to help students afford the cost of tuition. These discounts are based on merit, need, and other factors.Merit-based scholarshipsIUB offers a number of merit-based scholarships to students with outstanding academic records. These scholarships are awarded to students who have achieved a high GPA in their previous studies.Need-based financial assistanceIUB offers need-based financial assistance to students who demonstrate financial need. This assistance can be in the form of grants, loans, or work-study opportunities.Sibling discountsIUB offers a 50% tuition discount to siblings of current IUB students.Employee discounts IUB offers a 10% tuition discount to children of IUB employees.Alumni discounts IUB offers a 10% tuition discount to children of IUB alumni. Early bird discounts IUB offers a 5% tuition discount to students who apply and pay their tuition fees early. Referral discounts IUB offers a 5% tuition discount to students who refer new students to IUB. For more information on financial discounts, please visit the IUB website or contact the Financial Aid Office.',
}

depermant_info = {
    'department': 'Independent University, Bangladesh (IUB) has 12 departments:Department of Business Administration (BBA),Department of Economics,Department of English and Modern Languages,Department of Law,Department of Media and Communication,Department of Pharmacy,Department of Public Health,Department of Social Sciences,Department of Computer Science and Engineering (CSE),Department of Electrical and Electronic Engineering (EEE),Department of Civil and Environmental Engineering (CEE),In addition to these departments, IUB also has a number of centers and institutes, such as the Center for Excellence in Journalism (CEJ), the Institute for Development Studies (IDS), and the Institute for Business Research (IBR).',

    'cse': 'The Department of Computer Science and Engineering (CSE) at Independent University, Bangladesh (IUB) is a leading center for computing education and research in Bangladesh. The department offers a four-year Bachelor of Science (BSc) program in Computer Science and Engineering, as well as a two-year Master of Science (MSc) program in Computer Science.The BSc program is designed to provide students with a solid foundation in the theoretical and practical aspects of computer science and engineering. The program covers a wide range of topics, including:Programming languagesData structures and algorithmsSoftware engineeringComputer architectureOperating systemsDatabasesNetworkingArtificial intelligenceMachine learning. The CSE department has a distinguished faculty of experienced and well-qualified teachers who are committed to providing students with the best possible education. The department also has a strong research program, with faculty members actively engaged in research in a variety of areas.',

    'eee': 'The Department of Electrical and Electronic Engineering (EEE) at Independent University, Bangladesh (IUB) is a leading center for electrical and electronic engineering education and research in Bangladesh. The department offers a four-year Bachelor of Science (BSc) program in Electrical and Electronic Engineering, as well as a two-year Master of Science (MSc) program in Electrical and Electronic Engineering.The Department of Electrical and Electronic Engineering (EEE) at Independent University, Bangladesh (IUB) is a leading center for electrical and electronic engineering education and research in Bangladesh. The department offers a four-year Bachelor of Science (BSc) program in Electrical and Electronic Engineering, as well as a two-year Master of Science (MSc) program in Electrical and Electronic Engineering.Circuit theoryElectromagnetism ElectronicsPower systemsControl systems Communication systems Computer engineering Microprocessors Digital signal processing',

    'bba': "Independent University Bangladesh (IUB) BBA department is one of the oldest and most prestigious business schools in Bangladesh. The department offers a four-year undergraduate program that is designed to prepare students for careers in business and management. The program covers a wide range of topics, including accounting, finance, marketing, human resources, and management information systems. The department has a strong focus on practical application, and students are required to complete internships and projects as part of their coursework. The BBA department has a distinguished faculty of experienced and well-qualified teachers. The department also has a strong alumni network that provides students with valuable support and guidance.",

    'economics': 'The Economics department at Independent University Bangladesh is a top-notch program that offers a comprehensive education in economics. The department has a strong focus on both theoretical and applied aspects of the field, and students are given the opportunity to conduct research and develop their own projects. The Economics department has a distinguished faculty of experienced and well-qualified teachers who are committed to providing students with the best possible education. The department also has a strong alumni network that provides students with valuable support and guidance.',

    'pharmacy': 'The Department of Pharmacy at Independent University, Bangladesh (IUB) offers a four-year Bachelor of Pharmacy (BPharm) program that is designed to prepare students for careers in the pharmaceutical industry. The program covers a wide range of topics, including pharmaceutical chemistry, pharmacology, pharmaceutics, and pharmacy practice. Students are also given the opportunity to conduct research and develop their own projects.Graduates of the BPharm program are eligible to take the Bangladesh Pharmacy Council licensure examination. Upon passing the examination, they are qualified to practice as pharmacists in Bangladesh.In addition to the BPharm program, the Department of Pharmacy also offers a number of non-degree training programs in areas such as HPLC, GC-MS, LC-MS, AAS, and NMR. These programs are designed to provide professionals with the skills they need to use these advanced analytical techniques.',
}

admission_info = {
    'Undergraduate':"Admission Requirements,Combined GPA of 7 in SSC and HSC with a minimum GPA of 3 in each O'Level in minimum 5 subjects with a GPA of 2.50 and A'Level in 2 subjects with a minimum GPA of 2.00 International Baccalaureate or U.S. High School Diploma Other 12 years equivalent degree (must have the equivalence certificate from Ministry of Education)",

    'graduate': "Bachelor's degree from a recognized university with a minimum CGPA of 3.00 GRE or GMAT scores (optional)",
}

lab_info ={
    'lab':'There are 27 labs in Independent University, Bangladesh (IUB). The list of labs are as follows:Advanced Materials Processing Lab,Bioinformatics Lab, Chemistry Lab, Computer Vision Lab, Data Science Lab , Electronics Lab, Fab Lab , Mechanical Engineering Lab, Physics Lab, Robotics Lab, Software Engineering Lab, Biochemistry Lab , Microbiology Lab,Biotechnology Lab, Food Science and Technology Lab, Pharmacy Lab, Public Health Lab, Environmental Science Lab, Geography Lab, Geography Lab, Media Lab, Language Lab, Psychology Lab, Sociology Lab, Economics Lab, Finance Lab, Accounting Lab',
    
}

school_info = {
    'school':'Independent University, Bangladesh (IUB) has 5 schools: School of Business and Entrepreneurship (SBE) ,School of Engineering, Technology, and Sciences (SETS) ,School of Environment and Life Sciences (SELS), School of Liberal Arts and Social Sciences (SLASS) ,School of Pharmacy and Public Health (SPPH) ',

    'sbe':'The School of Business and Entrepreneurship (SBE) at Independent University, Bangladesh (IUB) has 8 departments:Accounting,Economics,Finance,General Management,Human Resource Management,International Business,Management Information Systems,Marketing ',

    'sets': 'The School of Engineering, Technology and Sciences (SETS) at Independent University, Bangladesh (IUB) has three departments. These are: Computer Science and Engineering (CSE), Electrical and Electronic Engineering (EEE), Physical Sciences (PS)',

    'sels':'The School of SELS is the School of Environment and Life Sciences, which has two departments. These are:Department of Life Sciences,Department of Environmental Science and Management',

    'slass':' the School of Liberal Arts and Social Sciences (SLASS) has five departments1. These are:English,Global Studies and Governance,Law,Media and Communication,Social Sciences and Humanities',

    'spph':'the School of Pharmacy and Public Health (SPPH) at Independent University, Bangladesh (IUB) has two departments1. These are: Department of Pharmacy,Department of Public Health'
}

bilding_info ={
    'c':'Lats go with me. BC Bilding is the mani bilding in IUB. it has three parts.Left, Right and Font side. Left side have all the office of univirsity. Font side have canteen and library. Right side have all class rooom and department.'
}

#Init
listener = sr.Recognizer()
urro = pyttsx3.init()
voices = urro.getProperty('voices')
urro.setProperty('voice',voices[1].id)

#talk the assisttant 
def talk(text):
    urro.say(text)
    urro.runAndWait()

#commend take from voice
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

# Set the initial rest position of the servo
set_servo_rest_position()

# All handler function
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
        move_forward()
        sleep(5)
        stop_motors()
        turn_left()
        sleep(5)
        stop_motors()
        move_forward()
        sleep(5)
        stop_motors()
    

def how_are_you_handler(commend):
    pt = "I am fine, what about you?"
    print(pt)
    talk(pt)

def unknown_handler():
    pt = "Please say it again i don't understand"
    print(pt)
    talk(pt)

# Take the commend and call right handler function
def run_urro():
    commend = take_commend()
    if 'time' in commend:
        time_handler()
    elif 'play' in commend:
        play_handler(commend)
    elif 'tell me about' in commend:
        wikipedia_handler(commend)
    elif 'how are you' in commend:
        how_are_you_handler(commend)
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

# Loop run run_ueeo() function
while True:
    run_urro()