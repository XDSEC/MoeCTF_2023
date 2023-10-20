//gcc format_level2.c -o format_level2 -g -m32 -no-pie -z now
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>

struct character{
	int HP;
	int ATK;
};

struct character pwner;
struct character dragon;

void init()
{
    	setvbuf(stdin,0,_IONBF,0);
    	setvbuf(stdout,0,_IONBF,0);
    	setvbuf(stderr,0,_IONBF,0);
}

void success()
{
	system("cat flag");
	exit(0);
}

void introduction()
{
	puts("Welcome!");
	puts("There's a dragon here.");
	puts("If you can defeat it, the flag will appear.");
}

void init_person_and_dragon()
{
	pwner.HP = 100;
	pwner.ATK = 1;
	dragon.HP = 10000000;
	dragon.ATK = 100000;
}

void menu()
{
	puts("What would you like to do?");
	puts("1. Attack the dragon");
	puts("2. ChenDian");
	puts("3. Talk with dragon");
	puts("4. Give up");
	puts("Your choice: ");
}

void attack()
{
	puts("You rushed into the dragon's lair.");
	sleep(1);
	puts("You pick up your sword and slash at the dragon.");
	sleep(1);
	dragon.HP = dragon.HP - pwner.ATK;
	puts("You attacked the dragon.");
	printf("Now the dragon's HP is %d.\n", dragon.HP);

	if(dragon.HP < 1)
        {
                puts("You succeed.");
        }

	sleep(1);
	puts("Then the dragon attack you.");
	pwner.HP = pwner.HP - dragon.ATK;
	printf("Now your HP is %d.\n", pwner.HP);
	sleep(1);

	if(pwner.HP < 1)
	{
		puts("You died.");
		exit(0);
	}
}

void chendian()
{
	puts("You practiced for 2.5 years.");
	pwner.HP += 10;
	pwner.ATK += 1;
	printf("Now your HP is %d, your ATK is %d.\n\n", pwner.HP, pwner.ATK);
}

void talk()
{
	char str[0x10];
	memset(str, 0, 0x10);

	puts("Input what you want to talk: ");
	read(0, str, 0x10);
	
	puts("You said: ");
	printf(str);

	puts("But the dragon seems to ignore you.\n");
}

void game()
{
	int choice;
	introduction();
	init_person_and_dragon();
	
	while(1)
	{
		menu();
		choice = 0;
		scanf("%d", &choice);
		switch(choice)
		{
			case 1:
				attack();
				break;
			case 2:
				chendian();
				break;
			case 3:
				talk();
				break;
			default:
				puts("Goodbye.");
				return;
		}
	}
}

int main()
{
	init();	
	game();
	return 0;
}
