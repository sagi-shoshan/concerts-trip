from os import path, walk
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(port="8888", debug=True)
