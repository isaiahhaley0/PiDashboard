import subprocess

class Monitor:
    def __init__(self):
        pass

    def get_temp(self):
        temp = subprocess.run(["/opt/vc/bin/vcgencmd", "measure_temp"], stdout=subprocess.PIPE)
        #isolate the temperature in C
        temp = str(temp.stdout).split('=')[1]
        temp = temp.split('\'')[0]
        return temp

    def get_storage(self):
        stor = subprocess.run(["df"], stdout=subprocess.PIPE)
        stor = str(stor.stdout).split("\\n")
        for l in stor:
            print(l)
    
    def get_cpu_usage(self):
        cpu = subprocess.run(["uptime"], stdout=subprocess.PIPE)
        print(cpu.stdout)
        
 