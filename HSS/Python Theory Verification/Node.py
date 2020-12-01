import numpy as np
class Node:
    '''
    cpun means the number of CPU needs for the task
    gpun means the number of GPU needs for the task
    memb means the average of memory bandwidth needed for the task
    nicb means the average of network bandwidth needed for the task

    taskQ means the task run in this node
    '''
    def __init__(self, cpun, gpun, memb, nicb):
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
            if (self.cpu[gpuid] == task_index + 1):
                self.cpu[gpuid] = 0
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
            
            
    