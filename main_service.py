from importlib import import_module
from flask import Flask, render_template, Response, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import pyaml

app = Flask(__name__)

#curl -i -X PUT  -F name=Test -F data=@specs.epgz http://localhost:8080/upload_file
@app.route('/upload_file', methods=['PUT','POST'])
def receive_file():
    file = request.files['data']
    print (file)
    if file:
        filename = secure_filename(file.filename)
        file.save(filename)    
        #return (redirect(url_for('receive_file')))
    return jsonify({"mesasge":"move message received"})

@app.route('/', methods=['GET'])
def entry():
    return "Hello World"

def main():
    app.run(host='0.0.0.0', port=8080, threaded=True)

if __name__ == '__main__':
    main()