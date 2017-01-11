import ctypes
import threading
import sys
import os
import errno




def execute():
	'''
	threaded function for execution in seprate thread context. 
	TODO: test memeory for memeory leaks with Py_Initialize()
	'''
	OSX_PY_DYLIB27 = '/usr/lib/libpython2.7.dylib'
	OSX_PY_DYLIB26 = '/usr/lib/libpython2.6.dylib'
	PROGRAM_NAME = 'load-test'
	SIMPLE_STRING = "print 'Hi from the python matrix!'\n"
	PY_HOME = '/usr/lib/python2.6/'

	print "-------------------------------------------"
	libpy27 = ctypes.CDLL(OSX_PY_DYLIB27, use_errno=True)
	if not libpy27:
		print "Error loading C libary: %s" % errno.errorcode[ctypes.get_errno()]
	print "* C runtime libary loaded: %s" % OSX_PY_DYLIB27
	print "* C runtime handle at: %s" % libpy27

	libpy26 = ctypes.CDLL(OSX_PY_DYLIB26, use_errno=True)
	if not libpy26:
		print "Error loading C libary: %s" % errno.errorcode[ctypes.get_errno()]
	print "* C runtime libary loaded: %s" % OSX_PY_DYLIB26
	print "* C runtime handle at: %s" % libpy26


	if (libpy26.Py_SetProgramName(PROGRAM_NAME) == 0):
		print "* Python program name set to: %s" % PROGRAM_NAME
	if (libpy26.Py_SetPythonHome(PY_HOME) == 0):
		print "* Python home set to: %s" % PY_HOME

	libpy26.Py_Initialize()
	if (libpy26.Py_IsInitialized() == 0):
		print "* Python interpreter failed to initialize.."
		exit()
	else:
		print "* Python interpreter successfully initialized!"

	print "* attempting to run python simple string"
	print "-------------------------------------------"
	libpy26.PyRun_SimpleString(SIMPLE_STRING)

	print "-------------------------------------------"
	print "* Python interpreter being finalized"
	libpy26.Py_Finalize()
	exit()


if __name__ == "__main__":
	print "-------------------------------------------"
	print "* Spawning Py thread for thread context"
	t = threading.Thread(target=execute,)
	print "* Thread object starting %s" % t
	t.start()
