import pyttsx3 
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
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
                    speak("Currently running on my full potential. The HMM network is at its full bandwidth")
                elif "Can you check the the RNN status report" in query:
                    speak("The HMM tests are running succesfully, this time I scored 8764 out of ten thousand test cases . May I mail you the results sir")
                elif "model status" in query:
                    speak("The diagnosis were not upto the marks sir . I am still unable to work on myself ! Sorry for the underperformance")