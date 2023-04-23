import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


dictapp = {"commandprompt": "cmd", "chrome": "chrome",
           "vscode": "code", "powerpoint": "powerpnt"}


def openappweb(query):
    speak("Launching Sir...")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("jarvis", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in query:
            os.system(f"start {dictapp[app]}")


def closeappweb(query):
    speak("Closing sir")
    if "one tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("all tabs closed")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("all tabs closed")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("all tabs closed")
        pyautogui.hotkey("ctrl", "w")
        speak("all tabs closed")
