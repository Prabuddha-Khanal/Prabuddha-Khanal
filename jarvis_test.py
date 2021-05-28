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
import time

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
    text = input("Text = ")

    try:
        query = text

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

        if 'open youtube' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("youtube.com")

        elif 'open facebook' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("facebook.com")

        elif 'open my youtube channel' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("youtube.com/channel/UCcKMFPWMxijuk2hPAnDp2sw")

        elif 'open google' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")

        elif 'meeting' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://us04web.zoom.us/j/3808012742?pwd=MnBCRzFaejFmSnJXY3UzYkVBV2NEZz09")

        elif 'youtube' in query:
            query = query.replace("youtube", "")
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.youtube.com/results?search_query=" + query)

        elif 'class' in query:
            speak(f"you {clas}")
            print(f"you {clas}")
            if clas=='do not have class right now':
                print('')
            else:
                speak('do you want to join, yes or no')
                i = input('do you want to join (yes/no) ')
                if i== 'yes':
                    speak('joining')
                    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(c)
                    time.sleep(1)                              
                    os.system("TASKKILL /F /IM chrome.exe")
                elif i=='no':
                    print('ok')
                else:
                    print("")

        elif 'open zoom' in query:
            path = 'C:/Users/dell/AppData/Roaming/Zoom/bin/zoom.exe'
            os.startfile(path)

        elif 'filmora' in query:
            path = 'C:\Program Files\Wondershare\Wondershare Filmora\Wondershare Filmora9.exe'
            os.startfile(path)

        elif 'how are you' in query:
            speak("fine, how about you")
            speak("fine, how about you")

        elif 'who are you' in query:
            speak("I am Jarvis")
            speak("I am Jarvis")

        elif 'you speak nepali' in query:
            speak("malai aaunca")
        
        elif 'who made you' in query:
            speak("I was made by Prabu Vlogs in oct 12 2020")
            print("I was made by Prabuddha in october 12 2020")

        elif 'play music' in query:
            music_dir = 'C:/Users/dell/Music/Playlists/all prabu'
            songs = os.listdir(music_dir)
            speak(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'whats the time' in query:
            hour = datetime.datetime.now().strftime("%M")
            minute = datetime.datetime.now().strftime("%M")
            am = datetime.datetime.now().strftime("%p")
            speak(f"Sir, the time is {hour+minute+am}")

        elif 'open chrome' in query:
            codePath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
            os.startfile(codePath)

        elif 'send email to harry' in query:
            try:
                speak("What should I send?")
                content = takeCommand()
                to = "harikhanal.com.np@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak(e)
                speak("Sorry. I am not able to send this email")

        elif 'good night' in query:
            speak("ok goodnight")
            print("ok goodnight")

        elif 'open minecraft' in query:
            codePath = "C:/Users/dell/AppData/Roaming/.minecraft/TLauncher.exe"
            os.startfile(codePath)

        elif 'what' in query:
            query = query.replace("", "")
            results = wikipedia.summary(query, sentences=2)
            speak("ok")
            print(results)
            speak(results)

        elif 'who' in query:
            query = query.replace("", "")
            results = wikipedia.summary(query, sentences=2)
            speak("ok")
            print(results)
            speak(results)
