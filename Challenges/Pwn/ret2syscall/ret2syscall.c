#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char binsh[] = "/bin/sh";

void gadget() {
    asm volatile(
    	"pop %rax;"
    	"ret;"
        "pop %rdi;"
        "ret;"
        "pop %rsi;"
        "pop %rdx;"
        "ret;"
        "syscall");
}

int main() {
    printf("Can you make a syscall?\n");
    char buf[60];
    read(0, buf, 0x100);
    return 0;
}

__attribute__((constructor)) void unbuffer() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

// gcc ret2syscall.c -fno-stack-protector -no-pie -o ret2syscall
