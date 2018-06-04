from flask import Flask,request
import json
from gtts import gTTS
from playsound import playsound
import os
def mytranslator(request):
    mytext = request.json['mytext']
    language = 'ta'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.wav")
    playsound("https://s3.amazonaws.com/infocuithtml/welcome.wav")
    print("printing")
    return(json.dumps({'Status': 'Success','Message': 'Computer Think! You Say This '},indent=4))







