from Task import Task
import numpy as np
class Node:
    '''
    id means the id of the
    cpun means the number of CPU needs for the task
    gpun means the number of GPU needs for the task
    memb means the average of memory bandwidth needed for the task
    nicb means the average of network bandwidth needed for the task

    taskQ means the task run in this node
    '''
    def __init__(self, id, cpun, gpun, memb, nicb):
        self.id = id
        
        self.cpun = cpun
        self.gpun = gpun
        self.memb = memb
        self.nicb = nicb

        self.taskQ = []
        
        self.cpu = np.zeros(cpun)
        self.gpu = np.zeros(gpun)

        
        self.allocatecpu = 0
        self.allocategpu = 0

        self.allocatedmemb = 0
        self.allocatednicb = 0
    
    def get_cpun(self):
        return self.cpun

    def get_gpun(self):
        return self.gpun

    def get_memb(self):
        return self.memb
    
    def get_nicb(self):
        return self.nicb

    def get_free_cpun(self):
        return self.cpun - self.allocatecpu
    
    def get_free_gpun(self):
        return self.gpun - self.allocategpu

    def get_free_memb(self):
        return self.memb - self.allocatedmemb
    
    def get_free_nicb(self):
        return self.nicb - self.allocatednicb
        
    def get_taskQ_len(self):
        return len(self.taskQ)
    '''
    places: the each task refer to this node's resource then we need to 

    places[i] means the ith task
    places[i]['cpu'] = [0,1,2] means it need to use 0,1,2
    places[i]['gpu'] = [0,1,3] means it need to use 0,1,3
    '''
    def allocate_task(self,tasks:list,places:list):
        for index in range(len(tasks)):
            self.taskQ.append(tasks[index])
            for cpuid in places[index]['cpu']:
                self.cpu[cpuid] = len(self.taskQ)
                self.allocatecpu += 1
            for gpuid in places[index]['gpu']:
                self.gpu[gpuid] = len(self.taskQ)
                self.allocategpu += 1
            self.allocatedmemb += tasks[index].memb
            self.allocatednicb += tasks[index].nicb
    
    def finish_task(self,task_index):
        for cpuid in range(len(self.cpu)):
            if (self.cpu[cpuid] == task_index + 1):
                self.cpu[cpuid] = 0
                self.allocatecpu -= 1
        for gpuid in range(len(self.gpu)):
            if (self.gpu[gpuid] == task_index + 1):
                self.gpu[gpuid] = 0
                self.allocategpu -= 1
        self.allocatedmemb -= self.taskQ[task_index].memb
        self.allocatednicb -= self.taskQ[task_index].nicb
        self.taskQ.pop(task_index)
    
    def step(self):
        task_index = 0
        finish_task = []
        for task in self.taskQ:
            task.runningtime += 1
            if (task.runningtime == task.time):
                self.finish_task(task_index)
                finish_task.append(task)
            task_index += 1
        return finish_task
            
            
    def print_info(self):
        print("==================== Node {} ====================".format(self.id))
        print("cpun: {}".format(self.cpun))
        print("gpun: {}".format(self.gpun))
        print("memb: {}".format(self.memb))
        print("nicb: {}".format(self.nicb))
        print("allocatecpu: {}".format(self.allocatecpu))
        print("allocategpu: {}".format(self.allocategpu))
        print("allocated cpu position:")
        for i in range(len(self.cpu)):
            if (i != len(self.cpu) - 1):
                print(i,end=' ')
            else:
                print(i)
        for i in range(len(self.cpu)):
            if (i != len(self.cpu) - 1):
                print(self.cpu[i],end=' ')
            else:
                print(self.cpu[i])
        print("allocated gpu position:")
        for i in range(len(self.gpu)):
            if (i != len(self.gpu) - 1):
                print(i,end=' ')
            else:
                print(i)
        for i in range(len(self.gpu)):
            if (i != len(self.gpu) - 1):
                print(self.gpu[i],end=' ')
            else:
                print(self.gpu[i])
        print("allocatememb: {}".format(self.allocatedmemb))
        print("allocatenicb: {}".format(self.allocatednicb))
        print("taskQ:")
        for i in range(len(self.taskQ)):
            if (i != len(self.taskQ) - 1):
                self.taskQ[i].print_info()
            else:
                self.taskQ[i].print_info()
        

        