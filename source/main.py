from UsageStats import UsageStats
from time import sleep

for i in range(10):
    print("CPU Usage #1: " + UsageStats.find_cpu_usage())
    print(UsageStats.find_ram_usage())
    print()
    sleep(1)
