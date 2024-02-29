!pip install flask_ngrok

import pandas as pd
from flask_ngrok import run_with_ngrok
from flask import request, jsonify, Flask
import random as rk

app = Flask(__name__) #the name of the application package
run_with_ngrok(app) 

d = {
    "name": "Nikola", 
    "surname": "Tesla", 
    "idade": 60
      }

@app.route("/") #code to assign HomePage URL in our app to function home.

def home():
  '''
  The entire line below must be written in a single line.
  '''
  return "<marquee><h3> TO CHECK IN PUT ADD '/input' TO THE URL AND TO CHECK OUT PUT ADD '/output' TO THE URL.</h3></marquee>"

@app.route("/input") #code to assign Input URL in our app to function input.

def input():
  return jsonify(d) # "d" is the dictionary we defined

@app.route('/output', methods=['GET','POST']) #output page

def predJson():
 pred = r.choice(["positive","negative"])
 nd = d # our input
 nd["prediction"]=pred
 return jsonify(nd)

app.run()

