from importlib import import_module
from flask import Flask, render_template, Response


app = Flask(__name__)


@app.route('/', methods=['GET'])
def entry():
    return "Hello World"


def main():
    app.run(host='0.0.0.0', port=8080, threaded=True)

if __name__ == '__main__':
    main()