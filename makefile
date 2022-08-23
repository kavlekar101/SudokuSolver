all: library

# fPIC creates position independent code so it doesn't matter what the \
absolute address is, just the relative address \
for each program that is using this library
library: makefile
	g++ -dynamiclib -undefined suppress -flat_namespace brains.o -o libtrial.dylib

brains: brains.o
	gcc -g -o $@ $^

brains.o: brains.c
	gcc -g -c $<

%.o: %.c
	gcc -c $< -o $@