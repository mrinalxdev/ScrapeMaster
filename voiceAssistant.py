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
            data = recognizer.recognizer_google(audio)
            print(data)
        except sr.UnknownValueError:
            print("Not Understanding")