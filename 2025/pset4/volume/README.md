# Volume

Write a program to modify the volume of an audio file.

```
$ ./volume input.wav output.wav 2.0
```

## WAV Files

[WAV files](https://docs.fileformat.com/audio/wav/) are a common file format for representing audio. WAV files store audio as a sequence of "samples": numbers that represent the value of some audio signal at a particular point in time. WAV files begin with a 44-byte "header" that contains information about the file itself, including the size of the file, the number of samples per second, and the size of each sample. After the header, the WAV file contains a sequence of samples, each a single numerical value representing the audio signal at a particular point in time.

Scaling each sample value by a given factor has the effect of changing the volume of the audio. Multiplying each sample value by 2.0, for example, will have the effect of doubling the volume of the origin audio. Multiplying each sample by 0.5, meanwhile, will have the effect of cutting the volume in half.

## Implementation Details

Complete the implementation of `volume.c` at right, such that it changes the volume of a sound file by a given factor.

* The program accepts three command-line arguments: `input` stores the name of an audio file, `output` stores the name of the new audio file that should be generated, and `factor` is the amount by which the volume of the original audio file should be scaled.
    * For example, if `factor` is `2.0`, then your program should double the volume of the audio file in `input` and save the newly generated audio file in `output`.
* Your program should first read the header from the input file and write the header to the output file. Recall that this header is always exactly 44 bytes long.
* Your program should then read the rest of the data from the WAV file, one 16-bit (2-byte) sample at a time. Your program should multiply each sample by the `factor` and write the new sample to the output file.
    * You may assume that the WAV file will use 16-bit signed values as samples. In practice, WAV files can have varying numbers of bits per sample, but we'll assume 16-bit samples for simplicity here.
* Your program, if it uses `malloc`, must not leak any memory.

### Hints

* Note that this file includes the header file `stdint.h`, which includes the types `uint8_t` (for storing an 8-bit unsigned integer) and `int16_t` (for storing a 16-bit signed integer). Both may prove helpful to you! For instance, to store a 16-bit sample value, you might use a variable of type `int16_t`.
* You may find the documentation for [`fread`](https://man.cs50.io/3/fread) and [`fwrite`](https://man.cs50.io/3/fwrite) helpful here.
    * In particular, note that both functions accept the following arguments:
        * `ptr`: a pointer to the location in memory to store data (when reading from a file) or from which to write data (when writing data to a file)
        * `size`: the number of bytes in an item of data
        * `nmemb`: the number of bytes of data to read or write
        * `stream`: the file pointer to be read from or written to
    * Per its documentation, `fread` will return the number of items of data successfully read. You may find this useful to check for when you've reached the end of the file!

### How to Test Your Code

Your program should behave per the examples below.

```
$ ./volume input.wav output.wav 2.0
```

When you listen to `output.wav`, it should be twice as loud as `input.wav`!


```
$ ./volume input.wav output.wav 0.5
```

When you listen to `output.wav`, it should be half as loud as `input.wav`!

{% next %}

## How to Submit

TODO
