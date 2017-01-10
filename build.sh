#!/bin/bash
echo "- Starting to build Shellcode: system-execve-shell "
gcc-6 -c shellcode/system-execve-shell.c -o shellcode/system-execve-shell.o --shared -fpic -static -O0 -fno-asynchronous-unwind-tables -D LIB
echo "- Starting to link Shellcode: system-execve-shell "
ld shellcode/system-execve-shell.o -o shellcode/system-execve-shell -S -static -dylib -order_file shellcode/system-execve-order-file.txt
echo "- Starting to export Shellcode: system-execve-shell "
gobjcopy -O binary --only-section=.text shellcode/system-execve-shell shellcode/system-execve-shell.sc

echo "- Clean Up from build"
rm -f shellcode/system-execve-shell.o
rm -f shellcode/system-execve-shell
