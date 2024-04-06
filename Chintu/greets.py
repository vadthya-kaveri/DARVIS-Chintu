import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,Kavya")
    elif hour >12 and hour<=16:
        speak("Good Afternoon ,Kavya")
    elif hour >16 and hour<=21:
        speak("Good Evening,Kavya")
    else:
        speak("Good Night,Kavya")

    speak("Please tell me, How can I help you ?")