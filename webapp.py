from flask import Flask, request, render_template, flash
from markupsafe import Markup

import os
import json

app = Flask(__name__)

@app.route("/")
def  home():
    year = get_year()
    #print(states)
    return render_template('home.html, years=years)
