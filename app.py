
from http import client
from telnetlib import TLS
from flask import Flask, redirect, render_template, request, session, url_for
import datetime
import pymongo

# FlASK
#############################################################
app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(days=365)
app.secret_key = "super secret key"

#############################################################

# MONGODB
#############################################################
mongodb_key = "mongodb+srv://desarrollowebuser:desarrollowebpassword@cluster0.dfh7g.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(
    mongodb_key, tls=True, tlsAllowInvalidCertificates=True)
db = client.Escuela
cuentas = db.alumno
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
            return render_template("index.html", data= email)

@app.route('/logout')
def logout():
    if "email" in session:
        session.clear()
        return redirect(url_for("home"))


@app.route("/usuarios")
def usuarios():
    cursor = cuentas.find({})
    users = []
    for doc in cursor:
        users.append(doc)
    return render_template("/usuarios.html", data=users)
