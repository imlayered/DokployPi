If you're using a raspberry pi:

1. clone the repository:
   ```bash
   git clone https://github.com/imlayered/DokployPi dokploypi
    ```
2. cd into the directory:
   ```bash
   cd dokploypi
   ```
3. create venv & install stuff
   ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
4. enable execution of the script:
   ```bash
   chmod +x start_dokploypi.sh
   ```
5. add the following to your ``.bashrc`` file: (Modify {your_account_name} to your actual username)
    ```bash
    if [ $(tty) == /dev/tty1 ]; then
    /home/{your_account_name}/start_dokploypi.sh
    fi
    ```
6. reboot your raspberry pi

7. after reboot, you should see "no notification!" on the screen. this means the script is running and waiting for a notification.

8. you can use the gotify CLI to send notifications to your raspberry pi or a service like Dokploy to send when an event happens.

9. star the repository please :3 (https://github.com/imlayered/DokployPi)