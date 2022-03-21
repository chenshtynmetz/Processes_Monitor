import platform

class Manual:
    def __init__(self, time1, time2, my_time):
        self.time1 = time1
        self.time2 = time2
        self.my_time = my_time
        self.system = platform.system()
        self.serviceList = "serviceList.txt"
        self.monitoring()

    def monitoring(self):
        first_index = -1
        second_index = -1
        with open(self.serviceList, "r") as f:
            lines = f.readlines()
        for i in range(len(lines)):
            if lines[i] == self.time1:
                first_index = i
            if lines[i] == self.time2:
                second_index = i

