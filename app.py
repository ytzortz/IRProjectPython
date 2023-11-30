from asyncio import subprocess

import flask
# This it the tutorial I am checking out right now
# https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

from flask import Flask, render_template, request, jsonify

from destroy_index import delete_directory
from indexing_script import indexing
from search_script import searchDatabase

app = flask.Flask(__name__)


@app.route('/run-destroy-index-script', methods=['POST'])
def run_destroy_index_script():
    try:
        print("DESTROYING INDEXES --START")
        delete_directory("../index")
        return jsonify({'message': 'Indexing script executed successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/run-index-script', methods=['POST'])
def run_index_script():
    try:
        print("INDEXING --START")
        indexing()
        return jsonify({'message': 'Indexing script executed successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query')
    print("FROM PYTHON: " + query)

    genres = request.json.get('genres')

    title = request.json.get('titleFlag')

    results = searchDatabase(title, genres, query)


    return jsonify(results=results)


@app.route('/')
def index():
    return render_template('INDEX.html')

if __name__ == '__main__':
    app.run(debug=True)


