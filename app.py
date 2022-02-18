import os
from flask import Flask, render_template, request
from bot import *

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/",methods=["POST"])    
def form_post():
    if request.method == "POST":
            text = request.form['text']
            answer = chat(text)

    return render_template("index.html",text = text,answer = answer)




if __name__ == '__main__':
    app.run(debug=True)