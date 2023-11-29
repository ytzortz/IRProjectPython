from asyncio import subprocess

import flask
# This it the tutorial I am checking out right now
# https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

from flask import Flask, render_template, request, jsonify

app = flask.Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query')
    print("FROM PYTHON: " + query)

    # we search things here

    result = 'THE RESULTS ARE HERE'
    return jsonify(message=result)


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/run-indexing-script', methods=['POST'])
def run_indexing_script():
    try:
        subprocess.run(['python', 'indexing_script.py'], check=True, text=True)
        return jsonify({'message': 'Indexing script executed successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})
