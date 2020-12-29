import pyttsx3
import datetime
import speech_recognition as sr 
import pyaudio
import wikipedia
import webbrowser
import os
import sys
#from youtube_search import youtubesearch as ytsearch
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[1].id)
#print(voices[1])

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening........")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("recognizing......")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        #print(e)
        speak("say that again")
        print("say that again")
        return "None"
    return query
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("hello and good morning boss.......how are you today.")
    elif hour>=12 and hour <18:
        speak("good evening boss.......you are late to work today")
    else:
        speak("goodnight sir .........it was really hectic today")
if True:
    wishMe()
    
    
    while True:
        query=takecommand().lower()
        if 'work late' in query:
            speak(" What can i do for you?")
        elif 'wikipedia' in query:
            query=query.replace("wikipedia","") 
            results=wikipedia.summary(query, sentences=5)
            speak("According to wikipedia")
            speak(results)
            print(results)
        elif 'open youtube' in query:
            print(query)
            webbrowser.open("https://www.youtube.com/")
        
        elif 'good night' in query:
            speak("good night boss")
        elif ' ' in query:
            speak("if there is nothing more to do then let me sleep boss")    
        #elif 
