from flask import Flask, Response, request
from flask import render_template

import requests
import redis
import os

app = Flask(__name__)
cache = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/', methods=['GET'])
def mainpage():
    return render_template('index.html')

@app.route('/dict/<word>', methods=['GET'])
def get_translation(word):
    translation = cache.get(word)
    if translation is None:
        translation = requests.get('http://dict:8080/' + word).content
        cache.set(word, translation)

    return Response(translation)

@app.route('/add/<word>/<definition>', methods=['POST'])
def add_definition(word, definition):
    cache.set(word, definition)
    return Response('The word was added!')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
