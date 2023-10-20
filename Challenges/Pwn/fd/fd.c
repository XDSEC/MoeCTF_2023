//gcc fd.c -o fd -g
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main()
{
	int input = 0;
	char flag[0x50];
	puts("Do you know fd?");
	int fd = open("./flag", 0, 0);

	int new_fd = (fd<<2) | 666;
	dup2(fd, new_fd);
	close(fd);

	puts("Which file do you want to read?");
	puts("Please input its fd: ");
	scanf("%d", &input);
	read(input, flag, 0x50);
	puts(flag);

	return 0;
}
