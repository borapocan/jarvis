import pyttsx3
import datetime
import pytz
from pytz import timezone
from datetime import datetime
import speech_recognition as sr
from random import choice
# from utils import opening_text
import pyaudio
import os
import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
# from decouple import config
import geocoder
import urllib
import webbrowser

engine = pyttsx3.init()

def speak(audio):

    engine.say(audio)

    engine.runAndWait()

# speak("How may I help you sir")

print('Date: ' + (datetime.utcnow().strftime('%c')))

speak('Process started...')

def greet_user():

    hour = datetime.utcnow().hour

    if (hour >= 6) and (hour < 12):

        speak(f"Good Morning Sir")

    elif (hour >= 12) and (hour < 16):

        speak(f"Good afternoon Sir")

    elif (hour >= 16) and (hour < 19):

        speak(f"Good Evening Sir")

    #speak(f"I am Jarvis. How may I assist you?")

def time():

    utc_now = datetime.utcnow()

    utc = pytz.timezone('UTC')

    aware_date = utc.localize(utc_now)

    turkey = timezone('Europe/Istanbul')

    now_turkey = aware_date.astimezone(turkey)

    return now_turkey

def findMyLocation():

    location = os.system('curl ipinfo.io')

    speak('For your convenience, I am printing it on the screen sir.')

    print(location)

# time()

def speechRecognition():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        speak("Listening...")

        recognizer.pause_threshold = 0.5

        audio = recognizer.listen(source)

    try:

        speak("Recognizing...")

        query = recognizer.recognize_google(audio, language="en-in")

        print(query)

    except Exception as e:

        speak(e)

        speak("Please say that again...")

        print(e)

        # return "None"

    return query

# speechRecognition()

def open_terminal():

    os.system("/bin/zsh")

def open_calculator():

    os.system('mate-calc')

def open_google():

    os.system("open wwww.google.com.tr")

def open_camera():

    os.system("cheese")

def open_keyboardPractice():

    url = "https://www.keybr.com/"

    webbrowser.open(url)

def findMyIP():

    local = os.system("ip addr show dev $(ip route ls|awk '/default/ {print $5}')|grep -Po 'inet \K(\d{1,3}\.?){4}'")

    public = os.system("echo $(wget -qO - https://api.ipify.org)")

    return local + public

def search_on_wikipedia(query):

    results = wikipedia.summary(query, sentences=2)

    return results

def activateVirtualAssistant():

    user_query = speechRecognition()

    return "user query...", user_query

def play_on_youtube(video):

    kit.playonyt(video)

def search_on_google(query):

    kit.search(query)

def open_discord():

    os.system("discord")

#    if "open terminal" or "open Terminal" in user_query:
#        open_terminal()
#         return
#    if "open google" or "open Google" in user_query:
#        open_google()
#        return

greet_user()

while True:

    query = activateVirtualAssistant()

    if 'open camera' in query:

        open_camera()

    elif "shutdown" in query:

        speak("Terminating the process. Hope to see you soon. Good bye")

        break

    elif 'find my IP' in query:

        speak('For your convenience, I am printing it on the screen sir.')

        local = os.system("ip addr show dev $(ip route ls|awk '/default/ {print $5}')|grep -Po 'inet \K(\d{1,3}\.?){4}'")

        public = os.system("echo $(wget -qO - https://api.ipify.org)")


    elif 'YouTube' in query:

        speak('What do you want to play on Youtube, sir?')

        video = speechRecognition().lower()

        play_on_youtube(video)

    elif 'Wikipedia' in query:

            speak('What do you want to search on Wikipedia, sir?')

            search_query = speechRecognition().lower()

            results = search_on_wikipedia(search_query)

            speak(f"According to Wikipedia, {results}")

            speak("For your convenience, I am printing it on the screen sir.")

            print(results)

    elif 'open calculator' in query:

        open_calculator()

    elif 'find my location' in query:

        findMyLocation()

    elif 'Google' in query:

        speak('What do you want to search on Google, sir?')

        search_query = speechRecognition().lower()

        speak('I will open your search query on Google, sir')

        search_on_google(search_query)

    elif 'what is the date' in query:

        print(datetime.utcnow().strftime('%A %B %Y'))

        speak(datetime.utcnow().strftime('%A %B %Y'))

    elif 'what time is it' in query:

        print(datetime.utcnow().strftime('%X'))

        speak(datetime.utcnow().strftime('%X'))

    elif 'open keyboard practice' in query:

        open_keyboardPractice()

# if __name__ == '__main__':
#
#     greet_user()
#
#     while True:
#
#         query2 = speechRecognition().lower()
#
#         if "open discord" or "open Discord" in query2:
#
#             open_discord()
#
#         elif 'open camera' in query2:
#
#             open_camera()
#
#         else:
#
#             speechRecognition()
#