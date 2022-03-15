import platform
import os
import time
from datetime import datetime


class Monitor:
    def __init__(self):
        self.my_time = input("please enter period of time in seconds:")
        self.system = platform.system()
        self.serviceList = "serviceList.txt"
        self.status_log = "Status_Log.txt"
        self.flag = 1
        self.monitoring()

# this function monitor the active processes and write them to file
    def monitoring(self):
        if self.system == "Windows":
            curr_proc = ""
            while True:
                if self.flag == 0:
                    return
                curr_time = "\n" + str(datetime.now()) + "\n"
                prev_proc = curr_proc
                curr_proc = os.popen("tasklist").read()
                self.compare(curr_proc, prev_proc, curr_time)
                with open(self.serviceList, "a") as file:
                    file.write(curr_time)
                    file.write(curr_proc)
                # print(curr_time)
                # print(curr_proc)
                time.sleep(float(self.my_time))
        if self.system == "Linux":
            pass

# this function check if something changes
    def compare(self, curr, prev, curr_time):
        prev_list = prev.split('\n')  # split the process list by lines
        curr_list = curr.split('\n')
        prev_id_list = [1, 1, 1]
        curr_id_list = [1, 1, 1]
        for i in range(3, len(prev_list)):  # get process by ID
            prev_id_list.append(prev_list[i][26:33])  # todo: check if pid is the id of the process
        for i in range(3, len(curr_list)):
            curr_id_list.append(curr_list[i][26:33])  # get process by ID
        with open(self.status_log, "a") as file:  # write the differences between the files
            file.write('\n' + curr_time + '\n')
            print('\n' + curr_time + '\n')
            for i in range(3, len(prev_list)):
                if prev_id_list[i] not in curr_id_list:
                    file.write("stopped:" + '\t' + prev_list[i] + '\n')
                    print("stopped:" + '\t' + prev_list[i] + '\n')
            for i in range(3, len(curr_list)):
                if curr_id_list[i] not in prev_id_list:
                    file.write("started:" + '\t' + curr_list[i] + '\n')
                    print("started:" + '\t' + curr_list[i] + '\n')

    def exit_monitor(self):
        self.flag = 0
