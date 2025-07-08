from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.route('/')
def index():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json or {}
    prompt = data.get('prompt', '')
    payload = {
        "model": "llama3:8b",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    result = response.json()
    return jsonify({"response": result.get("response", "")})

if __name__ == '__main__':
    app.run(debug=True) 