"""

# -*- coding: utf-8 -*-
Created on          26 Jan 2019 at 9.01 PM
@author:            Arvind Sachidev Chilkoor
Created using:      PyCharm
Name of Project:    Simple Website Project - FLASK



This program demonstrates the usage of flask and how to create live running website.

"""

from flask import Flask, render_template

app=Flask(__name__)             # Flask declaration and initialization

@app.route('/')
def home():                                 # Defining the Home() method for web page for "HOME" section
    return render_template("home.html")

@app.route('/about/')
def about():                                # Defining the Home() method for web page for "ABOUT" section
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)                     # Calling the web app to run.
