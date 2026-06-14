#include<stdio.h>
int main(int argc ,char **argv[]){

    int sum = 0;
    for(int i=1 ;i<argc ;i++){
        sum = sum + argv[i];
        
    }
    printf("The sum of all the number as %d :\n",sum);
    return 0;
}