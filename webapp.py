from flask import Flask, request, render_template, flash
from markupsafe import Markup

import os
import json

app = Flask(__name__)

@app.route("/")
def  home():
    year = year_option()
    #print(states)
    return render_template('home.html', year_option=year)

@app.route("/showYear")
def render_info():
    year = year_option()
    ayear = request.args["year"]
    astronaut = Astronauts_in_year(year)
    fact = "In the year " + ayear + ", there were " + astronaut + "astronauts"
    return render_template('index2.html', year_option=year, AFact=fact )
def year_option():
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
def Astronauts_in_year(year):
    with open('astronauts.json') as astronaut_data:
        years = json.load(astronaut_data)
    count=0
    for c in count:
        if c['Mission']['Year'] == ayear:
            count = count+1
    
    return count
    
    
 

def is_localhost():
    """ Determines if app is running on localhost or not
    Adapted from: https://stackoverflow.com/questions/17077863/how-to-see-if-a-flask-app-is-being-run-on-localhost
    """
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url


if __name__ == '__main__':
    app.run(debug=True) # change to False when running in production

#def Astronauts_in_year(ayear):
  #  with open('astronauts.json') as astronaut_data:
  #      years = json.load(astronaut_data)
  #  amount = int(request.form['Year']
  #  count = sum(1 for test in data if test['Profile']['Selection']['Year'] ==