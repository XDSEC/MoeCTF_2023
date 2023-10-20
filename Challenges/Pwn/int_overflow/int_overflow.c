//gcc int_overflow.c -o int_overflow -g
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>

void backdoor()
{
	puts("Oh, you know it.");
	puts("This is flag:");
	system("cat flag");
	exit(0);
}

void init()
{
    	setvbuf(stdin,0,_IONBF,0);
    	setvbuf(stdout,0,_IONBF,0);
    	setvbuf(stderr,0,_IONBF,0);
}

void get_input(int* n)
{
	char s[0x20];
	read(0, s, 0x1f);
	if(strchr(s, '-'))
		*n = 0;
	else
		*n = atoi(s);
}

void vuln()
{
	int n;
	
	puts("Welcome to Moectf2023.");
	puts("Do you know int overflow?");
	puts("Can you make n == -114514 but no '-' when you input n.");
	puts("Please input n:");
	get_input(&n);
	if(n == -114514)
		backdoor();
	else
		puts("Maybe you should search and learn it.");
}

int main()
{
	init();
	vuln();
	return 0;
}
