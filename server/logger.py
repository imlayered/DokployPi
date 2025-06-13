import os
import json
from collections import deque
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

LOG_STORE_AMOUNT = int(os.getenv('LOG_STORE_AMOUNT', 1000))
LOGS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
LOG_FILE = os.path.join(LOGS_DIR, 'messages.log')

if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

class EventLogger:
    def __init__(self, max_events=LOG_STORE_AMOUNT, log_file=LOG_FILE):
        self.max_events = max_events
        self.log_file = log_file
        self.events = deque(maxlen=max_events)
        self._load_events()

    def _load_events(self):
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, 'r') as f:
                    for line in f:
                        event = json.loads(line.strip())
                        self.events.append(event)
            except Exception:
                self.events = deque(maxlen=self.max_events)

    def log_event(self, event):
        event_with_time = dict(event)
        event_with_time['timestamp'] = datetime.now().isoformat()
        self.events.append(event_with_time)
        with open(self.log_file, 'w') as f:
            for e in self.events:
                f.write(json.dumps(e) + '\n')

logger = EventLogger()
