#!/usr/bin/env python

import os, platform, sys, webbrowser

use_flask = False
try:
    import flask
    use_flask = True
except ImportError:
    import bottle

def get_footer():  # HTML to show version info for Python and Flask/bottle 
    def product_url(in_name, in_domain_name, in_version):
        fmt = '<a href="http://{}">{} {}</a>'
        return fmt.format(in_domain_name, in_name, in_version)

    python_link = product_url('Python', 'python.org', platform.python_version())
    if use_flask:
        web_framework_link = product_url('Flask', 'flask.pocoo.org', flask.__version__)
    else:
        web_framework_link = product_url('Bottle', 'bottlepy.org', bottle.__version__)
    return '<sub>Running on {} and {}.</sub>'.format(python_link, web_framework_link)

footer = get_footer()
app = flask.Flask(__name__) if use_flask else bottle.Bottle(__name__)

@app.route('/')
def hello():
    return '<h1>Hello World!</h1><p><p>' + footer

if __name__ == '__main__':
    if sys.platform == 'darwin':
        webbrowser.open('http://127.0.0.1:5000')
        app.run(debug=True, port=5000)  # if on Mac OSX
    else:
        port = os.getenv('VCAP_APP_PORT', '5000')
        app.run(host='0.0.0.0', port=int(port))
