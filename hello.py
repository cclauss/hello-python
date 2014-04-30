import os, sys
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World!<p><p><sub>Running on Python {}</sub>'.format(sys.version)

if __name__ == "__main__":
    if sys.platform == 'darwin':
        app.run(debug=True)  # if on Mac OSX
    else:
        port = os.getenv('VCAP_APP_PORT', '5000')
        app.run(host='0.0.0.0', port=int(port))
