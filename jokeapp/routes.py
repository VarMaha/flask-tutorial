from jokeapp import app
from flask import render_template
import json
import os
import random
@app.route("/joke")
def send_joke():
    joke_path = os.path.join(os.path.dirname(os.path.abspath(__file__))
                                            ,'resources','reddit_jokes.json').replace("\\","/")
    with open(joke_path) as jokes:
        data = json.load(jokes)
    
    joke = random.sample(data,1)[0]
    joke = dict(joke)
    return render_template("show_joke.html",joke=joke)

