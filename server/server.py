import os
from flask import Flask, request
from dotenv import load_dotenv
from logger import logger

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
    logger.log_event({
        'endpoint': 'webhook',
        'title': title,
        'message': message,
        'priority': priority
    })
    try:
        with open('logs/latest_notification.json', 'w') as notif_file:
            import json
            json.dump({'title': title, 'message': message, 'priority': priority}, notif_file)
    except Exception as e:
        print(f"Failed to write notification: {e}")
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
    logger.log_event({
        'endpoint': 'webhook_message',
        'title': title,
        'message': message,
        'priority': priority
    })
    try:
        with open('logs/latest_notification.json', 'w') as notif_file:
            import json
            json.dump({'title': title, 'message': message, 'priority': priority}, notif_file)
    except Exception as e:
        print(f"Failed to write notification: {e}")
    return '{}', 200, {'Content-Type': 'application/json'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5123)
