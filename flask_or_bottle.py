#!/usr/bin/env python

'''
This file exports two values:
    flask_or_bottle.app
        and
    flask_or_bottle.footer
'''

import platform

use_flask = False
try:
    import flask
    use_flask = True
except ImportError:
    import bottle

def get_footer():
    def product_url(in_name, in_domain_name, in_version):
        fmt = '<a href="http://{}">{} {}</a>'
        return fmt.format(in_domain_name, in_name, in_version)

    python_link = product_url('Python', 'python.org', platform.python_version())
    if use_flask:
        web_framework_link = product_url('Flask', 'flask.pocoo.org', flask.__version__)
    else:
        web_framework_link = product_url('Bottle', 'bottlepy.org', bottle.__version__)
    return '<sub>Running on {} and {}.</sub>'.format(python_link, web_framework_link)

app = flask.Flask(__name__) if use_flask else bottle.Bottle(__name__)
footer = get_footer()

if __name__ == '__main__':
    print('''This file exports two values:
    flask_or_bottle.app
        and
    flask_or_bottle.footer''')
