import pyttsx3
import datetime
from datetime import date
import calendar
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import wolframalpha
from selenium import webdriver
import requests
import json
import re
# #chrome path for webbrowser
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# webbrowser.get(using='google-chrome')
#-------------------
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
print(voices)
#print("Hello World!")
#print(voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('voices', voices[1].id) 
engine.setProperty('rate', 125)

#-------------------registering GOOGLE CHROME as the default web browser

# urL='https://www.google.com'
chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
# webbrowser.get('chrome').open_new_tab(urL)

def speak(audio): 
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    '''
Flow is greeting -> time -> temp.
    '''
#Greetings

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning RK!")
    elif hour>=12 and hour <17:
        speak("Good Afternoon RK!")
    else:
        speak("Good Evening RK!")

    speak("Welcome Back, I am online and at your service")    

# time and temp
    if hour<=9:
        strTime = datetime.datetime.now().strftime('%H:%M:%S')
        speak(f"The time is {strTime}")
        

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print("User said: ", query)
    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query

#--------------------------------------Main Fucntion-----------------------------------------------
if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
         #logic for executing tasks based on tasks
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        # elif 'open google' in query:
        #     webbrowser.get('chrome')
        #     webbrowser.open("google.com")

        # elif 'open stackoverflow' in query:
            
        #     webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            path = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'weather' in query or 'climate' in query:
            api = "35616db78b18e96c8cdb499df35db2d4"
            base = "http://api.openweathermap.org/data/2.5/weather?"
            speak('Which city Sir?')
            print("Which city?")
            city = takeCommand()
            url = base+"q="+city+"&appid="+api+"&units=metric"
            response=requests.get(url)
            if response.status_code == 200:
                data = response.json()
                main = data['main']
                temp = main["temp"]
                report = data["weather"]
                print(f"City: {city}")
                print(f"Temperature: {temp}")
                print(f"Weather report: {report[0]['description']}")
                speak(f"The current temperature in {city} is {temp} celsius")
            else:
                print("Error")
        
        
        
        
        elif 'bye' in query or 'quit' in query or 'thank you' in query or 'thanks' in query:
            speak("Until next time Sir!, Have a good one.")
            print("Until next time Sir!, Have a good one.")
            break


        
        