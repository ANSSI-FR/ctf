CC = gcc
CFLAGS = -m32 -Wall -Wextra -Wno-pointer-sign -Wno-format-security -no-pie -fstack-protector -O3

all: alfred

alfred: alfred.c
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm *.o *~ alfred
