#include<vector>
#include<iostream>
using namespace std;

#include "Task.h"

#ifndef NODE_H
#define  NODE_H

class Node{
    private:
        bool state;

        vector<Task> Running_tasks;

        int number_of_cores;
        int number_of_gpus;
    public:
        Node(int cores, int gpus);
        bool return_state();
        void pass_second();
        bool add_task(Task t);
        void set_cores(int tmp);
        void set_gpus(int tmp);
        int get_cores();
        int get_gpus();
};

#endif