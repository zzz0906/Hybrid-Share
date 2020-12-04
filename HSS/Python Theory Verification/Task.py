class Task:
    '''
    time means the running time of the task
    cpun means the number of CPU needs for the task
    gpun means the number of GPU needs for the task
    memb means the average of memory bandwidth needed for the task
    nicb means the average of network bandwidth needed for the task
    '''
    def __init__(self, jid, id, time, cpun, gpun, memb, nicb):
        self.id = id
        self.jid = jid
        self.time = time
        self.runningtime = 0
        self.waitingtime = 0
        self.cpun = cpun
        self.gpun = gpun
        self.memb = memb
        self.nicb = nicb

    def get_cpun(self):
        return self.cpun

    def get_gpun(self):
        return self.gpun

    def get_memb(self):
        return self.memb
    
    def get_nicb(self):
        return self.nicb

    def get_remaining_time(self):
        return self.time - self.runningtime
    
    def count_wait(self):
        self.waitingtime += 1
        
    def print_info(self):
        print("******************** Task {} ********************".format(self.id))
        print("jid: {}".format(self.jid))
        print("time: {}".format(self.time))
        print("runningtime: {}".format(self.runningtime))
        print("cpun: {}".format(self.cpun))
        print("gpun: {}".format(self.gpun))
        print("memb: {}".format(self.memb))
        print("nicb: {}".format(self.nicb))
        
        
        