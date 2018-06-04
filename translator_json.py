from flask import Flask,request
import json
from gtts import gTTS
from playsound import playsound
import os
def mytranslator(request):
    mytext = request.json['mytext']
    language = 'ta'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    playsound("C:/Users/dell/AppData/Local/Programs/Python/Python35/welcome.mp3")
    print("printing")
    return(json.dumps({'Status': 'Success','Message': 'Computer Think! You Say This '},indent=4))







