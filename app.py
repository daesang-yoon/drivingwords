from flask import Flask, render_template, request

from quote import get_inspirational_quote, get_stoic_quote

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def home():
    if request.method=="GET":
        return render_template('index.html', inspirational_quote='', stoic_quote='', description='Be inspired')
    if request.method=="POST":
        return render_template('index.html', inspirational_quote=get_inspirational_quote(), stoic_quote=get_stoic_quote(), description='Get Another Quote')
    

@app.route("/about")
def about():
    return render_template('about.html')