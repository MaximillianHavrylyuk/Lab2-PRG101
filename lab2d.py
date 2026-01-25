#Author:Maximillian Havrylyuk
#Lab2d.py
#pycharm printing command line arguements and importing the sys module

#importing the sys module
import sys

print(sys.version) # prints the version of the python currently in use.
print(sys.platform) # prints the name of operating system.
print(sys.argv) # prints the list of all arguments given at the command line when running our python script from terminal.
print(len(sys.argv)) # tells us the number of command line arguments the user provides from terminal.

print(sys.argv[0]) # prints the first argument, it is always the name of script.
print(sys.argv[1]) # prints the second argument .
print(sys.argv[2]) # prints the third argument.
print(len(sys.argv)) # tells us the number of command line arguments the user provides from terminal.
