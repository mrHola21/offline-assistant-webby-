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
    engine.say("I am  webby gautam the great . Please tell me how may I help you")
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
            if command=="google":
                engine.say('ok gautam')
                webbrowser.open('www.google.com')
                engine.runAndWait()
                break
            if command=="teams":
                engine.say('ok gautam')
                webbrowser.open("https://www.office.com/?auth=2")
                engine.runAndWait()
                break
            if command=="music":
                music_dir = 'D:\\My Music E\\English Songs\\La Bamba and other Hits'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[1] ))
            if command=="movie":
                movie_dir=''
                movies=os.listdir(movie_dir)
                os.startfile(os.path.join(movie_dir,movies[0]))
                break
            if command=='time':
                time()
            if command=='images':
                image_dir="D:\My Pictures E"
                images=os.listdir(image_dir)
                os.startfile(os.path.join(image_dir,images[random]))
            if command=="arduino":
                arduinppath="C:\\Program Files (x86)\\Arduino\\arduino.exe"
                os.startfile(arduinppath)
                break
            if command=="pycharm":
                pypath="C:\\Users\\Sandeep\\Desktop\\someThing\\PyCharm Community Edition 2019.3.4\\bin\\pycharm64.exe"
                os.startfile(pypath)
            if command=="android studio":
                aspath="C:\\Program Files\\Android\\Android Studio\\bin\\as.exe"
                os.startfile(aspath)
            if command=="unity installer":
                unity="C:\\Program Files\\Unity Hub\\Unity Hub.exe"
                os.startfile(unity)
            if command=='vsi':
                vsi=""
                os.startfile()
