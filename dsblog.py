# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:44:41 2021


"""
# author: Telemachos Chatzitheodorou

from flask import Flask , render_template, url_for

from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '3543e0d8e4084eff2644c031a79cc73a'

posts = [
    {"author": "niarniar",
     "date_posted": "14/08/2021",
     "title": "Post 1",
     "content": "Dummy post"
     }
    ]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',  title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)