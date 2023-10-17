#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <string.h>

void action(char * str) { execve(str,0,0); }

int makebinsh() {

	const char cs[] = "/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    int input[7];
    char* str = (char*)malloc(8 * sizeof(char));
	memset(str,0,8 * sizeof(char));

    srand(time(NULL));
    printf("Input seven single digits:\n");


    for (int i = 0; i < 7; i++) {
        scanf("%d", &input[i]);
    }


    if (input[1] * input[3] == input[4]*10 + input[5]) {
    	strncat(str,&cs[0],1);
    } else {
        strncat(str,&cs[(int)(((double)rand() / RAND_MAX) * 53)],1);
    }
    
    if(input[5] == input[6] + 1){
		strncat(str,&cs[2],1);
	} else {
		strncat(str,&cs[(int)(((double)rand() / RAND_MAX) * 53)],1);
	}
    
    
    strncat(str,&cs[input[1]],1);
    

    if(input[1] == input[3]){
		strncat(str,&cs[14],1);
	} else {
		strncat(str,&cs[(int)(((double)rand() / RAND_MAX) * 53)],1);
	}
	
	strncat(str,&cs[input[6]],1);

	if(input[0] == input[2]){
		strncat(str,&cs[19],1);
	} else {
		strncat(str,&cs[(int)(((double)rand() / RAND_MAX) * 53)],1);
	}
	
	if(input[3] - input[4] == input[0]){
		strncat(str,&cs[8],1);
	} else {
		strncat(str,&cs[(int)(((double)rand() / RAND_MAX) * 53)],1);
	}


	printf("Here's the string:%s\n",str);
    printf("The address is:%p\n",(void*)str);


    return 0;
}

void gadget() {
    asm volatile(
        "pop %rdi;"
        "ret;");
}


int main() {
	makebinsh();
    char wish[64];
    printf("What do you want?");
    read(0, wish, 0x64);
    return 0;
}

__attribute__((constructor)) void unbuffer() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}


// gcc rePWNse.c -fno-stack-protector -no-pie -z now -o rePWNse
