from Job import *
from Utils import *
from Policy import *
class Scheduler:
    def __init__(self,policy):
        pass
        self.policy = policy
        self.jobq = []
    '''
    The process of the scheduler recieve a task 
    '''
    def recieve_a_job(self, job:Job):
        self.jobq.append(job)
    
    '''
    The process of the scheduler return the task need to be run

    1. the scheduled jobid
    2. a list contain each task's allocated node id
    3. a list contains resources list in each nodes's 
    '''
    '''
    We consider a job (including multiple tasks) be scheduled at the same time
    '''
    def scheduling_a_job(self,nodelist):
        return self.policy.select(self.jobq,nodelist)
    
    '''
    schedule keep scheduling until there is no runnable job in the queue
    '''
    def step(self,nodelist):
        jobindex,nodeindex,places = self.scheduling_a_job(nodelist)
        
        while (jobindex != -1):
            for index in range(len(nodeindex)):
                nodelist[nodeindex[index]].allocate_task([self.jobq[jobindex].tasks[index]],[places[index]]) 
                # Basic policy only for each job index's task has a single node we can modify it to adapt to allocate_task
            self.jobq.pop(jobindex)
            jobindex,nodeindex,places = self.scheduling_a_job(nodelist)
    
