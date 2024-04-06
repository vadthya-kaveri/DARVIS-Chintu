import os
import pyttsx3
import speech_recognition
import requests
import bs4
from bs4 import BeautifulSoup
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
#creating alarm
def alarm(query):
    timehere = open("alarm.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "hey" in query:
            from greets import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "sleep" in query:
                    speak("Ok Kavya , You can call me anytime")
                    break
                elif "hello" in query:
                    speak("Hello Kavya, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, Kavya")
                elif "how are you" in query:
                    speak("Perfect, Thankyou Kavya")
                elif "thank you" in query:
                    speak("you are welcome, Kavya")

                elif "open" in query:
                    from openintrnlapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from openintrnlapp import closeappweb
                    closeappweb(query)
                elif "google" in query:
                    from search import searchGoogle

                    searchGoogle(query)
                elif "youtube" in query:
                    from search import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from search import searchWikipedia
                    searchWikipedia(query)
                elif "temperature" in query:
                    search = "temperature in your area"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in your area"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current{search} is {temp}")

                  #alarm command
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,Kavya")


                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Kavya, the time is {strTime}")
                elif "chintu sleep" in query:
                    speak("Going to sleep,Kavya")
                    exit()


