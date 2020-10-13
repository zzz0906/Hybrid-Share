#include "Node.h"

Node::Node(int cores, int gpus){
    this->number_of_cores = cores;
    this->number_of_gpus = gpus;
    //this-> = 0;
    this->state = true;
}

bool Node::return_state(){
    return state;
}

void Node::pass_second(){
    for (int i = 0; i < this->Running_tasks.size(); i++){
        this->Running_tasks[i].pass_time();
        if (this->Running_tasks[i].get_remaining_time() == 0){
            this->number_of_cores += this->Running_tasks[i].get_cores();
            this->number_of_gpus += this->Running_tasks[i].get_gpus();
            
            this->Running_tasks.erase(this->Running_tasks.begin()+i);
        
            i--;
        }
    }
    if (this->Running_tasks.empty()) this->state = true;
}

bool Node::add_task(Task t){
    if (t.get_cores() > this->number_of_cores || t.get_gpus() > this->number_of_gpus) return false;
    this->Running_tasks.push_back(t);
}

void Node::set_cores(int tmp){
    this->number_of_cores = tmp;
}

void Node::set_gpus(int tmp){
    this->number_of_gpus = tmp;
}

int Node::get_cores(){
    return this->number_of_cores;
}

int Node::get_gpus(){
    return this->number_of_gpus;
}