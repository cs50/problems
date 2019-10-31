import check50

@check50.check()
def exists():
    """dna.py exists"""
    check50.exists("dna.py")
    check50.include("sequences", "databases")

@check50.check(exists)
def test1():
    """correctly identifies sequences/1.txt"""
    check50.run("python3 dna.py databases/small.csv sequences/1.txt").stdout("Bob\n").stdout(check50.EOF).exit(0)

@check50.check(exists)
def test2():
    """correctly identifies sequences/2.txt"""
    check50.run("python3 dna.py databases/small.csv sequences/2.txt").stdout("[Nn]o [Mm]atch\n", "No match\n").stdout(check50.EOF).exit(0)

@check50.check(exists)
def test3():
    """correctly identifies sequences/3.txt"""
    check50.run("python3 dna.py databases/small.csv sequences/3.txt").stdout("[Nn]o [Mm]atch\n", "No match\n").stdout(check50.EOF).exit(0)

@check50.check(exists)
def test4():
    """correctly identifies sequences/4.txt"""
    check50.run("python3 dna.py databases/small.csv sequences/4.txt").stdout("Alice\n").stdout(check50.EOF).exit(0)

@check50.check(exists)
def test5():
    """correctly identifies sequences/5.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/5.txt").stdout("Lavender\n").stdout(check50.EOF).exit(0)

@check50.check(exists)
def test6():
    """correctly identifies sequences/6.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/6.txt").stdout("Luna\n").stdout(check50.EOF).exit(0)

@check50.check(exists)
def test7():
    """correctly identifies sequences/7.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/7.txt").stdout("Ron\n").stdout(check50.EOF).exit(0)

@check50.check(exists)
def test8():
    """correctly identifies sequences/8.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/8.txt").stdout("Ginny\n").stdout(check50.EOF).exit(0)

@check50.check(exists)
def test9():
    """correctly identifies sequences/9.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/9.txt").stdout("Draco\n").stdout(check50.EOF).exit(0)

@check50.check(exists)
def test10():
    """correctly identifies sequences/10.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/10.txt").stdout("Albus\n").stdout(check50.EOF).exit(0)

@check50.check(exists)
def test11():
    """correctly identifies sequences/11.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/11.txt").stdout("Hermione\n").stdout(check50.EOF).exit(0)

@check50.check(exists)
def test12():
    """correctly identifies sequences/12.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/12.txt").stdout("Lily\n").stdout(check50.EOF).exit(0)

@check50.check(exists)
def test13():
    """correctly identifies sequences/13.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/13.txt").stdout("[Nn]o [Mm]atch\n", "No match\n").stdout(check50.EOF).exit(0)

@check50.check(exists)
def test14():
    """correctly identifies sequences/14.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/14.txt").stdout("Severus\n").stdout(check50.EOF).exit(0)

@check50.check(exists)
def test15():
    """correctly identifies sequences/15.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/15.txt").stdout("Sirius\n").stdout(check50.EOF).exit(0)

@check50.check(exists)
def test16():
    """correctly identifies sequences/16.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/16.txt").stdout("[Nn]o [Mm]atch\n", "No match\n").stdout(check50.EOF).exit(0)

@check50.check(exists)
def test17():
    """correctly identifies sequences/17.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/17.txt").stdout("Harry\n").stdout(check50.EOF).exit(0)

@check50.check(exists)
def test18():
    """correctly identifies sequences/18.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/18.txt").stdout("[Nn]o [Mm]atch\n", "No match\n").stdout(check50.EOF).exit(0)

@check50.check(exists)
def test19():
    """correctly identifies sequences/19.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/19.txt").stdout("Fred\n").stdout(check50.EOF).exit(0)

@check50.check(exists)
def test20():
    """correctly identifies sequences/20.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/20.txt").stdout("[Nn]o [Mm]atch\n", "No match\n").stdout(check50.EOF).exit(0)

