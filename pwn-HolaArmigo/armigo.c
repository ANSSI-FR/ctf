#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

const char *shell = "cat flag";

void debug(char *cmd){
    system(cmd);
}

int main() {
    char buffer[64];
    setbuf(stdout, NULL);
    debug("echo \"Hello, what's your name?\"");
    scanf("%s", buffer);
    printf("Hello %s!\n", buffer);
    return 0;
}
