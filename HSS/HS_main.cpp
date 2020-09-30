#include <iostream>
#include <unistd.h> 
#include <string>
using namespace std;
/*
get current work dir
*/    
string getCwd(){  
    string path;  
    path = getcwd(NULL,0);  
    return path;  
}  
/*
Determine whether a file exist
*/
bool File_Exist(char* filename){
    File *fh = fopen(filename,"r");
    if(fh == NULL) return true;
    else return false;
}

int main(int argc, char** argv) 
{ 
    if (argc < 1){
        cout << "please refer to help to use the command" << endl; 
    }
    char* srun = "srun ";
    if File_Exist(argv[1]){
        //fork
        system(strcat(srun,argv[1]));
    }
    /*
    First Command
    */
} 