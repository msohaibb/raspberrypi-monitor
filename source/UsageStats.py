import psutil

class UsageStats:

    @staticmethod
    def find_cpu_usage():
        cpu_usage = psutil.cpu_percent()
        return str(cpu_usage)

    @staticmethod
    def find_ram_usage():
        memory_usage_percentage = psutil.virtual_memory()[2]
        return memory_usage_percentage
