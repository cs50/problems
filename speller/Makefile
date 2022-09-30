CC = $(shell echo $$CC)
CFLAGS = $(shell echo $$CFLAGS)
LDLIBS = $(shell echo $$LDLIBS)

speller: dictionary.c dictionary.h speller.c Makefile
	$(CC) $(CFLAGS) -o speller speller.c dictionary.c $(LDLIBS)
