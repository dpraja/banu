from flask import Flask,request
import json
import goslate
from gtts import gTTS
from playsound import playsound
import os
app = Flask(__name__)
@app.route("/helloworld",methods=['POST'])
def audi():
    text = request.json['text']
    gs = goslate.Goslate()
    translatedText = gs.translate(text.encode(encoding='UTF-8'),'ar')
    print(translatedText)
    return(json.dumps({'Status':'sucess','Message': translatedText }))
if __name__ == "__main__":
    app.run(host="192.168.1.4",port=5000)





