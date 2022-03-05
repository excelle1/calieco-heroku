from flask import Flask, render_template
from replit import web

app = Flask(__name__)

@app.route('/')
def index():
  return 'Wassup'

@app.route('/about')
def about():
  return 

@app.route('/signin')
web.run(app)