import subprocess


class Monitor:
    def __init__(self):
        self.get_storage()

    def get_temp(self):
        temp = subprocess.run(["/opt/vc/bin/vcgencmd", "measure_temp"], stdout=subprocess.PIPE)
        #isolate the temperature in C
        temp = str(temp.stdout).split('=')[1]
        temp = temp.split('\'')[0]
        return temp

    def get_storage(self):
        stor = subprocess.run(["df"], stdout=subprocess.PIPE)
        stor = str(stor.stdout).split("\\n")
        #isolate line of interest
        l2 = stor[1].split(" ")
        metrics =[]
        for token in l2:
            if token != "":
                metrics.append(token)
        self.__total_memory = metrics[1]
        #to return
        toreturn=[]
        toreturn.append(metrics[2])
        toreturn.append(metrics[4])
        return toreturn

    def get_total_storage(self):
        return self.__total_memory

    def get_cpu_usage(self):
        cpu = subprocess.run(["uptime"], stdout=subprocess.PIPE)
        cpu = str(cpu.stdout)
        print(cpu)
        

 