import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyaudio
import random
import subprocess

#  بناء المحرك الصوتي
enging = pyttsx3.init('sapi5')
voices =enging.getProperty('voices')
enging.setProperty('voice',voices[0].id)

def speak(audio):
    # دالة تحويل النص لصوت 
    enging.say(audio)
    enging.runAndWait()

def wish_me():
    #  دالة لتحية المستخدم بناء على الوقت
    hour= datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak ("good morning !")
    elif 12 <= hour <18:
        speak ("good afternoon !")
    else:
        speak ("good evening !")
    speak("  hello I'm jarvis your helper assistanc . how can I help you?  ")

def take_command ():
    # دالة لاستقبال الاوامر الصوتية من المستخدم
    recognizer=sr.Recognizer()
    with sr.Microphone() as source :
        print ("listening...")
        recognizer.pause_threshold =1
        audio = recognizer.listen(source)

    try :
        print("Recognizing...")
        query = recognizer.recognize_google(audio,language ='en')
        print(f"user said :{query}/n")
    except Exception as e:
        print(" sorry , could not understand . please can you say that again ")
        return ""
    return query

# def answer_random_question():
#     # دالة للاجابة على الاسلئة العشوائية
#     random_answers = [
#         " I'm sorry I don't have answer for that.",
#         "I'm still learning and Idon't have information for this topic.",
#         " I'm afraid I can't  help with that question.",
#         " I don't know the answer to that question. ",
#         "I'm  sorry I'm not programmed to answer that question."
#     ]
#     speak(random.choice(random_answers))


if __name__=="__main__":
    wish_me()
    while True :
        query = take_command().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia.....')
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences =2)
            print(results)
            speak(results)
        elif'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        elif'open google'in query:
            webbrowser.open("https://google.com")
        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {str_time}")  
        elif 'close' in query:
            speak("good bye")
            break
         #امر جديد افتح برنامج
        elif'open program' in query:
            try:
                program_name =query.split('open program')[1]
                subprocess.Popen(program_name)
                speak(f"open program done :{program_name}")
            except Exception as e:
                speak(" an error occurred,please try again")
                print(f"an error occurred:{str(e)}")
# دالة  لاستكشاف البرامج و استدعائها
def search_programs(query):
    command=f'wmic product where "name like "%{query}%""get name'
    results= subprocess.run(command,capture_output=True,text=True,shell=True)
    output =results.stdout.strip().split('\n')[1:]
    programs = [line.strip() for line in output]
    return programs

def open_program (program_name):
    command= f'start"" "{program_name}"'
    # تنفيذ البحث عن البرامج بواسطة الاستعلام  "google chrome"
    programs = search_programs(" Google chrome")
    
    if programs:
        print(" the following programs are found :")
        for program in programs :
            print(program)

# كود للطلب من المستخدم فتح البرنامج
    selected_program= input("please choose the program you want to open :")
    if selected_program in programs :
        open_program(selected_program)
    else :
        print(" the selected program is incorrect")