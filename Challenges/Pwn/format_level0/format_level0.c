//gcc format_level0.c -o format_level0 -g -m32 -z now
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>

void init()
{
    	setvbuf(stdin,0,_IONBF,0);
    	setvbuf(stdout,0,_IONBF,0);
    	setvbuf(stderr,0,_IONBF,0);
}

int main()
{
	char flag[0x50];
	char name[0x50];

	init();
	
	memset(flag, 0, 0x50);
	memset(name, 0, 0x50);

	int fd = open("flag", 0, 0);
        if(fd == -1)
        {
                puts("open flag error!");
                exit(0);
        }
        read(fd, flag, 0x50);
        close(fd);	

	puts("Please input your name:");
        read(0, name, 0x50);
        printf("Your name is: ");
        printf(name);
	return 0;
}
