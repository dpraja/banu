from flask import Flask,request
import speech_recognition as sr
import json
import tamil
import time
app = Flask(__name__)

@app.route("/helloworld",methods=['GET'])
def jk():
   r=sr.Recognizer()
   with sr.Microphone() as source:
       return 'say something'
       print('say something ')
       audio=r.listen(source)
   try:
       #print('google thinks you said:\n'+r.recognize_google(audio))
       c=r.recognize_google(audio)
       print(c)
       #time.sleep(5)
       return(json.dumps({'Status': 'Success','message':c}))
   except:
        pass
if __name__ == "__main__":
   app.run(host="192.168.1.10",port=5000) #change the port using ipconfig in cmd
