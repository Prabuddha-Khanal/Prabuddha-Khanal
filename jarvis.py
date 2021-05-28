import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import mysql.connector
from googlesearch import search
from routine import clas
from join import c

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("rate", 200)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("what do you want me to do")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('samssmith6060@gmail.com', 'n0password')
    server.sendmail('samssmith6060@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'jarvis open youtube' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("youtube.com")

        elif 'jarvis open facebook' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("facebook.com")

        elif 'jarvis open my youtube channel' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("youtube.com/channel/UCcKMFPWMxijuk2hPAnDp2sw")

        elif 'jarvis open google' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")

        elif 'start the meeting' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://us04web.zoom.us/j/3808012742?pwd=MnBCRzFaejFmSnJXY3UzYkVBV2NEZz09")

        elif 'jarvis youtube' in query:
            query = query.replace("youtube", "")
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.youtube.com/results?search_query=" + query)

        elif 'jarvis join class' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(c)

        elif 'jarvis open zoom' in query:
            path = 'C:/Users/dell/AppData/Roaming/Zoom/bin/zoom.exe'
            os.startfile(path)

        elif 'jarvis filmora' in query:
            path = 'C:\Program Files\Wondershare\Wondershare Filmora\Wondershare Filmora9.exe'
            os.startfile(path)

        elif 'jarvis how are you' in query:
            print("fine, how about you")
            speak("fine, how about you")

        elif 'jarvis who are you' in query:
            print("I am Jarvis")
            speak("I am Jarvis")

        elif 'jarvis you speak nepali' in query:
            speak("malai aaunca")
        
        elif 'jarvis who made you' in query:
            print("I was made by Prabu Vlogs in oct 12 2020")
            speak("I was made by Prabuddha in october 12 2020")


        elif 'jarvis play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'jarvis whats the time' in query:
            hour = datetime.datetime.now().strftime("%M")
            minute = datetime.datetime.now().strftime("%M")
            am = datetime.datetime.now().strftime("%p")  
            speak(f"Sir, the time is {hour+minute+am}")

        elif 'jarvis open chrome' in query:
            codePath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
            os.startfile(codePath)

        elif 'jarvis send email to harry' in query:
            try:
                speak("What should I send?")
                content = takeCommand()
                to = "harikhanal.com.np@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")

        elif 'jarvis good night' in query:
            print("ok goodnight")
            speak("ok goodnight")

        elif 'jarvis open minecraft' in query:
            codePath = "C:/Users/dell/AppData/Roaming/.minecraft/TLauncher.exe"
            os.startfile(codePath)

        elif 'jarvis what' in query:
            speak('Searching Wikipedia...')
            query = query.replace("", "")
            results = wikipedia.summary(query, sentences=2)
            speak("ok")
            print(results)
            speak(results)

        elif 'jarvis who' in query:
            speak('Searching Wikipedia...')
            query = query.replace("", "")
            results = wikipedia.summary(query, sentences=2)
            speak("ok")
            print(results)
            speak(results)

        elif 'jarvis which class' in query:
            print(f"You have {clas}")
            speak(f"you have {clas}")