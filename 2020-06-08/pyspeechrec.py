# Hands on Speech-recognitation...

import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
from gtts import gTTS
import random

r=sr.Recognizer()
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio=r.listen(source)
        voice_data=''
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueErro:
            print('sorry!, I did not get that ')
        except sr.RequestError:
            print('Sorry ! my speech services is down')
        return voice_data
def vivek_speak(audio_string):
    tts=gTTS(text=audio_string, lang='en')
    r= random.randint(1,10000)
    audio_file='audio-'+str(r)+ '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)

    
def respond(voice_data):
    if 'what is your name' in voice_data:
        print('Your Name....')
        vivek_speak('My Name is Vivek Vishwakarma')
    if 'time' in voice_data:
        vivek_speak(ctime())
    if 'search' in voice_data:
        search=record_audio('what do you want to search ?')
        url = 'https://google.com/search?q=' +search
        webbrowser.get().open(url)
        vivek_speak('Here is what I found for '+search)

    if 'location' in voice_data:
        location=record_audio('what do you want to location')
        url = 'https://google.nl/maps/place/'+location+ '/&amp:'
        webbrowser.get().open(url)
        vivek_speak('Here your location  '+location)

    if 'ok go' in voice_data:
        exit()


time.sleep(1)
vivek_speak('how can help you....')

while 1:
    voice_data=record_audio()
    respond(voice_data)


# STILL UNDER CONSTRUCTION...    