class Job:
    def __init__(self,id,tasks):
        self.tasks = tasks
        self.id = id
        self.number_of_tasks = len(tasks)
        self.waiting_time = 0
    
    def count_wait(self):
        for task in self.tasks:
            task.count_wait()