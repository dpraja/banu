'''import speech_recognition as sr
import requests
import json
from flask import Flask,request
import tamil
app = Flask(__name__)
@app.route("/helloworld",methods=['POST'])
def jk():
    from os import path
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "file.wav")

    r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source) # read the entire audio file

with open(r"/home/charan/Desktop/Speech/Speech-5156b41357e6.json", "r") as f:
    credentials_json = f.read()
    print("Google Speech Recognition thinks you said " + r.recognize_google_cloud(audio, credentials_json=credentials_json))
if __name__ == "__main__":
    app.run(host="192.168.1.6",port=5000)'''



import speech_recognition as sr
import requests
import json
from flask import Flask,request
import tamil
app = Flask(__name__)
@app.route("/helloworld",methods=['POST'])

def celll():
    {
  "config": {
      "encoding":"FLAC",
      "sampleRateHertz": 16000,
      "languageCode": "en-US"
  },
  "audio": {
      "uri":"http://192.168.1.6:5000/helloworld"
  }
}
if __name__ == "__main__":
    app.run(host="192.168.1.6",port=5000)
