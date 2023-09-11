import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyaudio
import random

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
    speak("  I'm jarvis your helper assistanc . how can I help you?  ")

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
    except Exception as e :
        print(" sorry , could not understand . please can you say that again ")
        return ""
    return query

def answer_random_question():
    # دالة للاجابة على الاسلئة العشوائية
    random_answers = [
        " I'm sorry I don't have answer for that.",
        "I'm still learning and Idon't have information for this topic.",
        " I'm afraid I can't  help with that question.",
        " I don't know the answer to that question. ",
        "I'm  sorry I'm not programmed to answer that question."
    ]
    speak(random.choice(random_answers))

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
        elif 'quti' in query:
            speak("good bye")
            break
