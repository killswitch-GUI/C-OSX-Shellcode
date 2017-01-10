default: system-execve-shell

system-execve-shell.o: shellcode/system-execve-shell.c 
	gcc-6 -c shellcode/system-execve-shell.c -o shellcode/system-execve-shell.o --shared -fpic -static -O0 -fno-asynchronous-unwind-tables -D LIB

system-execve-shell: shellcode/system-execve-shell.o
	ld shellcode/system-execve-shell.o -o shellcode/system-execve-shell -S -static -dylib -order_file shellcode/system-execve-order-file.txt

system-execve-shell: shellcode/system-execve-shell
	gobjcopy -O binary --only-section=.text shellcode/system-execve-shell shellcode/system-execve-shell.sc

clean:
	-rm -f shellcode/system-execve-shell.o
	-rm -f shellcode/system-execve-shell
