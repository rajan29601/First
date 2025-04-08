# setup.py (or a helper script to run everything)

import subprocess
import time

print("Building Docker image...")
subprocess.run(["docker", "build", "-t", "flask-app", "."])

print("Stopping any existing flask-app container...")
subprocess.run(["docker", "rm", "-f", "flask-app"], stderr=subprocess.DEVNULL)

print("Running Docker container on port 5000...")
subprocess.run([
    "docker", "run", "-d", "--name", "flask-app",
    "-p", "5000:5000",
    "flask-app"
])

print("Setting up Windows portproxy using PowerShell (run as Admin)...")
subprocess.run([
    "powershell", "-Command",
    "netsh interface portproxy add v4tov4 listenport=5000 listenaddress=0.0.0.0 connectport=5000 connectaddress=127.0.0.1"
])

print("All set! Visit http://<your-local-ip>:5000 from another device on the same Wi-Fi network.")



