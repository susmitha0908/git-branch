# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hiiiiiiiiiiiiiiii from Docker + Python!"

@app.route('/about')
def about():
    return "This is a Python Flask app running in Python3!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
