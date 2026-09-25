import psutil
import datetime
import requests

CPU_LIMIT = 80
MEMORY_LIMIT = 80
DISK_LIMIT = 80

timestamp = datetime.datetime.now()

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent

print("===================================")
print("Server Monitoring")
print("===================================")
print(f"Time   : {timestamp}")
print(f"CPU    : {cpu}%")
print(f"Memory : {memory}%")
print(f"Disk   : {disk}%")

if cpu > CPU_LIMIT:
    print("WARNING: High CPU usage!")

if memory > MEMORY_LIMIT:
    print("WARNING: High memory usage!")

if disk > DISK_LIMIT:
    print("WARNING: High disk usage!")

try:
    response = requests.get(
        "http://localhost:5000/health",
        timeout=5
    )

    if response.status_code == 200:
        print("Application: UP")
    else:
        print("Application: DOWN")

except Exception:
    print("Application: DOWN")
