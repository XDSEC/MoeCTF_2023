#include<stdio.h>
#include<string.h>


void rc4_enc(unsigned char *S_table, unsigned char *T_table,unsigned char *arr,unsigned int len,unsigned char *k,unsigned int len_k)
{
  int i, j = 0, tmp, key,index=0;
  for (i = 0; i < 256; i++)
  {
    S_table[i] = i;
    T_table[i] = k[i % len_k];
  }
  for (i = 0; i < 256; i++)
  {
    j = (j + S_table[i] + T_table[i]) % 256;
    tmp = S_table[j];
    S_table[j] = S_table[i];
    S_table[i] = tmp;
  }
  i = 0;
  j = 0;
  while (len > 0)
  {
    i = (i + 1) % 256;
    j = (j + S_table[i]) % 256;
    tmp = S_table[j];
    S_table[j] = S_table[i];
    S_table[i] = tmp;
    key = (S_table[i] + S_table[j]) % 256;
    arr[index] =arr[index]^ S_table[key];
    index++;
    len--;
  }
}

int main()
{
  unsigned char arr[37]={0},data[37]={0x1B, 0x9B, 0xFB, 0x19, 0x06, 0x6A, 0xB5, 0x3B, 0x7C, 0xBA, 0x03, 0xF3, 0x91, 0xB8, 0xB6, 0x3D, 0x8A, 0xC1, 0x48, 0x2E, 0x50, 0x11, 0xE7, 0xC7, 0x4F, 0xB1, 0x27, 0xCF, 0xF3, 0xAE, 0x03, 0x09, 0xB2, 0x08, 0xFB, 0xDC, 0x22};
  unsigned char S_table[256]={0},T_table[256]={0},k[]="moectf2023";
  int flag=0;
  puts("welcome to moectf!!!");
  puts("show your flag:");
  //moectf{y0u_r3a11y_understand_rc4!!!!}
  scanf("%s",arr);
  if (strlen(arr)==37)
  {
    rc4_enc(S_table,T_table,arr,sizeof(arr),k,sizeof(k)-1);
    for (int i = 0; i < sizeof(arr); i++)
	  {
		  if(data[i]==arr[i])
        flag++;
	  }
  }
  if(flag==37)
    printf("right!");
  else
    printf("try again~");
  return 0;
}