#include<stdio.h>

int main(){
	char code[100] = {};
	gets(code);
	void (*p)();
	p = code;
	p();
	return 0;
}
__attribute__((constructor)) void unbuffer() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}
//gcc shellcode_level0.c -o shellcode_level0 -z execstack
