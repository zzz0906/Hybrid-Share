#include "Task.h"
#include <iostream>
using namespace std;

#define N 20
#define T 10

Task::Task(int id, int time, int cores, int gpus, int mem){
    this->id = id;
    this->remaining_time = time;
    this->used_cores = cores;
    this->used_gpus = gpus;
    this->used_mem = mem;
}

int Task::get_id(){
    return this->id;
}
int Task::get_remaining_time(){
    return this->remaining_time;
}
int Task::get_cores(){
    return this->used_cores;
}
int Task::get_gpus(){
    return this->used_gpus;
}
int Task::get_mem(){
    return this->used_mem;
}
void Task::set_mem(int tmp){
    this->used_mem = tmp;
}
void Task::set_id(int tmp){
    this->id = tmp;
}
void Task::set_remaining_time(int tmp){
    this->remaining_time = tmp;
}
void Task::set_cores(int tmp){
    this->used_cores = tmp;
}
void Task::set_gpus(int tmp){
    this->used_gpus = tmp;
}
void Task::pass_time(){
    this->remaining_time--;
}

int main(){
    /*
        t
        n
        c(cpus) g(gpus) m(memory) b(bandwidth) 
    */
    for (int i = 0; i < T; i++){
        int t;
        int n;
        int c;
        int g;
        int m;
    }
}