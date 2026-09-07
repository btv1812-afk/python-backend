import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_NAME = os.getenv('APP_NAME', 'python-backend')
APP_VERSION = os.getenv('APP_VERSION', '1.0.0')
APP_ENV = os.getenv('APP_ENV', 'production')
PORT = int(os.getenv('PORT', 8080))

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'status': 'OK',
        'message': "Python Backend is сhanging and running v1",
    }), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'OK',
        'message': "Python Backend is healthy",
    }), 200


@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        'app_name': APP_NAME,
        'app_version': APP_VERSION,
        'app_env': APP_ENV,
        'port': PORT
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)