#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define PASSWORD "eCfSDFwEeAYDr" // SuPerpAsSworD

size_t len;
unsigned int i;

int main() {
  char password[32];
  int security = 0x45435343;
  
  printf("Please enter your password:\n");
  fflush(NULL);
  fgets(password, 40, stdin);

  len = strlen(PASSWORD);
  for (i=0; i<len; ++i) password[i] ^= 0x36;
  
  if(!strncmp(password, PASSWORD, len)) {
    
    printf("Welcome back!\n");
    fflush(NULL);
    
    if (security != 0x45435343) {
      printf("Entering debug mode\n");
      fflush(NULL);
      system("/bin/dash");
    }
    
  } else {
    printf("Sorry, that's not the correct password.\n");
    printf("Bye.\n");
    fflush(NULL);
  }
  
  return 0;
}
