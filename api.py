#!flask/bin/python
from flask import Flask, request
import backend

app = Flask(__name__)

@app.route('/')
def health_check():
    return "Hello, World!"

@app.route('/translate', methods=['POST'])
def call_translator():
    print request.data
    return backend.translate_text_to_text(request.data)

@app.route('/speak', methods=['POST'])
def call_translator_speech():
    print request.data
    return backend.speak_translated_text(request.data)


if __name__ == '__main__':
    app.run(debug=True)
