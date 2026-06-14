#include<unistd.h>
int main(){
	//printf("Enter something");//library calls 
	write(STDOUT_FILENO,"Enter something\n", 16 ); //a system call  through which we can write output  ** System CAll

	char buf[10];
	// scanf("%s",buf);  // library call
	int n = read(STDIN_FILENO,buf,10);  

	write(STDOUT_FILENO,"You entered: ",13);

	write(STDOUT_FILENO,buf,n);

	return 0;

}
