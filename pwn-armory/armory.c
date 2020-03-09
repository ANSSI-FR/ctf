#include <stdio.h>
#include <stdlib.h>

void evil() {
    system("/bin/dash");
}

int main() {
    char buffer[64];
    printf("Hello, what's your name?\n");
    fflush(NULL);
    scanf("%s", buffer);
    printf("Hello %s!\n", buffer);
    fflush(NULL);
    return 0;
}
