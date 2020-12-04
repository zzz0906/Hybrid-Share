from Task import *
from Job import *
class Job_Generator():
    def __init__(self) -> None:
        pass

    def fixed_jobs(self,J,T,time,cpun,gpun,memb,nicb):
        jid = 1
        jobs = []
        for _ in range(J):
            tasks = []
            tid = 1
            for _ in range(T):
                tasks.append(Task(jid,tid,time,cpun,gpun,memb,nicb))
                tid += 1
            jobs.append(Job(jid,tasks))
            jid += 1
        return jobs
    