# pip install pyttsx3 SpeechRecognition pyaudio
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Female voice
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language="en-in")
            print(f"User said: {command}\n")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I could not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

def run_assistant():
    speak("Hello, I am your assistant. How can I help you?")

    while True:
        query = listen()


        if "time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")


        elif "exit" in query or "quit" in query:
            speak("Goodbye! Have a nice day.")
            break