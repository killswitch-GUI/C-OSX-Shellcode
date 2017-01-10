import ctypes
import sys
import os
import errno

# mmap/mprotect header defs
PROT_READ = 0x01
PROT_WRITE = 0x02
MAP_ANON = 0x1000
MAP_PRIVATE = 0x0002
PROT_EXEC = 0x04

# static vars
NULL = 0
OSX_LIBC_DYLIB = '/usr/lib/libSystem.B.dylib'

if (len(sys.argv) != 2) :
	print "\nExample: python loader.py shellcode_file.sc\n"
	exit()

def deref(addr, typ):
    return ctypes.cast(addr, ctypes.POINTER(typ)).contents

print "-------------------------------------------"
libc = ctypes.CDLL(OSX_LIBC_DYLIB, use_errno=True)
libc.restype = ctypes.c_void_p
if not libc:
	print "Error loading C libary: %s" % errno.errorcode[ctypes.get_errno()]
print "* C runtime libary loaded: %s" % OSX_LIBC_DYLIB

page_size = libc.getpagesize()
print "* Current page size: %s" % page_size

# set return type to pointer object
mmap = libc.mmap
mmap.restype = ctypes.POINTER(ctypes.c_int)
shellcode_buf_pointer = libc.mmap(NULL, page_size, PROT_READ | PROT_WRITE, MAP_ANON | MAP_PRIVATE, -1, 0);
print "* Shellcode buffer pointer: %s" % shellcode_buf_pointer
if (shellcode_buf_pointer == -1):
	print "Error building shellcode buffer: %s" % errno.errorcode[ctypes.get_errno()]

file_size = os.path.getsize(sys.argv[1])
print "* Shellcode file size: %s" % file_size

# set return type to pointer object
fopen = libc.fopen
fopen.restype = ctypes.POINTER(ctypes.c_int)
print "* Shellcode file pointer: %s" % shellcode_buf_pointer
file_handle = libc.fopen(sys.argv[1], "r");
return_val = libc.fread(shellcode_buf_pointer, file_size, 1, file_handle)
if return_val != 1:
	print "Error moving shellcode file into buffer: %s" % errno.errorcode[ctypes.get_errno()]

print "-------------------------------------------"
if (libc.mprotect(shellcode_buf_pointer, page_size, PROT_READ | PROT_EXEC) != 0):
	print "Error RX buffer: %s" % errno.errorcode[ctypes.get_errno()]
print "- Shellcode buffer now RX memory"
print "- Casting pointer to: %s " % shellcode_buf_pointer
print "- Executing shellcode"
# ((void (*)())shellcode_buf_pointer)();
try:
	shell = ctypes.cast(shellcode_buf_pointer, ctypes.CFUNCTYPE(ctypes.c_void_p))
	shell()
except:
	print "Shellcode done...."

#libc.fclose(sys.argv[1])





