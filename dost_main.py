import pyttsx3 
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening Sir")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 5)
    try:
        print("Understanding..")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"You said : {query}")
    except Exception as e :
        print("Say that again")
        return "None"
    return query

if __name__ == "__main__" :
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True: 
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Gratitude towards you Sir . Thank you for using me")
                    break

                elif "hello" in query:
                    speak("Greetings sir, How may I help you ?")
                elif "what's your status" in query:
                    speak("Currently running on my full potential. The markov model network is at its full bandwidth")
                elif "give me the test results" in query: 
                    speak("this time i scored 8972 out of ten thousand test cases .")
                elif "model status" in query:
                    speak("The diagnosis were not upto the marks sir . I am still unable to work on myself ! Sorry for the underperformance")
                elif "ok thank you for the information" in query:
                    speak("welcome sir")

                elif "open" in query:
                    


                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWiki
                    searchWiki(query)


                elif "temprature" in query: 
                    search = "temprature in varanasi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current {search} is {temp}")
                elif "weather" in query: 
                    search = "temprature in varanasi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current {search} is {temp}")
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir the time is {strTime}")
                elif "finally sleep" in query:
                    speak("Going to sleep ")
                    exit()