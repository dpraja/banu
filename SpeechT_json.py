from flask import Flask,request
import speech_recognition as sr
import json
import tamil
app = Flask(__name__)
@app.route("/helloworld",methods=['POST'])
def jk():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('say something')
        audio=r.listen(source)
        print('google thinks you said:\n'+r.recognize_google(audio))
        return(json.dumps({'Status': 'Success','message':r.recognize_google(audio) }))

if __name__ == "__main__":
    app.run(host="192.168.1.8",port=5000)
