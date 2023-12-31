from gtts import gTTS
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

def speak(audio):
    tts = gTTS(text=audio, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am jarvis  Sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I could not understand. Please repeat.")
            return "None"
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return "None"

def sendEmail(to, content):
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.ehlo()
            server.starttls()
            server.login('youremail@gmail.com', 'your-password')
            server.sendmail('youremail@gmail.com', to, content)
        print("Email has been sent!")
    except smtplib.SMTPException as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
            speak("youtube is open now")

        elif 'open google' in query:
            webbrowser.open("https://google.com")
            speak("google is open now")

        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com")
            speak("stackoverflow is open now")
        elif 'open four ways' in query:
            webbrowser.open("https://fourways.net")
            speak("fourways is open now")
        elif 'open chat gpt' in query:
            webbrowser.open("https://chat.openai.com")
            speak("chatgpt is open now")

        elif 'play music' in query:
            webbrowser.open("https://open.spotify.com")
            speak("spotify is open now")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "/Users/pratyushsharma/Documents/main projects/jarvis.py"
            os.system("code " + codePath)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ironfist2710@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Pratyush bhai. I am not able to send this email")
        elif 'news' in query:
            webbrowser.open("https://www.hindustantimes.com")
            speak("here are some interesting headlines")
        elif 'hello' in query:
            speak("Hello sir how may i help you")
        elif 'jarvis' in query:
            speak("Yes Sir how may i help you")
        elif 'Alexa' in query:
            speak("Not exactly. but i offer no resistance to helpfull assistants")
        elif 'today is my birthday' in query:
            speak("Happy Birthday Naresh")
        elif 'stop' in query:
            speak("Bye Bye")
            break
        