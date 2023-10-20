//gcc shellcode.c -o shellcode -g -masm=intel
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <errno.h>
#include <sys/stat.h>
#include <unistd.h>
#include <string.h>

void init()
{
	char* p_map;

	setvbuf(stdin, 0, 2, 0);
	setvbuf(stdout, 0, 2, 0);
	setvbuf(stderr, 0, 2, 0);
	
	//内存映射 
	p_map = (char *)mmap((char*)0x114514000, 0x1000, PROT_READ | PROT_WRITE | PROT_EXEC, 34, -1, 0); 
	if(p_map == MAP_FAILED) 
	{ 
		printf("mmap fail\n"); 
		exit(1);
	} 

}

void filter(char* buf, int len)
{
	int i;
	for(i = 0; i < len - 1; i++)
	{
		if(buf[i] == '\x0f' && buf[i+1] == '\x05')
		{	
			puts("Is that 'syscall'?");
			buf[i] = 0;
			buf[i+1] = 0;
			puts("Oh, nothing.");
		}
	}
}

int main()
{
	char buf[0x28];

	init();

	memset(buf, 0, 0x28);
	puts("Please input your shellcode: ");
	read(0, buf, 0x28);
	
	filter(buf, 0x28);
	memcpy((char*)0x114514000, buf, 0x28);
	
	__asm("mov rdx, 0x114514000; jmp rdx");
	return 0;
}
