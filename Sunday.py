import pyttsx3
import speech_recognition as sr 
import datetime 
import wikipedia
import webbrowser
import os 
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices) 
engine.setProperty('voice', voices[1].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()
speak("sunday,'version 1.5'. Fechingout system data. Anallysing your Algorithem. system security,'check'. system Temperature,'check'. Performance,'check'. Your persional assistance. 'Activated!!'.")

def wishMe(): 
    hour = int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12:
        speak("good morning sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir") 

    else:
        speak("Good Evening sir")

def takeCommand(): 
    #it takes microphone input from the user and returns string output
 
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("listening...") 
        r.pause_threshold = 1
        audio = r.listen(source)
    try: 
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")
    except Exception as e: 
       # print(e)

        print("say that again please...")
        return "None" 
    return query

if __name__ == "__main__" :
   wishMe() 
   while True:
       query = takeCommand().lower()

       if 'wikipedia' in query:
           speak('searching wikipedia...')
           query = query.replace("wikipedia","")
           results =wikipedia.summary(query, sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)
 
       elif 'open youtube' in query:
           webbrowser.open("youtube.com")
       elif 'open google' in query: 
           webbrowser.open("google.com") 
       elif 'play some music' in query:
           music_dir = 'C:\\Users\\hp\\Music'
           songs = os.listdir(music_dir) 
           print(songs)
           os.startfile(os.path.join(music_dir,songs[0]))
       elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           print(strTime)
           speak(f"the time is {strTime}")
       elif 'open visual studio' in query:
           visualstudioPath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
           os.startfile(visualstudioPath)
       elif 'hi sunday' in query:
           speak('HLLOW Sir. Nice too see you back.')  
       elif 'hay sunday' in query:
           speak('HLLOW Sir. Nice too see you back.')
       elif 'what the f***' in query:
           speak('did you just said what the fuck, fuck. let me remind you sir bad words are not allowed here. is that clear.')     
       elif 'help me' in query:
           speak("i will alwayas there for you.")
       elif 'what can you do' in query: 
           speak("I can do anything you want me to do sir. ")
       elif 'sunday quit' in query: 
           speak("Quitting sir.")
           exit()
       elif 'exit pycharm' in query:
           try: 
               os.system('Taskkill /f /im pycharm64.exe')
               speak('exitting the programme sir, hope you enjoy') 
           except Exception as e: 
               print(e)
               speak('sorry sir, i think there is a problem') 
       elif 'exit visual studio' in query: 
           try:
              speak('exitting the programme sir, hope you enjoy') 
              os.system('Taskkill /f /im code.exe')
           except Exception as e:
               print(e) 
       elif 'calculator' in query:
           try:
               os.system('calc')
           except Exception as e:
               print(e)          
       elif 'open notepad' in query:
           try:
               os.system('notepad')
           except Exception as e:
               print(e)        
       elif 'remote desktop connection' in query:
           try:
               os.system('mstsc')
           except Exception as e:
               print(e)
       elif 'open task manager' in query:
           try:
               os.system('taskmgr')
           except Exception as e:
               print(e)
       elif 'on screen keyboard' in query:
           try:
               os.system('osk')
           except Exception as e:
               print(e)
       elif 'show wi-fi around me' in query:
           wifipath="D:\\PROGRAMMING\\Batch programming\\wifi.bat"
           os.startfile(wifipath)
       elif 'shutdown ' in  query:
           try:
               os.system('shutdown /s')
           except Exception as e:
               print(e)
           speak('your system will be shut down in less than 30 seconds.')
       elif 'stop the system shutdown'in query:
           try:
               os.system('shutdown /a')
           except Exception as e:
               print(e)
           speak('aborted, system shut down.')
       elif 'hacking' in query:
           speak('woooooooooooo, i am sooooooooo excited!!' )
       elif'made you' in query:
           speak('name of my creater is rohit. ')
       elif 'CMD' in query:
           cmdpath="C:\\Windows\\system32\\cmd.exe"
           os.startfile(cmdpath)
       elif 'virus' in query:
          try:
               os.system('D:\\PROGRAMMING\\Batch programming\\virus2.bat')
          except Exception as e:
               print(e)
                  