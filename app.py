import subprocess
import sys
import threading

if __name__ == "__main__":
    try:
        import server.logger 
        def run_display():
            subprocess.run([sys.executable, "server/display.py"])
        display_thread = threading.Thread(target=run_display, daemon=True)
        display_thread.start()
        subprocess.run([sys.executable, "server/server.py"])
    except KeyboardInterrupt:
        print("Shut down... Goodbye! || webhookpi.auri.lol")