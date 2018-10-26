import subprocess


class UsageStats:

    @staticmethod
    def find_cpu_usage():
        cpu_usage = str(subprocess.check_output("wmic cpu get loadpercentage"))
        cpu_usage = cpu_usage.replace("b", "")
        cpu_usage = cpu_usage.replace("Load", "")
        cpu_usage = cpu_usage.replace("Pe", "")
        cpu_usage = cpu_usage.replace("ce", "")
        cpu_usage = cpu_usage.replace("tage", "")
        cpu_usage = cpu_usage.replace("\\", "")
        cpu_usage = cpu_usage.replace("r", "")
        cpu_usage = cpu_usage.replace("n", "")
        cpu_usage = cpu_usage.replace("'", "")
        cpu_usage = cpu_usage.replace(" ", "")
        cpu_usage = cpu_usage
        return cpu_usage

    @staticmethod
    def find_ram_usage():
        total_memory = str(subprocess.check_output("wmic OS get TotalVisibleMemorySize"))
        total_memory = total_memory.replace("b'TotalVisibleMemorySize ", "")
        total_memory = total_memory.replace("\\", "")
        total_memory = total_memory.replace("r", "")
        total_memory = total_memory.replace("n", "")
        total_memory = total_memory.replace("'", "")
        total_memory = total_memory.replace(" ", "")

        free_memory = str(subprocess.check_output("wmic OS get FreePhysicalMemory"))
        free_memory = free_memory.replace('b', "")
        free_memory = free_memory.replace("F", "")
        free_memory = free_memory.replace('e', "")
        free_memory = free_memory.replace('Physical', "")
        free_memory = free_memory.replace('M', "")
        free_memory = free_memory.replace('mo', "")
        free_memory = free_memory.replace('y', "")
        free_memory = free_memory.replace("\\", "")
        free_memory = free_memory.replace("r", "")
        free_memory = free_memory.replace("n", "")
        free_memory = free_memory.replace("'", "")
        free_memory = free_memory.replace(" ", "")

        memory_usage_percentage = str("%6.2f" % ((float(total_memory) - float(free_memory)) / float(total_memory) * 100))
        return memory_usage_percentage
