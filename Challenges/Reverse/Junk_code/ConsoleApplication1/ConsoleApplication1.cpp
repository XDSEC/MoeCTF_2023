#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>


int enc1(char* flag, int len1)
{
    unsigned char part1[18] = { 0 };
    int i;
    char tmp;
    __asm {
        test eax ,eax
        _emit 0x74
        _emit 0x1
        _emit 0xe8
    }
    static unsigned char enc1[] = "hj`^oavt+pZm`h+q._";
    for (i = 0; i < len1; ++i)
    {
        tmp = *flag++;
        *(part1 + i) = tmp;
    }
    for (i = 0; i < len1; ++i)
    {
        *(part1 + i ) -=0x5;
    }
    for (i = 0; i < len1; ++i)
    {
        if (enc1[i] != *(part1 + i))
        {
            return 0;
        }
    }
    return 1;
}
int enc2(char* flag, int len2)
{

    __asm {
        _emit 0x74
        _emit 0x3
        _emit 0x75
        _emit 0x1
        _emit 0xe8

    }

    const static  char enc2[] = { 0x39,0x12,0xe,0x55,0x39,0xc,0x13,0x8,0xd,0x39,0x5,0x56,0x2,0x55,0x47,0x47,0x47,0x1b ,0};
    int i;
    for (i = 0; i < len2; ++i)
    {
        flag[i] ^= 0x66;
    }
    return !strncmp(enc2, flag,len2); 
}
int main()
{
    //static char flag[] = "moectf{y0u_rem0v3d_th3_junk_c0d3!!!}";
    puts("welcome to moectf\nyour flag:");
    char flag[37];
    flag[36] = '\0';
    scanf("%36s", flag);
    int len = strlen(flag) >> 1;
    if (len != 18)
    {
        puts("WORNG!");
        return 0;
    }
    if (enc1(flag, len) && enc2(&flag[len], len))
        puts("congratulations!!!");
    else
        puts("WORNG!");
    return 0;
}