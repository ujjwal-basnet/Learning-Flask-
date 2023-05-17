# the function 
# url_for is very useful for dynamic function 
 

from flask import Flask , redirect , url_for 
app = Flask(__name__)

@app.route('/admin')
def hellow_admin():
    return 'Hellow Admin'

@app.route('/guest/<name>')
def hellow_guest(name):
    return 'Hellow %s ' % name 

@app.route('/user/<name>')
def hellow_User(name):
    return 'How are you %s ' % name 

## use of url_for() function 



# the url_for () accepts name of the function as 
#first argument 

@app.route('/users/<names>')
def hellow_user(names):
    if names == "admin":
        return redirect(url_for('hellow_admin'))
    else :
        return redirect(url_for('hellow_guest') , guest = names )
    
if __name__ == '__main__':
    app.run(debug= True )
    