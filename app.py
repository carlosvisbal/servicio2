# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/saludo', methods=['POST'])
def hello_world():
    return 'Hola, Cunista 2024!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
