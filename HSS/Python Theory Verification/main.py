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
    
    for _ in range(N):
        node = Node(C,G,M,NICB)
        nodelist.append(node)
    
    Generator = Job_Generator()

    '''
    generate job and task in a fixed way
    '''
    jobs = Generator.fixed_jobs(J,T,100,4,2,1024*1024*1024,1024*1024)

    '''
    generate job's start time

    /*****/
    we assume all task of a job start at the same time in this model.
    
    You can modify it in there are some order between the tasks in the jobs
    /*****/
    '''
    start_times = []
    start_times = np.zeros(len(jobs))

    '''
    generate scheduler by the policy
    '''    
    basic_policy = Basic_Policy()
    scheduler = Scheduler(basic_policy)

    # '''
    # generate task inference as the profiling data
    # '''

    # start simulation
    M40_4 = Cluster(nodelist,scheduler,J*T)
    timestamp = 0
    while (M40_4.finalize() == False):
        jobs_need_add = []
        for index in range(len(start_times)):
            if (start_times[index] == timestamp):
                jobs_need_add.append(jobs[index])
        if (len(jobs_need_add) != 0):
            M40_4.add_jobs(jobs_need_add)
        M40_4.step()
        timestamp += 1
    
    print(timestamp)

if __name__ == '__main__':
    print('==================== simulation begin ====================')
    main()