//gcc feedback.c -o feedback -g -z now
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>

char* feedback_list[4];

//初始化缓冲区
void init()
{
    	setvbuf(stdin,0,_IONBF,0);
    	setvbuf(stdout,0,_IONBF,0);
    	setvbuf(stderr,0,_IONBF,0);
}

//读取flag到libc
void read_flag()
{
	int fd = open("./flag", 0, 0);

	if(fd == -1)
	{
		puts("open flag error!");
		exit(0);
	}
	
	char* flag = &puts - 0x84420 + 0x1f1700;
	if(!flag)
	{
		puts("malloc error!");
		exit(0);
	}

	read(fd, flag, 0x50);
	close(fd);
}

//读取数字
int read_num()
{
	char str[0x10];
	read(0, str, 0xf);
	return atoi(str);
}

//读取字符串
void read_str(char* str)
{
	int i;
	char ch;
	char buf[0x48];
	for(i = 0; i < 0x48; i++)
	{
		ch = getchar();
		if(ch == '\n')
			break;
		buf[i] = ch;
	}
	memcpy(str, buf, i);
}

//打印出你的反馈信息
void print_feedback()
{
	puts("Your feedback is: ");
	for(int i = 1; i < 4; i++)
		printf("%d. %s\n", i, feedback_list[i]);
}

void vuln()
{
	int i, index;
	
	//打印提示信息
	puts("Can you give me your feedback?");
	puts("There are some questions.");
	puts("1. What do you think of the quality of the challenge this time?");
	puts("2. Give me some suggestions.");
	puts("3. Please give me your ID.");

	//初始化反馈列表
	feedback_list[0] = 0;
	for(i = 1; i < 4; i++)
		feedback_list[i] = malloc(0x50);

	//输入反馈内容
	for(i = 0; i < 3; i++)
	{
		puts("Which list do you want to write?");
		index = read_num();
		if(index > 3)
		{
			puts("No such list.");
			continue;
		}

		puts("Then you can input your feedback.");
		read_str(feedback_list[index]);
		print_feedback();
	}
	_exit(0);
}

int main()
{
	init();
	read_flag();
	vuln();
	return 0;	
}
