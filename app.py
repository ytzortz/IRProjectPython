import flask
# This it the tutorial I am checking out right now
# https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

from flask import Flask, render_template, request

app = flask.Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello():
    return 'Hello, World!'