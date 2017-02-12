from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
   return 'Hello all! This is python flask app'

app.run