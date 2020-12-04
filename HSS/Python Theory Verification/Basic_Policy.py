from Policy import *
from Utils import *
from Node import *
from Task import *
import numpy as np

class Basic_Policy_Exclusive(Policy):
    def __init__(self):
        pass
    
    def select(self,joblist, nodelist):
        job_index = 0
        # find a job can run in the nodes
        node_index = 0
        # in basical ploicy, if a task dominate a node, it means it has been used. (no share)
        FLAG_WHETHER_USED_NODE = np.zeros(len(nodelist))
        for node in nodelist:

            if (node.get_taskQ_len() > 0):
                FLAG_WHETHER_USED_NODE[node_index] = 1
            node_index += 1

        for job in joblist:

            CAN_ALL_TASK_BE_SCHEDULED = True
            FLAG_WHETHER_USED_NODE_THIS_JOB = FLAG_WHETHER_USED_NODE
            job_node_id = []
            job_places = [] # if this job can be scheduled, this job will be scheduled

            for task in job.tasks:    
                # determine a task can be scheduled
                node_index = 0
                CAN_THIS_TASK_BE_SCH = False
               
                for node in nodelist:
                    if (FLAG_WHETHER_USED_NODE_THIS_JOB[node_index] == 0 and determine_single_task_single_node(task,node)):# this node haven't been allocated
                        FLAG_WHETHER_USED_NODE_THIS_JOB[node_index] = 1
                        CAN_THIS_TASK_BE_SCH = True
                        break
                    node_index += 1
                # this task cannot be scheduled
                if (CAN_THIS_TASK_BE_SCH == False):
                    CAN_ALL_TASK_BE_SCHEDULED = False
                    break
                else:
                    job_node_id.append(node_index) # index means the position in the list
                    job_places.append(self.generate_places(task,nodelist[node_index]))
                    
            #  all task in this job can be scheduled return it!
            if (CAN_ALL_TASK_BE_SCHEDULED):
                return job_index,job_node_id,job_places

            job_index += 1
        return -1,[],[]

    def generate_places(self,task:Task,node:Node):
        cpus = []
        reqc = task.get_cpun()
        cur = 0
        # in basic policy we allocate resources in order for the job
        for cpuid in range(len(node.cpu)):
            if (cur == reqc):
                break
            if (node.cpu[cpuid] == 0):
                cur += 1
                cpus.append(cpuid)
                
        gpus = []
        cur = 0
        for gpuid in range(len(node.gpu)):
            if (cur == task.get_gpun()):
                break
            if (node.gpu[gpuid] == 0):
                cur += 1
                gpus.append(gpuid)
        return generate_place_dic_from_list(cpus,gpus)
        
class Basic_Policy_Share(Policy):
    def __init__(self):
        pass
    
    def select(self,joblist, nodelist):
        job_index = 0
        # find a job can run in the nodes
        node_index = 0
        # in basical ploicy, if a task dominate a node, it means it has been used. (no share)
        FLAG_WHETHER_USED_NODE = np.zeros(len(nodelist))
        
        for job in joblist:

            CAN_ALL_TASK_BE_SCHEDULED = True
            job_node_id = []
            job_places = [] # if this job can be scheduled, this job will be scheduled

            for task in job.tasks:    
                # determine a task can be scheduled
                node_index = 0
                CAN_THIS_TASK_BE_SCH = False
               
                for node in nodelist:
                    if (determine_single_task_single_node(task,node)):# this node haven't been allocated
                        CAN_THIS_TASK_BE_SCH = True
                        break
                    node_index += 1
                # this task cannot be scheduled
                if (CAN_THIS_TASK_BE_SCH == False):
                    CAN_ALL_TASK_BE_SCHEDULED = False
                    break
                else:
                    job_node_id.append(node_index) # index means the position in the list
                    job_places.append(self.generate_places(task,nodelist[node_index]))
                    
            #  all task in this job can be scheduled return it!
            if (CAN_ALL_TASK_BE_SCHEDULED):
                return job_index,job_node_id,job_places

            job_index += 1
        return -1,[],[]

    def generate_places(self,task:Task,node:Node):
        cpus = []
        reqc = task.get_cpun()
        cur = 0
        # in basic policy we allocate resources in order for the job
        for cpuid in range(len(node.cpu)):
            if (cur == reqc):
                break
            if (node.cpu[cpuid] == 0):
                cur += 1
                cpus.append(cpuid)
                
        gpus = []
        cur = 0
        for gpuid in range(len(node.gpu)):
            if (cur == task.get_gpun()):
                break
            if (node.gpu[gpuid] == 0):
                cur += 1
                gpus.append(gpuid)
        return generate_place_dic_from_list(cpus,gpus)
        
        