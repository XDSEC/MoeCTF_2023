#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include <stdio.h>
#include <stdint.h>
unsigned char enc[65];
unsigned char flag[65] = { 0x5a,0xe3,0x6b,0xe4,0x6,0x87,0x2,0x4f,0x43,0xdf,0xcd,0xc1,0x77,0x98,0x6b,0xdb,0x8f,0x38,0x43,0x99,0xe3,0x93,0x22,0xb5,0x23,0xfd,0xb0,0x1c,0xe5,0xe3,0xee,0xce,0x2f,0x1d,0xad,0x2b,0xa4,0x15,0x98,0xf9,0xd8,0xeb,0x25,0xfa,0x6b,0x21,0xb7,0x72,0xb9,0x3,0x33,0x2e,0xd9,0x4c,0xeb,0x7b,0xf5,0xa7,0x48,0xf9,0x90,0x9d,0x38,0xfc, 0 };
unsigned char key1[16] = { "DX3906" };
unsigned char key2[16] = { "doctor3" };
unsigned char key3[16] = { "FUX1AOYUN" };
unsigned char key4[16] = { "R3verier" };
int idx = 0;

//-------anti-debug---------
typedef DWORD(WINAPI* ZW_SET_INFORMATION_THREAD) (HANDLE, DWORD, PVOID, ULONG);
#define ThreadHideFromDebugger 0x11
VOID DisableDebugEvent(VOID)
{
    HINSTANCE hModule;
    ZW_SET_INFORMATION_THREAD ZwSetInformationThread;
    hModule = GetModuleHandleA("Ntdll");
    ZwSetInformationThread = (ZW_SET_INFORMATION_THREAD)GetProcAddress(hModule, "ZwSetInformationThread");
    ZwSetInformationThread(GetCurrentThread(), ThreadHideFromDebugger, 0, 0);
}
//-------anti-debug---------

void my_scanf(const char* a, unsigned char* b)
{
    DisableDebugEvent();
    scanf(a, b);
}

/*
key1:DX3906
key2:doctor3
key3:FUX1AOYUN

moectf{WoOo00Oow_S0_interesting_y0U_C4n_C41l_M3tW1c3_BY_Unw1Nd~}
*/
void tea(uint32_t* v, uint32_t* k)
{
    uint32_t sum = 0;  // 注意sum也是32位无符号整型
    uint32_t v0 = v[0], v1 = v[1];
    uint32_t delta = 0x9e3779b9;
    uint32_t k0 = k[0], k1 = k[1], k2 = k[2], k3 = k[3];

    for (int i = 0; i < 32; i++) {
        sum += delta;
        v0 += ((v1 << 4) + k0) ^ (v1 + sum) ^ ((v1 >> 5) + k1);
        v1 += ((v0 << 4) + k2) ^ (v0 + sum) ^ ((v0 >> 5) + k3);

    }
    v[0] = v0;
    v[1] = v1;
    idx++;
    //printf("\nsum:%#x\n", sum);
}

EXCEPTION_DISPOSITION
__cdecl _except_handler(
    struct _EXCEPTION_RECORD* ExceptionRecord,
    void* EstablisherFrame,
    struct _CONTEXT* ContextRecord,
    void* DispatcherContext)
{
    tea((uint32_t*)enc + 8, (uint32_t*)key1);
    tea((uint32_t*)enc + 10, (uint32_t*)key2);
    tea((uint32_t*)enc + 12, (uint32_t*)key3);
    tea((uint32_t*)enc + 14, (uint32_t*)key4);

    return ExceptionContinueSearch;
}

void HomeGrownFrame(void)
{
    DWORD handler = (DWORD)_except_handler;
    __asm
    {
        push handler
        push FS : [0]
        mov FS : [0] , ES_PASSWORD
        int 3
        mov eax, [ESP]
        mov FS : [0] , EAX
        add esp, 8
    }
}

int main()
{
    DisableDebugEvent();
    puts("Welcome to moectf2023!!! Now you find YunZh1Jun's revenge!!!");
    puts("Do you know TEA(an encryption algorithm)? Do you know unwind in SEH? ");
    puts("I believe you can understand them! So let me check your flag~");
    printf("Input:");
    my_scanf("%64s", enc);

    __try {
        *(PDWORD)0 = 0;
    }
    __except (EXCEPTION_EXECUTE_HANDLER)
    {
        tea((uint32_t*)enc, (uint32_t*)key1);
        tea((uint32_t*)enc + 2, (uint32_t*)key2);
        tea((uint32_t*)enc + 4, (uint32_t*)key3);
        tea((uint32_t*)enc + 6, (uint32_t*)key4);
    }


    __try
    {
        HomeGrownFrame();
    }
    __except (EXCEPTION_EXECUTE_HANDLER)
    {
        for (int i = 0; i < 64; i++) {
            if (flag[i] != enc[i]) {
                puts("Ooooooooooops!Try again!");
                return 0;
            }
            //printf("%#x,", enc[i]);
        }
    }
    puts("Right flag! Have fun in moectf2023~");
    return 0;
}









