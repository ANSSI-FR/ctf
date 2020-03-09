#include <stdio.h>
#include <stdlib.h>

/* This function will never be called ;( */
void forever_alone()
{
    const char *flag = "ECSC{cdcd13c4c81a23a21506fa8efa5edff781e9fe80}";

    printf("The flag is %s.\n", flag);
}

int main(int argc, char *argv[])
{
    printf("Nope, I won't give you the flag *that* easily!\n");

    exit(EXIT_SUCCESS);
}
