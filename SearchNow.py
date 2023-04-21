import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
import sys
sys.stdout.reconfigure(encoding='utf-8')

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

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("dost", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        speak ("This what i got gor your search")

        try : 
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)
        except :
            speak("No speakable output")
        

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your answer")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        query = query.replace("dost", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit(query)
        speak("Done, sir")

def searchWiki(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia", "")
        query = query.replace("search wikipedia", "")
        query = query.replace("dost", "")
        result = wikipedia.summary(query,sentences = 2)
        print(result)
        speak(result)

    