# system_health_monitor.py

import psutil
import datetime

def log_alert(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("system_health.log", "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(message)

def check_system_health():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")

    if cpu > 80:
        log_alert("⚠️ CPU usage is above 80%!")
    if memory > 80:
        log_alert("⚠️ Memory usage is above 80%!")
    if disk > 80:
        log_alert("⚠️ Disk usage is above 80%!")

if __name__ == "__main__":
    check_system_health()
