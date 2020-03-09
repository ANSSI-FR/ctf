#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main () {
  char username[32];
  char age[4];
  char dev[4];
  char comment[128];

  printf("Hello, and welcome to ECSC!\n");
  printf("My name is Michel.\n");

  printf("What's your name?\n");
  printf(">> ");fflush(stdout);
  gets(username);

  printf("Nice to meet you %s. How old are you?\n", username);
  printf(">> ");fflush(stdout);
  gets(age);

  printf("Are you a developper? [Y/N]\n");
  printf(">> ");fflush(stdout);
  gets(dev);

  if (strncmp(dev, "Y", 1) == 0) {
    printf("This might be useful for you:\n");
    printf("\tusername: %p\n", &username);
    printf("\t     age: %p\n", &age);
    printf("\t     dev: %p\n", &dev);
    printf("\t comment: %p\n", &comment);
  } else {
    printf("Goodbye then!\n");
    return 0;
  }

  printf("Feel free to drop us a short comment about this CTF.\n");
  printf(">> ");fflush(stdout);
  gets(comment);

  printf("Thanks for your feedback!\n");
  printf("Bye.\n");
  
  return 0;
}
