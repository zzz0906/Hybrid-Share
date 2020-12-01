from Node import *
from Task import *

def generate_place_dic_from_list(cpus,gpus):
    res = {}
    res['cpu'] = cpus
    res['gpu'] = gpus
    return res

def determine_single_task_single_node(task:Task,node:Node):
    if (task.get_cpun() <= node.get_free_cpun() and task.get_gpun() <= node.get_free_gpun() and task.get_memb() <= node.get_free_memb() and task.get_nicb() <= node.get_free_nicb()):
        return True

def main():
    task = Task(1000,16,0,1024*1024*1024,0)
    node = Node(40,4,1024*1024*1024*200,1024*1024*1024*100)
    print(determine_single_task_single_node(task,node))
if __name__ == '__main__':
    main()
    