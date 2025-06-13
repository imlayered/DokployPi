import subprocess
import sys

if __name__ == "__main__":
    try:
        subprocess.run([sys.executable, "server/messages.py"])
    except KeyboardInterrupt:
        print("Shut down... Goodbye! || webhookpi.auri.lol")