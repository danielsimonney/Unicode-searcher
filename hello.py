#!/usr/bin/env python3
from flask import Flask,render_template, request
from jinja2 import Template
import utils
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('acceuil.html')

@app.route('/search/',methods = ['POST', 'GET'])
def search():
     if request.method == 'GET' and bool(request.args):
        result = request.args["q"]
        myData = utils.UnicodeEnter(result)
        return render_template("result.html",height = len(myData),Alldatas=myData)
     else:
        return render_template('search.html')

@app.route('/unicode/<codepoint>')
def matchsasa_uni(codepoint):
    print(codepoint)
    resultUniqueUni = utils.UniqueUni(codepoint)
    return render_template('simpleresult.html', unicode = resultUniqueUni['unicode'],hexa = resultUniqueUni['hexa'],name=resultUniqueUni['name'],number=resultUniqueUni['number'],cat=resultUniqueUni['cat'])