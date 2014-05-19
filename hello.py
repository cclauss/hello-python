#!/usr/bin/env python

import flask_or_bottle, os, sys, webbrowser

app = flask_or_bottle.app

@app.route('/')
def hello():
    return '<h1>Hello World!</h1><p><p>' + flask_or_bottle.footer

if __name__ == '__main__':
    if sys.platform == 'darwin':
        webbrowser.open('http://127.0.0.1:5000')
        app.run(debug=True, port=5000)  # if on Mac OSX
    else:
        port = os.getenv('VCAP_APP_PORT', '5000')
        app.run(host='0.0.0.0', port=int(port))
