#!/usr/bin/env python

import os, platform, sys, webbrowser
try:
    import flask
except ImportError:
    import bottle

def product_url(in_name, in_domain_name, in_version):
    fmt = '<a href="http://{}">{} {}</a>'
    return fmt.format(in_domain_name, in_name, in_version)

python_link = product_url('Python', 'python.org', platform.python_version())

app = None
web_framework_link = ''
try:
    app = flask.Flask(__name__)
    web_framework_link = product_url('Flask', 'flask.pocoo.org', flask.__version__)
except NameError:
    app = bottle.Bottle(catchall=False)
    web_framework_link = product_url('Bottle', 'bottlepy.org', bottle.__version__)

@app.route('/')
def hello():
    fmt = '<h1>Hello World!</h1><p><p><sub>Running on {} and {}.</sub>'
    return fmt.format(python_link, web_framework_link)

if __name__ == '__main__':
    if sys.platform == 'darwin':
        webbrowser.open('http://127.0.0.1:5000')
        app.run(debug=True, port=5000)  # if on Mac OSX
    else:
        port = os.getenv('VCAP_APP_PORT', '5000')
        app.run(host='0.0.0.0', port=int(port))
