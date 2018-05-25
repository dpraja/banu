from flask import Flask,request
import json
import goslate
from gtts import gTTS
from playsound import playsound
import os
def mytranslator(request):
    text = request.json['text']
    gs = goslate.Goslate()
    translatedText = gs.translate(text.encode(encoding='UTF-8'),'ar')
    print(translatedText)
    return(json.dumps({'Status':'sucess','Message': translatedText }))






