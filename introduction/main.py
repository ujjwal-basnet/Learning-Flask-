#basci flask app 
#importing 
from flask import Flask 
app = Flask(__name__)

@app.route('/')

def hellow_world():
    return "Hellow world "


#or you can also do 
def h_world():
    return "hellow world"
app.add.url_rule('/', 'h' , h_world)

#now run and do /h enter with exesting url 

# to run 
if __name__ == '__main__':
    app.run()
#about section 
