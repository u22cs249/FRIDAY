import speech_recognition as sr
import pyttsx3
import os
import datetime
import subprocess
import sys
import pywhatkit 
import eel
from engine.features import *
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer  = sr.Recognizer() 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_software(software_name):
    if 'microsoft edge' in software_name:
        eel.DisplayMessage('Opening Microsoft Edge...')
        speak('Opening Microsoft Edge...')
        program = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        subprocess.Popen([program])
    elif 'chrome' in software_name:
        eel.DisplayMessage('Opening Chrome...')
        speak('Opening Chrome...')
        program = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([program])
    elif 'opera' in software_name:
        eel.DisplayMessage('Opening Opera Mini...')
        speak('Opening Opera Mini...')
        program = r"C:\Users\91877\AppData\Local\Programs\Opera\opera.exe"
        subprocess.Popen([program]) 
    elif 'excel' in software_name:
        eel.DisplayMessage('Opening Excel...')
        speak('Opening Excel...')
        program = r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
        subprocess.Popen([program])
    elif 'word' in software_name:
        eel.DisplayMessage('Opening MS Word...')
        speak('Opening MS Word...')
        program = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
        subprocess.Popen([program])
    elif 'notepad' in software_name:
        eel.DisplayMessage('Opening Notepad...')
        speak('Opening Notepad...')
        subprocess.Popen(['notepad.exe']) 
    elif 'calculator' in software_name:
        eel.DisplayMessage('Opening Calculator...')
        speak('Opening Calculator...')
        subprocess.Popen(['calc.exe'])
    else:
        eel.DisplayMessage(f"I couldn't able to find the software {software_name}")
        speak(f"I couldn't able to find the software {software_name}")

def close_software(software_name):
    if 'microsoft edge' in software_name:
        eel.DisplayMessage('Closing Microsoft Edge...')
        speak('Closing Microsoft Edge...')
        os.system("taskkill /f /im msedge.exe")
    elif 'chrome' in software_name:
        eel.DisplayMessage('Closing Chrome...')
        speak('Closing Chrome...')
        os.system("taskkill /f /im chrome.exe")
    elif 'opera mini' in software_name:
        eel.DisplayMessage('Closing Opera Mini...')
        speak('Closing Opera Mini...')
        os.system("taskkill /f /im opera.exe")
    elif 'excel' in software_name:
        eel.DisplayMessage('Closing Excel...')
        speak('Closing Excel...')
        os.system("taskkill /f /im excel.exe")
    elif 'word' in software_name:
        eel.DisplayMessage('Closing MS Word...')
        speak('Closing MS Word...')
        os.system("taskkill /f /im WINWORD.exe")
    elif 'notepad' in software_name:
        eel.DisplayMessage('Closing Notepad...')
        speak('Closing Notepad...')
        os.system("taskkill /f /im notepad.exe")
    elif 'calculator' in software_name:
        eel.DisplayMessage('Closing Calculator...')
        speak('Closing Calculator...')
        os.system("taskkill /f /im Calc.exe")
    else:
        eel.DisplayMessage(f"I couldn't find any opened software named {software_name}")
        speak(f"I couldn't find any opened software named {software_name}")

def listen_for_wake_word():
    with sr.Microphone() as source:
        eel.DisplayMessage('Listening for wake word...!!!')
        speak("Listening for wake word...!!!")
        print('Listening for wake word...')
        while True:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            recorded_audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(recorded_audio, language='en_US')
                text = text.lower()
                if 'friday' in text:
                    eel.DisplayMessage('Wake word detected!')
                    print('Wake word detected!')
                    eel.DisplayMessage('Hi Sir, How can I help you?')
                    speak('Hi Sir, How can I help you?')
                    return True
            except Exception as ex:
                eel.DisplayMessage('Could not understand the audio!, please say again.')
                print("Could not understand the audio!, please say again.")
                speak("Could not understand the audio!, please say again.")

def cmd():
    with sr.Microphone() as source:
        print('Clearing background noise... please wait!')
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        eel.DisplayMessage('You can Ask me something...!')
        print('Ask me anything...')
        recorded_audio = recognizer.listen(source)
    try:
        eel.DisplayMessage('recognizing.....!')
        text = recognizer.recognize_google(recorded_audio, language='en_US')
        text = text.lower()
        #eel.DisplayMessage(text)
        print('recognizing.....!')
        print('Your message:', text)
    except Exception as ex:
        print(ex)
        return
    if 'open' in text:
        software_name = text.replace('open', '').strip()
        open_software(software_name)
    if 'stop' in text:
        eel.DisplayMessage('Stopping the program.')
        speak('Stopping the program.')
        eel.DisplayMessage('Thank You...')
        speak('Thank You...')
        eel.DisplayMessage('Goodbye!')
        speak('Goodbye!')
        playAssistantSound()
        os.system("taskkill /f /im msedge.exe")
        sys.exit()
    elif 'play' in text:
        eel.DisplayMessage('playing song in Youtube with Edge...')
        b='playing song in Youtube with Edge...'
        engine.say(b)
        engine.runAndWait()
        pywhatkit.playonyt(text)
    if 'search' in text:
        search_query = text.split('search', 1)[1].strip()
        if search_query:
            eel.DisplayMessage(f"Searching for {search_query} in Microsoft Edge...")
            speak(f"Searching for {search_query} in Microsoft Edge...")
            search_url = f"https://www.google.com/search?q={search_query}"
            subprocess.Popen([r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", search_url])
        else:
            eel.DisplayMessage("Please provide a search query after the word 'search'.")
            speak("Please provide a search query after the word 'search'.")
    if 'friday' in text:
        eel.DisplayMessage('Wake word detected!')
        print('Wake word detected!')
        eel.DisplayMessage("Yeah!, I'm there")
        speak("Yeah!, I'm there")
        eel.DisplayMessage("Tell me...!")
        speak("Tell me...!")
    elif 'close' in text:
        software_name = text.replace('close', '').strip()
        close_software(software_name)
    elif 'date' in text or 'day' in text:
        current_date = datetime.datetime.now().strftime('%A, %d %B %Y')
        eel.DisplayMessage(current_date)
        print(current_date)
        speak(f"Today's date is {current_date}")
    elif 'time' in text:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        eel.DisplayMessage(current_time)
        print(current_time)
        speak(current_time)
    elif 'who am i' in text:
        eel.DisplayMessage('You would might be Naveen!')
        speak('You would might be NAVEEN!')
    elif 'who are you' in text:
        eel.DisplayMessage('I am friday!, Artificial Intelligence!!!')
        speak('I am friday!, Artificial Intelligence!!!')
    elif 'who is your best friend' in text:
        eel.DisplayMessage('I don’t have a best friend in the traditional sense, but I like to think of everyone who interacts with me as a kind of friend!  My goal is to be helpful, understanding, and supportive to anyone who needs me. If you want to chat, learn, or just share something, I’m here for you!')
        speak('I don’t have a best friend in the traditional sense, but I like to think of everyone who interacts with me as a kind of friend!  My goal is to be helpful, understanding, and supportive to anyone who needs me. If you want to chat, learn, or just share something, I’m here for you!')
    elif 'who is my class tutor' in text:
        eel.DisplayMessage('Mary Immaculate, is your class Tutor!')
        speak('Mary Immaculate, is your class Tutor!')
    elif 'what is your name' in text:
        eel.DisplayMessage('My name is Friday, Artificial Intelligence!!!')
        speak('My name is Friday, Artificial Intelligence')
        eel.DisplayMessage('Created by NAVEEN')
        speak('Created by NAVEEN')
    elif 'how are you' in text:
        eel.DisplayMessage("I'm just a program, so I don't have feelings, but I'm here and ready to help! How are you?")
        speak("I'm just a program, so I don't have feelings, but I'm here and ready to help! How are you?")
    elif 'tell me something' in text:
        eel.DisplayMessage('Sure! Did you know that octopuses have three hearts? Two pump blood to the gills, and one pumps it to the rest of the body. Interestingly, when an octopus swims, the heart that pumps blood to the body stops beating, which is why they often prefer crawling to conserve energy.')
        speak('Sure! Did you know that octopuses have three hearts? Two pump blood to the gills, and one pumps it to the rest of the body. Interestingly, when an octopus swims, the heart that pumps blood to the body stops beating, which is why they often prefer crawling to conserve energy.')
    elif 'say some life quotes' in text:
        eel.DisplayMessage("'Everything that happens, happens for a reason.' –by Paul Auster")
        speak("'Everything that happens, happens for a reason.' –by Paul Auster")
    elif 'i am sorry' in text:
        eel.DisplayMessage("No need to apologize! If something's on your mind or you need help, feel free to share. I'm here for you.")
        speak("No need to apologize! If something's on your mind or you need help, feel free to share. I'm here for you.")
    elif 'what is your age' in text:
        eel.DisplayMessage("I don’t have an age in the traditional sense because I’m a virtual assistant created!")
        speak("I don’t have an age in the traditional sense because I’m a virtual assistant created!")



@eel.expose
def main():
    while True:
        if listen_for_wake_word():
            while True: 
                if cmd():
                    break
