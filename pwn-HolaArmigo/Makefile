all:
	arm-linux-gnueabi-gcc  -Wall -Wextra armigo.c -o armigo -fno-stack-protector -static -Wl,-z,relro,-z,now,-z,noexecstack

clean:
	rm *.o *~ armigo

