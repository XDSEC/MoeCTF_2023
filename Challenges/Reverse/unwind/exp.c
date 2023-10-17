#include <stdio.h>
#include <stdint.h>

unsigned char key1[16] = { "DX3906" };
unsigned char key2[16] = { "doctor3" };
unsigned char key3[16] = { "FUX1AOYUN" };
unsigned char key4[16] = { "R3verier" };

void decrypt (uint32_t* v, uint32_t* k) {
    uint32_t v0 = v[0], v1 = v[1];
    uint32_t delta = 0x9e3779b9;
    uint32_t sum = delta * 32;
    uint32_t k0 = k[0], k1 = k[1], k2 = k[2], k3 = k[3];

    for (int i=0; i<32; i++) {
        v1 -= ((v0<<4) + k2) ^ (v0 + sum) ^ ((v0>>5) + k3);
        v0 -= ((v1<<4) + k0) ^ (v1 + sum) ^ ((v1>>5) + k1);
        sum -= delta;
    }

    v[0]=v0; 
    v[1]=v1;
}

int main()
{
    //unsigned char enc[33]={"moectf{C41l_m3_tW1c3_BY_Unw1Nd~}"};
    unsigned char enc[]={0x5a,0xe3,0x6b,0xe4,0x6,0x87,0x2,0x4f,0x43,0xdf,0xcd,0xc1,0x77,0x98,0x6b,0xdb,0x8f,0x38,0x43,0x99,0xe3,0x93,0x22,0xb5,0x23,0xfd,0xb0,0x1c,0xe5,0xe3,0xee,0xce,0x2f,0x1d,0xad,0x2b,0xa4,0x15,0x98,0xf9,0xd8,0xeb,0x25,0xfa,0x6b,0x21,0xb7,0x72,0xb9,0x3,0x33,0x2e,0xd9,0x4c,0xeb,0x7b,0xf5,0xa7,0x48,0xf9,0x90,0x9d,0x38,0xfc,0};

    decrypt((uint32_t*)enc, (uint32_t*)key1);
    decrypt((uint32_t*)enc+2, (uint32_t*)key2);
    decrypt((uint32_t*)enc+4, (uint32_t*)key3);
    decrypt((uint32_t*)enc+6, (uint32_t*)key4);
    
    decrypt((uint32_t*)enc+8, (uint32_t*)key1);
    decrypt((uint32_t*)enc+10, (uint32_t*)key2);
    decrypt((uint32_t*)enc+12, (uint32_t*)key3);
    decrypt((uint32_t*)enc+14, (uint32_t*)key4); 
    decrypt((uint32_t*)enc+8, (uint32_t*)key1);
    decrypt((uint32_t*)enc+10, (uint32_t*)key2);
    decrypt((uint32_t*)enc+12, (uint32_t*)key3);
    decrypt((uint32_t*)enc+14, (uint32_t*)key4); 

    printf("%s",enc);

    return 0;
}

