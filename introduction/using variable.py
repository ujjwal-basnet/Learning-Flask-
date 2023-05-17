# here we learn to build dynamical 
#website 

#  hint  <variable-name> 

from flask import Flask 
app = Flask(__name__)

@app.route('/hellow/<name>')
def hellow_name(name):
    return 'Hellow %s how are you ' % name 


# point to noice to run 
#   127.0.0.1:5000/hellow/ujjwal/hellow/<name> #nothings happens 


#now add variable 
# 127.0.0.1:5000/hellow/ujjwal
#output  ->  " cHellow ujjwal how are you "


#adding home route 




## contervers 
# int , float , path (acepts slashes used as directory seperator character )

@app.route('/about/<int:number>')
def show_contact(number):
    return 'your contact no is %d' % number

@app.route('/user/<float:balance>')
def user(balance):
    return "your current balance is %f" %balance 

if __name__ == '__main__':
    app.run()