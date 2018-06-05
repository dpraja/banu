import pygame
import requests
from time import sleep
from pygame import mixer
import os
from flask import Flask,request
app = Flask(__name__)
#@app.route("/Audiomp3",methods=['GET'])
def audiomp3url():
   
   #test_url = 'https://archive.org/download/PinkFloyd07CarefullWithThatAxeEugene/02%20-%20Learning%20To%20Fly.mp3'
   test_url = "https://s3.amazonaws.com/infocuithtml/Maleh-Maleh.mp3"
   pygame.mixer.init()
   r = requests.get(test_url,stream=True)
   pygame.mixer.music.load(r.raw)
   pygame.mixer.music.play()
   while pygame.mixer.music.get_busy():
           sleep(1)
#test_url = "https://s3.amazonaws.com/infocuithtml/0.mp3"
#if __name__ == "__main__":
  #app.run(host="192.168.1.1",port=5000)
