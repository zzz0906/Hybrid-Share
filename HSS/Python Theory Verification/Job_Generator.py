from Task import *
from Job import *
class Job_Generator():
    def __init__(self) -> None:
        pass

    def fixed_jobs(self,J,T,time,cpun,gpun,memb,nicb):
        jid = 0
        jobs = []
        for _ in range(J):
            tasks = []
            tid = 0
            for _ in range(T):
                tasks.append(Task(jid,tid,time,cpun,gpun,memb,nicb))
            jobs.append(Job(jid,tasks))
        return jobs
    