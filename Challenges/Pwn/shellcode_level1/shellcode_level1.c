#include<stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>

char paper1[100];

int main(){
    
    char shellcode[100] ={};
    char  paper2[100] = {};
    char *paper3 = malloc(100);
    void *paper4 = mmap(NULL, 100, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
    void *paper5 = mmap(NULL, 100, PROT_READ|PROT_WRITE|PROT_EXEC, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
    void (*p)();
    int choise = 0;

    printf("Which paper will you choose?\n");
    scanf("%d",&choise);
    printf("what do you want to write?\n");
    scanf("%s",shellcode);

    if(choise == 1){
	memcpy(paper1, shellcode, sizeof(shellcode));
	p = paper1;
    }else if(choise == 2){
	memcpy(paper2, shellcode, sizeof(shellcode));
	p = paper2;
    }else if(choise == 3){
	memcpy(paper3, shellcode, sizeof(shellcode));
	p = paper3;
    }else if(choise == 4){
	memcpy(paper4, shellcode, sizeof(shellcode));
	p = paper4;
	mprotect(paper4, 0x1000, PROT_READ | PROT_WRITE | PROT_EXEC);
    }else if(choise == 5){
	memcpy(paper5, shellcode, sizeof(shellcode));
	p = paper5;
	mprotect(paper5, 0x1000, PROT_NONE);
    }

    p();
    return 0;
}

__attribute__((constructor)) void unbuffer() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}
// gcc shellcode_level1.c -o shellcode_level1 -g

