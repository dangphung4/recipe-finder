from flask import Flask, render_template, request
import requests
from urllib.parse import unquote

#flask app
app = Flask(__name__)

#env SPOONTACULAR API KEY
API_KEY = "832820078b2e475f913f9fbb5f2fe382"

#home button route
@app.route("/home", methods=["GET"])
def home():
    #render main page, empty list and serach query
    return render_template("index.html", recipe=[], search_query="")

#main route for app
@app.route("/", methods=["GET", "POST"])
def index(): 
    if request.method == "POST":
        #if form is submitted
        query = request.form.get("search_query", "")
        # perform seasrch for recipes with given query
        recipes = search_recipes(query)
        