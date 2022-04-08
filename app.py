from crypt import methods
import email

from flask import Flask, redirect, render_template, request, session, url_for
import datetime


# FlASK
#############################################################
app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(days=365)
app.secret_key = "super secret key"

#############################################################

@app.route('/')
def home():
    email=None
    if "email" in session:
        email=session["email"]
        return render_template("index.html", data=email)
    else:
        return render_template('Login.html', data=email)

@app.route('/login', methods = ["GET","POST"])
def login():
    email =None
    if "email" in session:
        return render_template("index.html", data=email)
    else:

        if (request.method=="GET"):

            return render_template("Login.html", data="email")
        else:
            email=None
            email=request.form["email"]
            password= request.form["password"]
            session ["email"]=email

@app.route('/logout')
def logout():
    if "email" in session:
        session.clear
        #return redirect(url_for("home"))
        return render_template("index.html")
