speller: dictionary.c dictionary.h speller.c Makefile
	$CC $CLFAGS -c -o speller.o speller.c
	$CC $CLFAGS -c -o dictionary.o dictionary.c
	$CC $CLFAGS -o speller speller.o dictionary.o $LDLIBS
