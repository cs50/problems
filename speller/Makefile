CC = $(shell echo $$CC)
CFLAGS = $(shell echo $$CFLAGS)
LDLIBS = $(shell echo $$LDLIBS)

speller: dictionary.c dictionary.h speller.c Makefile
	$(CC) $(CFLAGS) -c -o speller.o speller.c
	$(CC) $(CFLAGS) -c -o dictionary.o dictionary.c
	$(CC) $(CFLAGS) -o speller speller.o dictionary.o $(LDLIBS)
