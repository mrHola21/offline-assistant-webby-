import pyttsx3
import datetime
import webbrowser
import os
import random

engine=pyttsx3.init()
running=True
minute=int(datetime.datetime.now().minute)
second=int(datetime.datetime.now().second)
hour = int(datetime.datetime.now().hour)


def  wishme():
    rate = engine.getProperty('rate')
    engine.setProperty('rate',250)
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        engine.say("Good Morning!")
    elif hour>=12 and hour<17:
        engine.say("Good Afternoon!")
    else:
        engine.say("Good Evening!")
    engine.say("I am  webby ,your name, . Please tell me how may I help you")
    engine.runAndWait()
def time():
    engine.say('it is')
    engine.say(hour)
    engine.say(minute)
    engine.say('minutes')
    engine.say(second)
    engine.say('seconds')
    engine.runAndWait()

while running==True:
            command=input('>')
            if command=="youtube":
                webbrowser.open('https://youtube.com/')
                engine.runAndWait()
                break
            if command=="google
                webbrowser.open('www.google.com')
                engine.runAndWait()
                break
            if command=="music":
                music_dir = 'add your music path'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[1] ))
            if command=="movie":
                movie_dir='add your movie path'
                movies=os.listdir(movie_dir)
                os.startfile(os.path.join(movie_dir,movies[0]))
                break
            if command=='time':
                time()
            if command=='images':
                image_dir="add your image path "
                images=os.listdir(image_dir)
                os.startfile(os.path.join(image_dir,images[random]))
            if command=="arduino":
                arduinppath="add your arduino's .exe file's path"
                os.startfile(arduinppath)
                break
          
