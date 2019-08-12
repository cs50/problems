import functools
import itertools
import os
import sys

import check50
import check50.c
import check50.internal
from cffi import FFI


@check50.check()
def exists():
    """fifteen.c exists"""
    check50.exists("fifteen.c")


@check50.check(exists)
def compiles():
    """fifteen.c compiles"""
    check50.c.compile("fifteen.c", lcs50=True)
    ffibuilder = FFI()
    header = f"""
    void init(void);
    extern int board[9][9];
    extern int d;
    _Bool move(int tile);
    """

    ffibuilder.cdef(header)
    ffibuilder.set_source("_fifteen_ffi", header, sources=["fifteen.c"], libraries=["cs50"])
    return ffibuilder.compile()


@check50.check(compiles)
def init4(path):
    """4x4 board: init initializes board correctly"""
    lib = get_lib(path, init=4)
    expected = [[15, 14, 13, 12], [11, 10, 9, 8], [7, 6, 5, 4],[3, 1, 2, 0]]
    check_board(expected, lib.board)
    return path

@check50.check(compiles)
def init3(path):
    """3x3 board: init initializes board correctly"""
    lib = get_lib(path, init=3)
    expected = [[8,7,6],[5,4,3],[2,1,0]]
    check_board(expected, lib.board)
    return path


@check50.check(init3)
def invalid8(path):
    """3x3 board: catches moving 8 as an illegal move"""
    lib = get_lib(path, init=3)
    check50.log("Attempting to move tile 8...")
    if lib.move(8):
        raise check50.Failure("Expected move to return false, but it returned true")
    expected = [[8,7,6],[5,4,3],[2,1,0]]
    check_board(expected, lib.board)

@check50.check(init3)
def valid1(path):
    """3x3 board: catches moving 1 as a legal move"""
    lib = get_lib(path, init=3)
    check50.log("Attempting to move tile 1...")
    if not lib.move(1):
        raise check50.Failure("Expected move to return true, but it returned false")
    expected = [[8,7,6],[5,4,3],[2,0,1]]
    check_board(expected, lib.board)

@check50.check(init3)
def move_up2(path):
    """3x3 board: move blank up twice"""
    lib = get_lib(path, init=3)
    check50.log("Attempting to move the blank tile up...")
    if not lib.move(3):
        raise check50.Failure("Expected move to return true, but it returned false")
    expected = [[8,7,6],[5,4,0],[2,1,3]]
    check_board(expected, lib.board)
    check50.log("Attempting to move the blank tile up again...")
    if not lib.move(6):
        raise check50.Failure("Expected move to return true, but it returned false")
    expected = [[8,7,0],[5,4,6],[2,1,3]]
    check_board(expected, lib.board)

@check50.check(init3)
def move_left2(path):
    """3x3 board: move blank left twice"""
    lib = get_lib(path, init=3)
    check50.log("Attempting to move the blank tile left...")
    if not lib.move(1):
        raise check50.Failure("Expected move to return true, but it returned false")
    expected = [[8,7,6],[5,4,3],[2,0,1]]
    check_board(expected, lib.board)
    check50.log("Attempting to move the blank tile left again...")
    if not lib.move(2):
        raise check50.Failure("Expected move to return true, but it returned false")
    expected = [[8,7,6],[5,4,3],[0,2,1]]
    check_board(expected, lib.board)

@check50.check(init3)
def move_left_right(path):
    """3x3 board: move blank left then right"""
    lib = get_lib(path, init=3)
    check50.log("Attempting to move the blank tile left...")
    if not lib.move(1):
        raise check50.Failure("Expected move to return true, but it returned false")
    expected = [[8,7,6],[5,4,3],[2,0,1]]
    check_board(expected, lib.board)
    check50.log("Attempting to move the blank tile right...")
    if not lib.move(1):
        raise check50.Failure("Expected move to return true, but it returned false")
    expected = [[8,7,6],[5,4,3],[2,1,0]]
    check_board(expected, lib.board)

@check50.check(init3)
def move_up_down(path):
    """3x3 board: move blank up then down"""
    lib = get_lib(path, init=3)
    check50.log("Attempting to move the blank tile up...")
    if not lib.move(3):
        raise check50.Failure("Expected move to return true, but it returned false")
    expected = [[8,7,6],[5,4,0],[2,1,3]]
    check_board(expected, lib.board)
    check50.log("Attempting to move the blank tile down...")
    if not lib.move(3):
        raise check50.Failure("Expected move to return true, but it returned false")
    expected = [[8,7,6],[5,4,3],[2,1,0]]
    check_board(expected, lib.board)

@check50.check(init3)
def move_around(path):
    """3x3 board: move up-up-left-down-down-left-up-up-right-down-down-right"""
    lib = get_lib(path, init=3)
    moves = [3, 6, 7, 4, 1, 2, 5, 8, 4, 1, 2, 3]
    moves_ = ["up", "up", "left", "down", "down", "left", "up", "up", "right", "down", "down", "right"]
    for move, move_ in zip(moves, moves_):
        check50.log(f"Attempting to move the blank tile {move_}...")
        if not lib.move(move):
            raise check50.Failure("Expected move to return true, but it returned false")
    expected = [[4,1,7],[8,2,6],[5,3,0]]
    check_board(expected, lib.board)

@check50.check(init3)
def invalid_start(path):
    """3x3 board: make sure none of 2, 4, 5, 6, 7, 8 move tile"""
    lib = get_lib(path, init=3)
    moves = [2, 4, 5, 6, 7, 8]
    for move in moves:
        check50.log(f"Attempting to move tile {move}...")
        if lib.move(move):
            raise check50.Failure("Expected move to return false, but it returned true")
    expected = [[8,7,6],[5,4,3],[2,1,0]]
    check_board(expected, lib.board)

@check50.check(init3)
def invalid_center(path):
    """3x3 board: move blank left (tile 1) then up (tile 4), then try to move tiles 1, 2, 6, 8"""
    lib = get_lib(path, init=3)
    check50.log(f"Attempting to move blank left...")
    if not lib.move(1):
        raise check50.Failure("Expected move to return true, but it returned false")
    check50.log(f"Attempting to move blank up...")
    if not lib.move(4):
        raise check50.Failure("Expected move to return true, but it returned false")
    moves = [1, 2, 6, 8]
    for move in moves:
        check50.log(f"Attempting to move tile {move}...")
        if lib.move(move):
            raise check50.Failure("Expected move to return false, but it returned true")
    expected = [[8,7,6],[5,0,3],[2,4,1]]
    check_board(expected, lib.board)

@check50.check(init3)
def win_3x3(path):
    """3x3 board: make sure game is winnable"""
    lib = get_lib(path, init=3)
    moves = [
        3, 4, 1, 2, 5, 8, 7, 6, 4, 1, 2, 5, 8,
        7, 6, 4, 1, 2, 4, 1, 2, 3, 5, 4, 7, 6,
        1, 2, 3, 7, 4, 8, 6, 4, 8, 5, 7, 8, 5,
        6, 4, 5, 6, 7, 8, 6, 5, 4, 7, 8
    ]
    for move in moves:
        check50.log(f"Attempting to move tile {move}...")
        if not lib.move(move):
            raise check50.Failure("Expected move to return true, but it returned false")
    expected = [[1,2,3],[4,5,6],[7,8,0]]
    check_board(expected, lib.board)

@check50.check(init4)
def win_4x4(path):
    """4x4 board: make sure game is winnable"""
    lib = get_lib(path, init=4)
    moves = [
        4, 5, 6, 1, 2, 4, 5, 6, 1, 2,
        3, 7, 11, 10, 9, 1, 2, 3, 4, 5,
        6, 8, 1, 2, 3, 4, 7, 11, 10, 9,
        14, 13, 12, 1, 2, 3, 4, 14, 13,
        12, 1, 2, 3, 4, 14, 13, 12, 1,
        2, 3, 4, 12, 9, 15, 1, 2, 3, 4,
        12, 9, 13, 14, 9, 13, 14, 7, 5, 9,
        13, 14, 15, 10, 11, 5, 9, 13, 7, 11,
        5, 9, 13, 7, 11, 15, 10, 5, 9, 13, 15,
        11, 8, 6, 7, 8, 14, 12, 6, 7, 8, 14,
        12, 6, 7, 8, 14, 15, 11, 10, 6, 7, 8,
        12, 15, 11, 10, 15, 11, 14, 12, 11, 15,
        10, 14, 15, 11, 12
    ]
    for move in moves:
        check50.log(f"Attempting to move tile {move}...")
        if not lib.move(move):
            raise check50.Failure("Expected move to return true, but it returned false")
    expected = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
    check_board(expected, lib.board)


def check_board(expected, actual):
    n = len(expected)
    for i, j in itertools.product(range(n), range(n)):
        if expected[i][j] == 0:
            continue
        check50.log(f"Checking that {expected[i][j]} appears at index ({i}, {j})")
        if expected[i][j] != actual[i][j]:
            raise check50.Failure(f"Expected {expected[i][j]} at index ({i}, {j}) but found {actual[i][j]}")

def get_lib(path, init=None):
    lib = check50.internal.import_file("_fifteen_ffi", path).lib
    if init is not None:
        lib.d = init
        lib.init()
    return lib
