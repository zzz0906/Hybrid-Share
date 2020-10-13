#include<iostream>
#ifndef TASK_H
#define  TASK_H

class Task{
    private:
        int id;
        int remaining_time;
        int used_cores;
        int used_gpus;
    public:
        Task(int id, int time, int cores, int gpus);
        int get_id();
        int get_remaining_time();
        int get_cores();
        int get_gpus();
        void set_id(int tmp);
        
        void set_remaining_time(int tmp);
        void set_cores(int tmp);
        void set_gpus(int tmp);
        void pass_time();
};
#endif