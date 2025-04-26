import os
import google.generativeai as genai
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash") 

chat = model.start_chat()

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak_text(text): 
    tts_engine.say(text)
    tts_engine.runAndWait()

def liste_to_user():
    with sr.Microphone() as source:
        print("Sun Raha ha hu mein...")
        audio = recognizer.listen(source)

        try: 
            user_input = recognizer.recognize_google(audio)
            print(f"You said: {user_input}")
            return user_input
        except sr.UnknownValueError:
            print("Rana Ji maaf karna mujhe samajh nahi aaya.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None
        


while True:
    user_input = liste_to_user()
    if user_input is None:
        continue
    if user_input.lower() == "exit":
        print("Acha Chalta hu Duao me yaad rakhna")
        speak_text("Acha Chalta hu Duao me yaad rakhna")
        break

    response = chat.send_message(user_input)
    print(f"NOVA: {response.text}")
    speak_text(response.text)

