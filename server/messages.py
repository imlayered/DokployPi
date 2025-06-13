import os
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

SECRET_URL = os.getenv('SECRET_URL')
if not SECRET_URL:
    raise ValueError("SECRET_URL not set in .env file")

app = Flask(__name__)

@app.route(f"/{SECRET_URL}", methods=['POST', 'GET'])
def webhook():
    if request.method == 'GET':
        return 'up', 200
    data = request.get_json(force=True, silent=True)
    if not data:
        print("nothing received")
        return '', 204
    title = data.get('title')
    message = data.get('message')
    priority = data.get('priority')
    print(f"  title: {title}")
    print(f"  msg: {message}")
    print(f"  priority: {priority}")
    return '', 204

@app.route(f"/{SECRET_URL}/version", methods=['GET'])
def webhook_version():
    return '{"version": "1.0.0"}', 200, {'Content-Type': 'application/json'} # Just so Gotify works

@app.route(f"/{SECRET_URL}/message", methods=['POST'])
def webhook_message():
    data = request.get_json(force=True, silent=True)
    if not data:
        print("nothing received")
        return '', 204
    title = data.get('title')
    message = data.get('message')
    priority = data.get('priority')
    print(f"  title: {title}")
    print(f"  msg: {message}")
    print(f"  priority: {priority}")
    return '{}', 200, {'Content-Type': 'application/json'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5123)
