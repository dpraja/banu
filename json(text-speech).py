from flask import Flask,request
import json
from gtts import gTTS
from playsound import playsound
import os
app = Flask(__name__)
@app.route("/helloworld",methods=['POST'])
def audi():
    mytext = request.json['mytext']
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    playsound("C:/Users/dell/AppData/Local/Programs/Python/Python35/welcome.mp3")
    print("printing")
    return(json.dumps({'Status': 'Success','Message': 'Computer Think! You Say This '},indent=4))
if __name__ == "__main__":
    app.run(host="192.168.1.8",port=5000)
