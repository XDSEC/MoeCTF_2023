#include<stdio.h>
#include <windows.h>
#include<string.h>

unsigned char enc[]={0x9f,0x91,0xa7,0xa5,0x94,0xa6,0x8d,0xb5,0xa7,0x9c,0xa6,0xa1,0xbf,0x91,0xa4,0x53,0xa6,0x53,0xa5,0xa3,0x94,0x9b,0x91,0x9e,0x8f};

void check(char *input) {
    int right = 1;
    for (int i = 0; i < strlen(input) ; ++i) {
        if((((input[i]+0x39)&0xff)^0x39)!= enc[i]) {
            right = 0;
        }
    }
    if (right == 0) {
        printf("Try again please");
    } else {
        printf("GOOD");
    }
}

void decrypt() {
    unsigned long old = (unsigned long) malloc(8);
    char *pcheck = check;
    int len = 167;
    char *addr = pcheck - (unsigned long) pcheck % 4096;
    VirtualProtect(addr, 4096, PAGE_EXECUTE_WRITECOPY, &old);
    for (int i = 0; i < len; i++) {
        *(pcheck + i) = (*(pcheck + i) ^ 0x66);
    }
}

int main() {
    char input[100];
    printf("Plz input your flag:\n");
    scanf("%s", input);
    decrypt();
    check(input);
}