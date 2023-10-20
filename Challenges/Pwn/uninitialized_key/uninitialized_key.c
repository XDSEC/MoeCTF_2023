//gcc uninitialized_key.c -o uninitialized_key -g
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
	int age = 0;
	puts("Please input your age:");
	scanf("%d", &age);
	printf("Your age is %d.\n", age);
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
