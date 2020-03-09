#include <time.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

int logtime() {
    time_t now;
    char s[32];
    struct tm tim;

    now = time(NULL);
    tim = *(localtime(&now));
    strftime(s, 32, "%Y-%m-%d %H:%M:%S", &tim);
    // 1985-04-18 02:25:00

    FILE * fp = fopen("/tmp/log.txt", "a+");

    if (!fp) {
      puts("Error: cannot open /tmp/log.txt!");
      fflush(NULL);
      exit(1);
    }
    
    dup2(0, 0);
    fprintf(fp, "%s\n", s);
    fclose(fp);
    return 0;
}

int check(int argc, char **argv) {
    char buf[50];
    logtime();
    read(STDIN_FILENO, buf, 256);
    return strncmp(buf, "ChAnG3_My_D3f4u1t_Pa$$w0rD", 26);
}

int main(int argc, char **argv) {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
    puts("Welcome. Please enter your password:");
    fflush(NULL);
    if(check(argc, argv)) {
        puts("Wrong password. Bye.");
	fflush(NULL);
    } else {
        puts("Welcome back!");
	fflush(NULL);
        // Do something
    }
    return 0;
}
