#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - runs the while loop indefinitely
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 * Return: Always 0.
 */

int main(void)
{
	pid_t pid;
	int count = 0;

	while (count < 5)
	{
		pid = fork();

		if (pid == 0)
			exit(0);
		printf("Zombie process created, PID: %d\n", pid);
		count++;
	}
	infinite_while();

	return (0);
}
