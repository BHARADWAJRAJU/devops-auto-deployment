import psutil
import requests
import datetime

CPU_LIMIT = 80
MEMORY_LIMIT = 80
DISK_LIMIT = 80

timestamp = datetime.datetime.now()

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent

print("===================================")
print("        EC2 ALERT MONITOR")
print("===================================")
print(f"Time   : {timestamp}")
print(f"CPU    : {cpu}%")
print(f"Memory : {memory}%")
print(f"Disk   : {disk}%")

alerts = []

if cpu > CPU_LIMIT:
    alerts.append(f"High CPU usage: {cpu}%")

if memory > MEMORY_LIMIT:
    alerts.append(f"High Memory usage: {memory}%")

if disk > DISK_LIMIT:
    alerts.append(f"High Disk usage: {disk}%")

try:
    response = requests.get(
        "http://localhost:5000/health",
        timeout=5
    )

    if response.status_code != 200:
        alerts.append("Application is DOWN")

except requests.exceptions.RequestException:
    alerts.append("Application is DOWN")

if alerts:
    print("\nALERTS:")

    with open("logs/alerts.log", "a") as log:
        for alert in alerts:
            message = f"{timestamp} - WARNING: {alert}"
            print(message)
            log.write(message + "\n")

else:
    print("\nSystem Status: HEALTHY")

print("===================================")
