from flask import Flask, request

app = Flask(__name__)


@app.route('/ping')
def ping():
    return {'message': 'pong'}


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
