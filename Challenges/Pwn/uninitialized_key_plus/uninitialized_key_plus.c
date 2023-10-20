//gcc uninitialized_key_plus.c -o uninitialized_key_plus -g
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

void init()
{
    	setvbuf(stdin,0,_IONBF,0);
    	setvbuf(stdout,0,_IONBF,0);
    	setvbuf(stderr,0,_IONBF,0);
}

void welcome()
{
	puts("Welcome to Moectf 2023.");
	puts("Do you know stack?");
}

void get_name()
{
	char name[0x18] = "\x00";
	puts("Please input your name:");
	scanf("%24s", name);
	printf("Your name is %s.\n", name);
}

void get_key()
{
	int key;
	puts("Please input your key:");
	scanf("%5d", &key);
	if(key == 114514)
	{
		printf("This is my flag.\n");
		system("cat flag");
	}
}

int main()
{
	init();
	welcome();
	get_name();
	get_key();
	return 0;
}
