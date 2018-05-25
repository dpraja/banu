'''
This is the master file for all the Web services
related to IVR application
'''
import json
from flask import Flask,request, jsonify
from flask_cors import CORS
from translator_json import mytranslator

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
   return "Welcome Banu!"
@app.route("/texttospeech",methods=['POST'])
def texttospeech():
   return mytranslator(request)




if __name__ == "__main__":
  app.run(debug=True)
   
