#include<unistd.h>
#include<stdlib.h>
#include<stdio.h>
int main(){
	int a,b,sum;
	char buf[10],str[100];
	write(STDOUT_FILENO, "Enter first Number:\n ",21);
	read(STDOUT_FILENO,buf,10);
	a = atoi(buf);

	write(STDOUT_FILENO,"Enter 2nd Number ",17);
	read(STDOUT_FILENO,buf,10);
	b = atoi(buf);

	sum = a + b;

	sprintf(str,"the sum is %d \n",sum);  //is library call
	write(STDOUT_FILENO,str,sizeof(str)); //sizeof or length str is used to  find the size 

	return 0;
}
