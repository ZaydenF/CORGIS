from flask import Flask, request, render_template, flash
from markupsafe import Markup

import os
import json

app = Flask(__name__)

@app.route("/")
def  home():
    year = year_options()
    #print(states)
    return render_template('home.html', year_options=year)

@app.route("/showYear")
def render_info():
    year = year_options()
    return render_template('index2.html', year_options=year)
    
def year_options():
    with open('astronauts.json') as astronaut_data:
        years = json.load(astronaut_data)
    year=[]
    for c in years:
        if c["Mission"]['Year'] not in year:
            year.append(c["Mission"]['Year'])
    options=""
    for s in year:
        options += Markup("<option value=\"" + str(s) + "\">" + str(s) + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options
    

def is_localhost():
    """ Determines if app is running on localhost or not
    Adapted from: https://stackoverflow.com/questions/17077863/how-to-see-if-a-flask-app-is-being-run-on-localhost
    """
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url


if __name__ == '__main__':
    app.run(debug=False) # change to False when running in production

