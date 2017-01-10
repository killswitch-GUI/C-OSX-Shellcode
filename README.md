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