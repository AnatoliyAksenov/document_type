#!flask/bin/python
from flask import Flask, jsonify
from flask import request
import io
import model
import base64
import tempfile

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/document/gettype', methods=['POST'])#
def post():
    imgfile = tempfile.NamedTemporaryFile(delete=False)
    imgfile.write(base64.b64decode(request.json['file'])) 
    imgfile.close()
    classes = model.predict(imgfile.name)
    result = {}
    result['classes'] = classes.tolist()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['PORT'], debug=False)