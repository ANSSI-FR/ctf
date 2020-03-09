#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <termios.h>

#define BUF_SIZE 100

static const char *password = "b87de397e1346bc605be4ed8361a68a3d9748fc9";
static char flag[BUF_SIZE] = { 0 };

/* Solution: 346bc605be4ed8361a68a3d9748fc9b87de397e1 */
/*
void print_solution()
{
    int i;
    for (i = 0; i < 40; i++)
    {
        putchar(password[(i + 10) % 40]);
    }
    putchar('\n');
}
*/

int check_char(unsigned int pos, unsigned char c)
{
   return password[(pos + 10) % 40] == c; 
}

int main(int argc, char *argv[])
{
    unsigned int pos = 0;
    unsigned char c;
    int b = 1;
    unsigned int sum = 0;

    /*
    print_solution();
    */

    struct termios tp, save;
    /* Retrieve current terminal settings, turn echoing off */
    if (tcgetattr(STDIN_FILENO, &tp) == -1)
    {
        fprintf(stderr, "tcgetattr");
        exit(-1);
    }
    save = tp;                          /* So we can restore settings later */
    tp.c_lflag &= ~ECHO;                /* ECHO off, other bits unchanged */
    if (tcsetattr(STDIN_FILENO, TCSAFLUSH, &tp) == -1)
    {
        fprintf(stderr, "tcsetattr");
        exit(-1);
    }

    printf("=-=-=-= Very secure vault =-=-=-=\n");
    printf("Please enter you very secure password: ");
    fflush(stdout);
    while ((c = getchar()) != EOF)
    {
        if (c == '\n')
        {
            putchar('\n');
            break;
        }
        b &= check_char(pos, c);
        if (b == 1)
        {
            sum += c;
            flag[pos % BUF_SIZE] = c;
        }
        pos += 1;
        /*
        printf("%u - sum: %u\n", b, sum);
        */
    }

    /* Restore original terminal settings */
    if (tcsetattr(STDIN_FILENO, TCSANOW, &save) == -1)
    {
        fprintf(stderr, "tcsetattr");
        exit(-1);
    }

    if (b != 1 || sum != 2827)
    {
        printf("Wrong password: authorities have been alerted!\n");
        exit(-1);
    }

    printf("\\o/ Access granted! \\o/\n");
    printf("Here is your flag: ECSC{%s}\n", flag);

    exit(EXIT_SUCCESS);
}
