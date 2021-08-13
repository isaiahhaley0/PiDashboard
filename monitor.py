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

    

        