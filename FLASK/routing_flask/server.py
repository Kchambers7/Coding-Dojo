from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/dojo')
def about():
    return "<h1> Dojo!</h1>

@app.route('/say/<name>')
def say(name):
    return f "Hi {name.capitalize()}!

@app.route('/say/<name>')
def say(name):
    return f"Hi {name.capitalize()}!"

app.route('/<int:num>/<name>')
def repeat(num, name):
         return f"{name * num"

if __name__=="__main__":
     app.run(debug=True)