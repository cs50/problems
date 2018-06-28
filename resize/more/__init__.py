less = __import__("check50").import_checks("../less")
from less import *

@check50.check(compiles)
def scale_6_to_3():
    """resizes 6x6-pixel BMP to 3x3 correctly when f is 0.5"""
    check50.include("6x6.bmp", "3x3.bmp")
    check50.run("./resize 0.5 6x6.bmp outfile.bmp").exit(0)
    check_bmps("3x3.bmp", "outfile.bmp")

@check50.check(compiles)
def scale_12_to_6():
    """resizes 12x12-pixel BMP to 6x6 correctly when f is 0.5"""
    check50.include("12x12.bmp", "6x6.bmp")
    check50.run("./resize 0.5 12x12.bmp outfile.bmp").exit(0)
    check_bmps("6x6.bmp", "outfile.bmp")

@check50.check(compiles)
def scale_18_to_9():
    """resizes 18x18-pixel BMP to 9x9 correctly when f is 0.5"""
    check50.include("18x18.bmp", "9x9.bmp")
    check50.run("./resize 0.5 18x18.bmp outfile.bmp").exit(0)
    check_bmps("9x9.bmp", "outfile.bmp")
