import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import subprocess
# بناء المحرك الصوتي
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# تهيئة المعرفة الصوتية
recognizer = sr.Recognizer()

def speak(audio):
    # دالة تحويل النص لصوت
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    # دالة لتحية المستخدم بناءً على الوقت
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    name = input("Enter your name: ")
    if name:
        speak(f"Hello {name}, I'm Jarvis, your assistant. How can I help you?")
    else:
        print("Please enter your name.")

def take_command():
    # دالة لاستقبال الأوامر الصوتية من المستخدم
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en')
        print(f"User said: {query}\n")
    except Exception as e:
        speak("Sorry, could not understand. Please say that again.")
        return ""

    return query

if __name__ == "__main__":
    wish_me()

    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {str_time}")
        elif 'open pinterest' in query:
            webbrowser.open("https://www.pinterest.com")
        elif 'open discord' in query:
            webbrowser.open("https://www.discord.com")
        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
        elif 'open visual studio code' in query:
            webbrowser.open("https://code.visualstudio.com")
        elif 'close' in query:
            speak("Goodbye")
