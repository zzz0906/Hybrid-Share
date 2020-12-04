from typing import Generator
from Node import *
from Cluster import *
from Job_Generator import *
from Basic_Policy import *
import numpy as np
# import argparse

# parser = argparse.ArgumentParser(description='SCSSP: Simulator for Comparing Sharing Scheduling Policy under Heterogeneous Jobs')
# parser.add_argument('integers', metavar='N', type=int, nargs='1',
#                     help='the number of the jobs')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

# args = parser.parse_args()
# print(args.accumulate(args.integers))

# 𝛼:𝑡ℎ𝑒 𝑡𝑖𝑚𝑒 coefficient of the sharing (**if there have interference in mem then 𝛼=(𝑚𝑖+𝑚𝑗)/𝑚 **
A = 0.9
#n: the number of nodes in the cluster
N = 4
# c: the number of CPUs per nodes
C = 20
#g: the number of GPUs per nodes
G = 8
#m: the memory per nodes
M = 256*1024*1024*1024

#nicb: the NIC bandwidth per nodes
NICB = 100*1024*1024*1024

HYPER = True

#J: the number of jobs
J = 100

# T: the number of tasks in a job
T = 1

if HYPER:
    C = C*2

Happens_time = []


def main():
    # 31536000 loop represent 1 year
    nodelist = []
    
    for i in range(N):
        node = Node(i,C,G,M,NICB)
        nodelist.append(node)
    
    Generator = Job_Generator()

    '''
    generate job and task in a fixed way
    jid; tid start from 1
    idex start from 0
    '''
    jobs = Generator.fixed_jobs(J,T,3,4,2,1024*1024*1024,1024*1024)

    '''
    generate job's start time

    /*****/
    we assume all task of a job start at the same time in this model. 
    we must schedule all these task into the cluster at the same time (gang scheduling for AI & HPC)
    /*****/

    If you want to modify it in there are some order or dependency between the tasks in the jobs.
    1. we need keep the job in the jobQ even if there are some task has been scheduled in the nodes
    2. we need to set the order of these jobs
    /*****/
    '''
    start_times = []
    start_times = np.zeros(len(jobs))

    '''
    generate scheduler by the policy
    '''    
    basic_policy = Basic_Policy_Share()
    scheduler = Scheduler(basic_policy)

    # '''
    # generate task inference as the profiling data
    # '''

    # start simulation
    M40_4 = Cluster(nodelist,scheduler,J*T)
    timestamp = 0

    #while (M40_4.finalize() == False):
    jobs_need_add = []
    for index in range(len(start_times)):
        if (start_times[index] == timestamp):
            jobs_need_add.append(jobs[index])
    if (len(jobs_need_add) != 0):
        M40_4.add_jobs(jobs_need_add)
    for node in nodelist:
        node.print_info()

    # never free
    M40_4.step()
    timestamp += 1
    
    print(timestamp)
    waiting_times = []
    for task in M40_4.finish_task:
        waiting_times.append(task.waitingtime)
    print("Average Respond Time {}".format(np.mean(waiting_times)))
    print("Throughput {}".format(round(J/timestamp,2)))

if __name__ == '__main__':
    print('==================== simulation begin ====================')
    main()