from crypt import methods
from distutils.log import error
import errno
from flask import Flask, render_template

# FlASK
#############################################################
app = Flask(__name__)
#############################################################

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prueba')
def prueba():
    nombres =[]
    nombres.append ({"nombre": "Isaac"})
    nombres.append ({"nombre": "David"})

    return render_template ("home.html", data=nombres)