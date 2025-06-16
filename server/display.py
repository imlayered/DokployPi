import os
import time
import json
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

NOTIF_PATH = os.path.join(os.path.dirname(__file__), '../logs/latest_notification.json')
console = Console()

def read_notification():
    try:
        with open(NOTIF_PATH, 'r') as f:
            return json.load(f)
    except Exception:
        return None

def display_notification(notification):
    if not notification:
        console.clear()
        console.print(Align.center('[bold yellow]no notification![/bold yellow]', vertical="middle"))
        return
    title = notification.get('title', 'No Title')
    message = notification.get('message', '')
    panel = Panel(f"[bold]{message}[/bold]", title=f"[cyan]{title}", border_style="green")
    console.clear()
    console.print(Align.center(panel, vertical="middle"))

def main():
    last_content = None
    while True:
        notif = read_notification()
        content = json.dumps(notif, sort_keys=True) if notif else ''
        if content != last_content:
            display_notification(notif)
            last_content = content
        time.sleep(1)

if __name__ == "__main__":
    main()
