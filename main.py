import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import os
import pyautogui




engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
#print(voice[1].id)
engine.setProperty('voice', voice[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Kshama!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Kshama!")

    else:
        speak("Good Evening Kshama!")
    speak("how may i help you")



def takeCommand():
    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: , {query}\n")

    except Exception as e:
        #print (e)

        print("Say that again please...")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Kshama, What should i search for you")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")


        elif 'open stackoverflow' in query:
            webbrowser.open("stackoerflow.com")

        elif 'chrome' in query:
            webbrowser.open("C:\Program Files\Google\Chrome\Application\chrome.exe")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Kshama, the time is {strTime}")

        elif 'song on youtube' in query:
            pywhatkit.playonyt("see you again")

        elif 'you can sleep' in query:
            speak("thanks kshama!, have a good day")
            sys.exit()

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'shutdown the system' in query:
            os.system("shutdown /r /t 5")

        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")

        elif 'send a whatsapp message' in query:
            pywhatkit.sendwhatmsg_instantly("+917033505450", "this is bot generated message", 14)
            time.sleep(120)
            speak("message sent")

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")






