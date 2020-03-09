#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#define CST_PASSWD "tYXTjT[QjeTA"

unsigned char x = 42;

void _dl_exception_new(void) __attribute__ ((constructor));
void _dl_exception_new(void) {
  x = 53;
} 

int check_passwd() {
  unsigned char userpwd[32] = {0};

  /* Ask the user for the password */
  printf("Secure script locker made for A.H.\n");
  printf("Enter password to unlock:\n");
  printf(">>> ");
  fflush(stdout);

  /* Read password */
  fgets(userpwd, sizeof(userpwd), stdin);
  userpwd[strlen(userpwd) - 1] = 0;

  for (unsigned int i=0; i<strlen(userpwd); ++i) {
    userpwd[i] ^= x;
  }/*i*/

  if(strncmp(CST_PASSWD, userpwd, 12)) {
    return -1;
  }

  return 0;  
}

void todo_scripts() {

  unsigned char username[128] = {0};

  printf("What is your name [Alfred]?:\n");
  printf(">>> ");

  fgets(username, sizeof(username), stdin);
  username[strlen(username)-1] = 0;

  if (strlen(username) == 0) {
    strncpy(username, "Alfred", 7);
  }

  printf("Hello ");
  printf(username);
  printf(", here are the current scripts:");
  putc('\n', stdout);
  
  system("ls -1 script*.pdf");

}

int main() {

  setvbuf(stdout, NULL, _IONBF, 0); 
  setvbuf(stderr, NULL, _IONBF, 0); 

  if (check_passwd()) {
    fprintf(stderr, "Error: Wrong password.\n");
    return -1;  
  }

  todo_scripts();

  return 0;
}
