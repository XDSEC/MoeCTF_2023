#include<stdio.h>
#include<string.h>

int main(){
	char code[100] = {};
	gets(code);
	if(strlen(code)){
	    memset(code,0,100);
	}
	void (*p)();
	p = &code[1];
	p();
	return 0;
}
__attribute__((constructor)) void unbuffer() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}
//gcc shellcode_level2.c -o shellcode_level2 -z execstack
