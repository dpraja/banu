from flask import Flask,request
import json
from gtts import gTTS
from playsound import playsound
import os
app = Flask(__name__)
@app.route("/127.168.0.1",methods=['POST'])
def audi():
    mytext = request.json['mytext']
    mobile = request.json['mobile']
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("C:/Users/dell/AppData/Local/Programs/Python/Python35/Recording/%s.mp3"%mobile)
    playsound("C:/Users/dell/AppData/Local/Programs/Python/Python35/Recording/%s.mp3"%mobile)
    print("printing")
    return(json.dumps({'Status': 'Success','Message': 'Computer Think! You Say This '},indent=4))
if __name__ == "__main__":
    app.run(host="192.168.1.4",port=5000)
