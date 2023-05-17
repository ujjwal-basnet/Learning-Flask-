#basci flask app 
#importing 
from flask import Flask 
app = Flask(__name__)

@app.route('/')

def hellow_world():
    return "Hellow world "

#about section 