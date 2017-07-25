# Using C to build OSX Shellcode 

A small setup that I used to learn X86_x64 shellcode generation using ASM and compiled C code. 


## OSX Host Setup

Please ensure you have the following installed before starting to build.

- Install XCode: `xcode-select --install`
- Install Brew: `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
- Install Brew GCC: `brew install gcc`
- Link GCC 6: `ln -s /usr/local/Cellar/gcc/6.3.0_1/bin/gcc-6 gcc-6`


## Shellcode generation

In this project we have a few diffrent types of shell code that I have built as POC using C and ASM.

### System Execve /bin/sh
This code uses inline ASM in C for system call and executes a /bin/sh as an example. 

## Shellcode loader

in the /loader folder you will find 2 loader examples, the Python and C based loader. Basic shellcode loader and best part is its pure python using ctypes and std C lib.

### Python Example:
`python loader.py ../shellcode/system-execve-shell.sc`

```
MacBook-Pro:loader test$ python loader.py ../shellcode/system-execve-shell.sc 
-------------------------------------------
* C runtime libary loaded: /usr/lib/libSystem.B.dylib
* Current page size: 4096
* Shellcode buffer pointer: <__main__.LP_c_int object at 0x10f56b950>
* Shellcode file size: 122
* Shellcode file pointer: <__main__.LP_c_int object at 0x10f56b950>
-------------------------------------------
- Shellcode buffer now RX memory
- Casting pointer to: <__main__.LP_c_int object at 0x10f56b950> 
- Executing shellcode
bash-3.2$ exit
exit
```

#### Credit
Thanks for the great resource: https://github.com/tbarabosch/MacRE
