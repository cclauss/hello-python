import flask, os, sys

app = flask.Flask(__name__)

@app.route('/')
def hello():
    fmt = '<h1>Hello World!</h1><p><p><sub>Running on Python {} and Flask {}.</sub>'
    return fmt.format(sys.version, flask.__version__)

if __name__ == "__main__":
    if sys.platform == 'darwin':
        app.run(debug=True)  # if on Mac OSX
    else:
        port = os.getenv('VCAP_APP_PORT', '5000')
        app.run(host='0.0.0.0', port=int(port))
