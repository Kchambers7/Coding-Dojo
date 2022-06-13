 make a new directory

 move this document inside the new directory.

 create virtual environment:

pipenv install flask

 activate virtual environment:

pipenv shell

 create server.py:

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    
 start webserver:

python server.py

 add templates folder with all the html files you need for your application.

 add routes as needed:

@app.route('/about')
def about():
    return render_template('about.html')