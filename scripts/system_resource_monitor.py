import psutil


print(f"CPU count: {psutil.cpu_count()}")
print(f"CPU stats: {psutil.cpu_stats()}")
print(f"Memory swap: {psutil.swap_memory()}")
print(f"CPU: {psutil.cpu_percent()}%, Memory: {psutil.virtual_memory().percent}%")
print(f"Disk partitions: {psutil.disk_partitions()}")
