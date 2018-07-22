import check50
import check50.c

from ctypes import Structure, c_uint16, c_uint32, c_int32
from itertools import zip_longest

class BitmapHeader(Structure):
    """Structure to maintain BITMAPFILEHEADER and BITMAPINFOHEADER"""
    _pack_ = 1
    _fields_ = [('bfType', c_uint16),
                ('bfSize', c_uint32),
                ('bfReserved1', c_uint16),
                ('bfReserved2', c_uint16),
                ('bfOffBits', c_uint32),
                ('biSize', c_uint32),
                ('biWidth', c_int32),
                ('biHeight', c_int32),
                ('biPlanes', c_uint16),
                ('biBitCount', c_uint16),
                ('biCompression', c_uint32),
                ('biSizeImage', c_uint32),
                ('biXPelsPerMeter', c_int32),
                ('biYPelsPerMeter', c_int32),
                ('biClrUsed', c_uint32),
                ('biClrImportant', c_uint32)]

    def __iter__(self):
        for field, _ in self._fields_:
            yield field, getattr(self, field)

    @classmethod
    def from_file(cls, file):
        header = cls()
        file.readinto(header)
        return header


def check_bmps(expected_filename, actual_filename):

    # Open files.
    with open(expected_filename, "rb") as expected_file, \
            open(actual_filename, "rb") as actual_file:

        # Read in the headers.
        expected_header = BitmapHeader.from_file(expected_file)
        actual_header = BitmapHeader.from_file(actual_file)

        expected_bytes = expected_file.read()
        actual_bytes = actual_file.read()


    check50.log(f"checking {actual_filename} header...")
    for (field, expected_field), (_, actual_field) in zip(expected_header, actual_header):
        if expected_field != actual_field:
            raise check50.Failure(f"expected {hex(expected_field)}, not {hex(actual_field)} in header field {field}")

    check50.log(f"checking {actual_filename} pixel data...")
    for i, (expected_byte, actual_byte) in enumerate(zip_longest(expected_bytes, actual_bytes), 1):
        if actual_byte is None:
            raise check50.Failure("image has fewer bytes than expected.")
        elif expected_byte is None:
            raise check50.Failure("image has more bytes than expected.")
        elif expected_byte != actual_byte:
            raise check50.Failure(f"expected {hex(expected_byte)}, not {hex(actual_byte)} in byte {i} of pixel data")


@check50.check()
def exists():
    """resize.c and bmp.h exist."""
    check50.include("bmp.h")
    check50.include("small.bmp", "smiley.bmp", "large.bmp")
    check50.include("small2.bmp", "small3.bmp", "small4.bmp", "small5.bmp")
    check50.include("large2.bmp", "smiley2.bmp", "smiley3.bmp")
    check50.exists("resize.c")

@check50.check(exists)
def compiles():
    """resize.c compiles."""
    check50.c.compile("resize.c", lcs50=True)

@check50.check(compiles)
def small_1():
    """doesn't resize small.bmp when n is 1"""
    check50.run("./resize 1 small.bmp outfile.bmp").exit(0)
    check_bmps("small.bmp", "outfile.bmp")

@check50.check(compiles)
def small_2():
    """resizes small.bmp correctly when n is 2"""
    check50.run("./resize 2 small.bmp outfile.bmp").exit(0)
    check_bmps("small2.bmp", "outfile.bmp")

@check50.check(compiles)
def small_3():
    """resizes small.bmp correctly when n is 3"""
    check50.run("./resize 3 small.bmp outfile.bmp").exit(0)
    check_bmps("small3.bmp", "outfile.bmp")

@check50.check(compiles)
def small_4():
    """resizes small.bmp correctly when n is 4"""
    check50.run("./resize 4 small.bmp outfile.bmp").exit(0)
    check_bmps("small4.bmp", "outfile.bmp")

@check50.check(compiles)
def small_5():
    """resizes small.bmp correctly when n is 5"""
    check50.run("./resize 5 small.bmp outfile.bmp").exit(0)
    check_bmps("small5.bmp", "outfile.bmp")

@check50.check(compiles)
def large_2():
    """resizes large.bmp correctly when n is 2"""
    check50.run("./resize 2 large.bmp outfile.bmp").exit(0)
    check_bmps("large2.bmp", "outfile.bmp")

@check50.check(compiles)
def smiley_2():
    """resizes smiley.bmp correctly when n is 2"""
    check50.run("./resize 2 smiley.bmp outfile.bmp").exit(0)
    check_bmps("smiley2.bmp", "outfile.bmp")

@check50.check(compiles)
def smiley_3():
    """resizes smiley.bmp correctly when n is 3"""
    check50.run("./resize 3 smiley.bmp outfile.bmp").exit(0)
    check_bmps("smiley3.bmp", "outfile.bmp")
