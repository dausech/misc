from flask import Flask
from OpenSSL import SSL

import os

context = SSL.Context(SSL.SSLv23_METHOD)
cer = os.path.join(os.path.dirname(__file__), 'resources/empresa.cer')
key = os.path.join(os.path.dirname(__file__), 'resources/empresa.key')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    context = (cer, key)
    app.run( host='0.0.0.0', port=5000, debug = True, ssl_context=context)