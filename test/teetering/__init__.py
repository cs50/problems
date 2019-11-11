import check50
import check50.py

test_cases = [
    [1, 1], # 0. True
    [1, 2], # 1. False
    [2, 2, 2, 2, 2], # 2. False
    [1, 1, 1, 1, 7, 1, 1, 1], # 3. True
    [3, 4, 5, 6, 8], # 4. True
    [5, 0, 2, 3, 4, 4, 0], # 5. True
    [8, 6, 5, 3, 2], # 6. False
    [9, 7, 6, 5, 4, 3], # 7. True
    [3, 2, 5, 4, 14], # 8. True
    [3, 2, 5, 4, 15], # 9. False
    [5, 5, 4, 8, 3, 8, 8], # 10. False
    [2, 8, 2, 3, 3, 5, 5], # 11. True
    [10, 9, 9, 9, 7, 8, 6], # 12. False
    [9, 7, 6, 5, 4, 10, 5], # 13. True
    [10, 9, 5, 5, 4, 8, 9], # 14. False
    [6, 4, 6, 8, 8, 6, 8], # 15. False
    [9, 8, 5, 4, 6, 9, 7], # 16. True
    [8, 9, 6, 6, 9, 8, 8], # 17. False
    [7, 7, 6, 7, 7, 10, 8], # 18. False
    [6, 4, 10, 4, 10, 6, 4], # 19. True
]

@check50.check()
def exists():
    """teetering.py exists and can be imported"""
    check50.exists("teetering.py")
    check50.py.import_("teetering.py")

@check50.check(exists)
def test0(exists):
    """balanceable identifies [1, 1] as balanceable"""
    check_output(0, True)

@check50.check(exists)
def test1(exists):
    """balanceable identifies [1, 2] as not balanceable"""
    check_output(1, False)

@check50.check(exists)
def test2(exists):
    """balanceable identifies [2, 2, 2, 2, 2] as not balanceable"""
    check_output(2, False)

@check50.check(exists)
def test3(exists):
    """balanceable identifies [1, 1, 1, 1, 7, 1, 1, 1] as balanceable"""
    check_output(3, True)

@check50.check(exists)
def test4(exists):
    """balanceable identifies [3, 4, 5, 6, 8] as balanceable"""
    check_output(4, True)

@check50.check(exists)
def test5(exists):
    """balanceable identifies [5, 0, 2, 3, 4, 4, 0] as balanceable"""
    check_output(5, True)

@check50.check(exists)
def test6(exists):
    """balanceable identifies [8, 6, 5, 3, 2] as not balanceable"""
    check_output(6, False)

@check50.check(exists)
def test7(exists):
    """balanceable identifies [9, 7, 6, 5, 4, 3] as balanceable"""
    check_output(7, True)

@check50.check(exists)
def test8(exists):
    """balanceable identifies [3, 2, 5, 4, 14] as balanceable"""
    check_output(8, True)

@check50.check(exists)
def test9(exists):
    """balanceable identifies [3, 2, 5, 4, 15] as not balanceable"""
    check_output(9, False)

@check50.check(exists)
def test10(exists):
    """balanceable identifies [5, 5, 4, 8, 3, 8, 8] as not balanceable"""
    check_output(10, False)

@check50.check(exists)
def test11(exists):
    """balanceable identifies [2, 8, 2, 3, 3, 5, 5] as balanceable"""
    check_output(11, True)

@check50.check(exists)
def test12(exists):
    """balanceable identifies [10, 9, 9, 9, 7, 8, 6] as not balanceable"""
    check_output(12, False)

@check50.check(exists)
def test13(exists):
    """balanceable identifies [9, 7, 6, 5, 4, 10, 5] as balanceable"""
    check_output(13, True)

@check50.check(exists)
def test14(exists):
    """balanceable identifies [10, 9, 5, 5, 4, 8, 9] as not balanceable"""
    check_output(14, False)

@check50.check(exists)
def test15(exists):
    """balanceable identifies [6, 4, 6, 8, 8, 6, 8] as not balanceable"""
    check_output(15, False)

@check50.check(exists)
def test16(exists):
    """balanceable identifies [9, 8, 5, 4, 6, 9, 7] as balanceable"""
    check_output(16, True)

@check50.check(exists)
def test17(exists):
    """balanceable identifies [8, 9, 6, 6, 9, 8, 8] as not balanceable"""
    check_output(17, False)

@check50.check(exists)
def test18(exists):
    """balanceable identifies [7, 7, 6, 7, 7, 10, 8] as not balanceable"""
    check_output(18, False)

@check50.check(exists)
def test19(exists):
    """balanceable identifies [6, 4, 10, 4, 10, 6, 4] as balanceable"""
    check_output(19, True)

def check_output(case, expected):
    try:
        teetering = check50.py.import_("teetering.py")
        actual = teetering.balanceable(test_cases[case])
    except Exception as e:
        raise check50.Failure("Exception thrown by function")
    if expected != actual:
        raise check50.Mismatch(str(expected), str(actual))
