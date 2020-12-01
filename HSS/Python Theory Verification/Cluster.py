from Node import *
from Scheduler import *

class Cluster:
    def __init__(self,nodeslist:list,scheduler:Scheduler,N:int):
        self.nodeslist = nodeslist
        self.scheduler = scheduler
        self.finish_task = []
        self.N = N

    def add_node(self,node:Node):
        self.nodeslist.append(node)
    
    def step(self):
        # scheduling a job into a node
        self.scheduler.step(self.nodeslist)

        # running 1s in a node
        for node in self.nodeslist:
            # records the task index in the nodes
            self.finish_task += node.step()

    def add_jobs(self,jobs:list):
        for job in jobs:
            self.scheduler.recieve_a_job(job)
        return True
    
    def finalize(self):
        if (len(self.finish_task) == self.N):
            return True
        return False

            
            
    