class Job:
    def __init__(self,id,tasks):
        self.tasks = tasks
        self.id = id
        self.number_of_tasks = len(tasks)
