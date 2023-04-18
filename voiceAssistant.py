import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes 


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening Broda...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing your Voice ....")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understanding")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__': 
    if sptext().lower() == "are you there":
        data1 = sptext().lower()
        if "your name" in data1:
            name = "My name is Dost, thanks for asking me such a beautiful question"
            speechtx(name)
        if "who made you" in data1:
            owner = "I have been designed and created by Mrinal Pramanick. My basic knowledge has been provided by the open source software commonly known as Convovational Neural Network. On the deeper knowledge of the things Mrinal is working with RNN's machine learning model"
        if "why are you there" in data1:
            reason = "Mrinal is buidling me, a voice assistant named as DOST to provide rural areas a knowledge of voice assistant and the upcoming future, I think after introduction to RNN's model my build will be successfull from 1 half. After getting enough training from the model, I will be training myself. I am ready to help everyone at their go !"
    else:
        print("Thanks for making me")
