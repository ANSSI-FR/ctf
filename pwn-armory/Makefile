all:
	arm-linux-gnueabi-gcc -Wall -Wextra armory.c -fno-stack-protector -no-pie -Wl,-z,relro,-z,now,-z,noexecstack -o armory 

clean:
	rm *.o *~ armory
