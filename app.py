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
        #render main page with search results and search query
        return render_template("index.html", recipe=recipes, search_query=query)
        
    #if no form is submitted
    search_query = request.args.get("search_query", "")
    decoded_search_query = unquote(search_query)
    # perform a search for recipes with the decoded search query
    recipes = search_recipes(decoded_search_query)
    #render main page
    return render_template("index.html", recipes=recipes, search_query=decoded_search_query)

# search function upon query
def search_recipes(query):
    url = f"https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apikey": API_KEY,
        "query" : query,
        "number": 10,
        "instructionsRequired": True,
        "addRecipeInformation": True,
        "fillIngredients" : True,
    }

    # Send get request to API
    response = requests.get(url, params=params)
    if response.status_code== 200:
        data = response.json()

        return data["results"]
    return []