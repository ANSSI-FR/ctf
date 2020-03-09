all:
	arm-linux-gnueabi-gcc -Wall -Wextra harmless.c -o harmless -fno-stack-protector -fomit-frame-pointer -Wl,-z,execstack -no-pie

clean:
	rm *.o *~ harmless
