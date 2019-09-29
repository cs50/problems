import check50
import check50.c
import re

SAMPLE_IMAGES = [

    # 0
    ["testing with sample 3x3 image",
    "first row: (255, 0, 0), (255, 0, 0), (255, 0, 0)",
    "second row: (0, 255, 0), (0, 255, 0), (0, 0, 255)",
    "third row: (0, 0, 255), (0, 0, 255), (0, 0, 255)"],

    # 1
    ["testing with sample 3x3 image",
    "first row: (10, 20, 30), (40, 50, 60), (70, 80, 90)",
    "second row: (110, 130, 140), (120, 140, 150), (130, 150, 160)",
    "third row: (200, 210, 220), (220, 230, 240), (240, 250, 255)"],

    # 2
    ["testing with sample 4x4 image",
    "first row: (10, 20, 30), (40, 50, 60), (70, 80, 90), (110, 110, 120)",
    "second row: (110, 130, 140), (120, 140, 150), (130, 150, 160), (140, 160, 170)",
    "third row: (195, 204, 213), (205, 214, 223), (225, 234, 243), (245, 254, 253)",
    "fourth row: (50, 28, 90), (0, 0, 0), (255, 255, 255), (85, 85, 85)"],

    # 3
    ["testing with sample 1x2 image",
    "first row: (255, 0, 0), (0, 0, 255)"],

    # 4
    ["testing with sample 1x3 image",
    "first row: (255, 0, 0), (0, 255, 0), (0, 0, 255)"]
]

def SAMPLE_PIXEL(r, g, b):
    return f"testing with pixel ({r}, {g}, {b})"

def log(lines):
    if isinstance(lines, list):
        for line in lines:
            check50.log(line)
    else:
        check50.log(lines)

@check50.check()
def exists():
    """helpers.c exists"""
    check50.exists("helpers.c")
    check50.include("Makefile", "bmp.h", "helpers.h", "testing.c")

@check50.check(exists)
def compiles():
    """filter compiles"""
    check50.c.compile("testing.c", "helpers.c")

@check50.check(compiles)
def grayscale_single_pixel():
    """grayscale correctly filters single pixel with whole number average"""
    log(SAMPLE_PIXEL(20, 40, 90))
    check50.run("./testing 0 0").stdout("50 50 50\n");
    pass

@check50.check(compiles)
def grayscale_rounding():
    """grayscale correctly filters single pixel without whole number average"""
    log(SAMPLE_PIXEL(27, 28, 28))
    check50.run("./testing 0 1").stdout("28 28 28\n");
    pass

@check50.check(compiles)
def grayscale_gray():
    """grayscale leaves alone pixels that are already gray"""
    log(SAMPLE_PIXEL(50, 50, 50))
    check50.run("./testing 0 2").stdout("50 50 50\n");
    pass

@check50.check(compiles)
def grayscale_multi():
    """grayscale correctly filters simple 3x3 image"""
    log(SAMPLE_IMAGES[0])
    check50.run("./testing 0 3").stdout("85 85 85\n" * 9);

@check50.check(compiles)
def grayscale3x3():
    """grayscale correctly filters more complex 3x3 image"""
    log(SAMPLE_IMAGES[1])
    check50.run("./testing 0 4").stdout("".join([
        "20 20 20\n", "50 50 50\n", "80 80 80\n",
        "127 127 127\n", "137 137 137\n", "147 147 147\n",
        "210 210 210\n", "230 230 230\n", "248 248 248\n"
    ]))


@check50.check(compiles)
def grayscale4x4():
    """grayscale correctly filters 4x4 image"""
    log(SAMPLE_IMAGES[2])
    check50.run("./testing 0 5").stdout("".join([
        "20 20 20\n", "50 50 50\n", "80 80 80\n", "110 110 110\n",
        "127 127 127\n", "137 137 137\n", "147 147 147\n", "157 157 157\n",
        "204 204 204\n", "214 214 214\n", "234 234 234\n", "251 251 251\n",
        "56 56 56\n", "0 0 0\n", "255 255 255\n", "85 85 85\n"
    ]))

@check50.check(compiles)
def sepia_single_pixel():
    """sepia correctly filters single pixel"""
    log(SAMPLE_PIXEL(20, 40, 90))
    check50.run("./testing 1 0").stdout("56 50 39\n");
    pass

@check50.check(compiles)
def sepia_multi():
    """sepia correctly filters simple 3x3 image"""
    log(SAMPLE_IMAGES[0])
    check50.run("./testing 1 3").stdout("".join([
        "100 89 69\n", "100 89 69\n", "100 89 69\n",
        "196 175 136\n", "196 175 136\n", "196 175 136\n",
        "48 43 33\n", "48 43 33\n", "48 43 33\n"
    ]))

@check50.check(compiles)
def sepia3():
    """sepia correctly filters more complex 3x3 image"""
    log(SAMPLE_IMAGES[1])
    check50.run("./testing 1 4").stdout("".join([
        "25 22 17\n", "66 58 45\n", "106 94 74\n",
        "170 151 118\n", "183 163 127\n", "197 175 136\n",
        "255 251 195\n", "255 255 214\n", "255 255 232\n"
    ]))


@check50.check(compiles)
def sepia4():
    """sepia correctly filters 4x4 image"""
    log(SAMPLE_IMAGES[2])
    check50.run("./testing 1 5").stdout("".join([
        "25 22 17\n", "66 58 45\n", "106 94 74\n", "147 131 102\n",
        "170 151 118\n", "183 163 127\n", "197 175 136\n", "210 187 146\n",
        "255 244 190\n", "255 255 199\n", "255 255 218\n", "255 255 235\n",
        "58 52 40\n", "0 0 0\n", "255 255 239\n", "115 102 80\n"
    ]))

@check50.check(compiles)
def reflect_row2():
    """reflect correctly filters 1x2 image"""
    log(SAMPLE_IMAGES[3])
    check50.run("./testing 2 0").stdout("".join([
        "0 0 255\n", "255 0 0\n"
    ]))

@check50.check(compiles)
def reflect_row3():
    """reflect correctly filters 1x3 image"""
    log(SAMPLE_IMAGES[4])
    check50.run("./testing 2 1").stdout("".join([
        "0 0 255\n", "0 255 0\n", "255 0 0\n"
    ]))

@check50.check(compiles)
def reflect_simple():
    """reflect correctly filters image that is its own mirror image"""
    log(SAMPLE_IMAGES[0])
    check50.run("./testing 2 2").stdout("".join([
        "255 0 0\n", "255 0 0\n", "255 0 0\n",
        "0 255 0\n", "0 255 0\n", "0 255 0\n",
        "0 0 255\n", "0 0 255\n", "0 0 255\n"
    ]))

@check50.check(compiles)
def reflect3():
    """reflect correctly filters 3x3 image"""
    log(SAMPLE_IMAGES[1])
    check50.run("./testing 2 3").stdout("".join([
        "70 80 90\n", "40 50 60\n", "10 20 30\n",
        "130 150 160\n", "120 140 150\n", "110 130 140\n",
        "240 250 255\n", "220 230 240\n", "200 210 220\n"
    ]))

@check50.check(compiles)
def reflect4():
    """reflect correctly filters 4x4 image"""
    log(SAMPLE_IMAGES[2])
    check50.run("./testing 2 4").stdout("".join([
        "100 110 120\n", "70 80 90\n", "40 50 60\n", "10 20 30\n",
        "140 160 170\n", "130 150 160\n", "120 140 150\n", "110 130 140\n",
        "245 254 253\n", "225 234 243\n", "205 214 223\n", "195 204 213\n",
        "85 85 85\n", "255 255 255\n", "0 0 0\n", "50 28 90\n"
    ]))

@check50.check(compiles)
def blur_middle():
    """blur correctly filters middle pixel"""
    log(SAMPLE_IMAGES[1])
    check50.run("./testing 3 0").stdout("127 140 149\n")

@check50.check(compiles)
def blur_edge():
    """blur correctly filters pixel on edge"""
    log(SAMPLE_IMAGES[1])
    check50.run("./testing 3 1").stdout("80 95 105\n")

@check50.check(compiles)
def blur_corner():
    """blur correctly filters pixel in corner"""
    log(SAMPLE_IMAGES[1])
    check50.run("./testing 3 2").stdout("70 85 95\n")

@check50.check(compiles)
def blur3():
    """blur correctly filters 3x3 image"""
    log(SAMPLE_IMAGES[1])
    check50.run("./testing 3 3").stdout("".join([
        "70 85 95\n", "80 95 105\n", "90 105 115\n",
        "117 130 140\n", "127 140 149\n", "137 150 159\n",
        "163 178 188\n", "170 185 194\n", "178 193 201\n"
    ]))

@check50.check(compiles)
def blur4():
    """blur correctly filters 4x4 image"""
    log(SAMPLE_IMAGES[2])
    check50.run("./testing 3 4").stdout("".join([
        "70 85 95\n", "80 95 105\n", "100 115 125\n", "110 125 135\n",
        "113 126 136\n", "123 136 145\n", "142 155 163\n", "152 165 173\n",
        "113 119 136\n", "143 151 164\n", "156 166 171\n", "180 190 194\n",
        "113 112 132\n", "155 156 171\n", "169 174 177\n", "203 207 209\n"
    ]))

