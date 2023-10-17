#include<stdio.h>
#include<unistd.h>
#include<sys/mman.h>
#include<string.h>

//char code[5] = {0xE8,0x4d,0xD1,0xFF,0xFF};
char code[5];
void givemeshell(){
    system("/bin/sh");
}

int main(){
	printf("5 bytes ni neng miao sha wo?\n");
	mprotect(0x404000,0x1000,7);
	gets(code);
	void (*p)();
	p = code;
	memset(&code[5],0,0xF72);
	p();
	return 0;
}
__attribute__((constructor)) void unbuffer() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}
//  gcc shellcode_level3.c -o shellcode_level3 -no-pie -g
