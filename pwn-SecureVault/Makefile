CC = arm-linux-gnueabi-gcc
CFLAGS = -Os -Wall -Wextra -fno-stack-protector -no-pie

all:
	$(CC) $(CFLAGS) SecureVault.s -o SecureVault

clean:
	rm *.o *~ SecureVault
