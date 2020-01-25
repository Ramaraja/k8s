import socket

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def version():
    return 'API Version 1'

@app.route('/hostname')
def hname():
    return '{}'.format(socket.gethostname())

@app.route('/health')
def health():
    return 'I\'m ok!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, )
