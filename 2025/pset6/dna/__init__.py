import check50
import random

@check50.check()
def exists():
    """dna.py exists"""
    check50.exists("dna.py")
    check50.include("generate_dynamic_test.py")
    check50.include("sequences", "databases")

@check50.check(exists)
def test1():
    """correctly identifies sequences/1.txt"""
    check50.run("python3 dna.py databases/small.csv sequences/1.txt").stdout("^Bob", "Bob\n", timeout=5).exit()

@check50.check(exists)
def test2():
    """correctly identifies sequences/2.txt"""
    check50.run("python3 dna.py databases/small.csv sequences/2.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

@check50.check(exists)
def test3():
    """correctly identifies sequences/3.txt"""
    check50.run("python3 dna.py databases/small.csv sequences/3.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

@check50.check(exists)
def test4():
    """correctly identifies sequences/4.txt"""
    check50.run("python3 dna.py databases/small.csv sequences/4.txt").stdout("^Alice", "Alice\n", timeout=5).exit()

@check50.check(exists)
def test5():
    """correctly identifies sequences/5.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/5.txt").stdout("^Lavender", "Lavender\n", timeout=5).exit()

@check50.check(exists)
def test6():
    """correctly identifies sequences/6.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/6.txt").stdout("^Luna", "Luna\n", timeout=5).exit()

@check50.check(exists)
def test7():
    """correctly identifies sequences/7.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/7.txt").stdout("^Ron", "Ron\n", timeout=5).exit()

@check50.check(exists)
def test8():
    """correctly identifies sequences/8.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/8.txt").stdout("^Ginny", "Ginny\n", timeout=5).exit()

@check50.check(exists)
def test9():
    """correctly identifies sequences/9.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/9.txt").stdout("^Draco", "Draco\n", timeout=5).exit()

@check50.check(exists)
def test10():
    """correctly identifies sequences/10.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/10.txt").stdout("^Albus", "Albus\n", timeout=5).exit()

@check50.check(exists)
def test11():
    """correctly identifies sequences/11.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/11.txt").stdout("^Hermione", "Hermione\n", timeout=5).exit()

@check50.check(exists)
def test12():
    """correctly identifies sequences/12.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/12.txt").stdout("^Lily", "Lily\n", timeout=5).exit()

@check50.check(exists)
def test13():
    """correctly identifies sequences/13.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/13.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

@check50.check(exists)
def test14():
    """correctly identifies sequences/14.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/14.txt").stdout("^Severus", "Severus\n", timeout=5).exit()

@check50.check(exists)
def test15():
    """correctly identifies sequences/15.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/15.txt").stdout("^Sirius", "Sirius\n", timeout=5).exit()

@check50.check(exists)
def test16():
    """correctly identifies sequences/16.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/16.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

@check50.check(exists)
def test17():
    """correctly identifies sequences/17.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/17.txt").stdout("^Harry", "Harry\n", timeout=5).exit()

@check50.check(exists)
def test18():
    """correctly identifies sequences/18.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/18.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

@check50.check(exists)
def test19():
    """correctly identifies sequences/19.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/19.txt").stdout("^Fred", "Fred\n", timeout=5).exit()

@check50.check(exists)
def test20():
    """correctly identifies sequences/20.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/20.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

@check50.check(exists)
def test21():
    """correctly identifies sequences/dynamic_1.txt"""
    check50.run("python3 generate_dynamic_test.py dynamic_1.csv dynamic_1.txt 1980 && python3 dna.py databases/dynamic_1.csv sequences/dynamic_1.txt").stdout("^Philosopher", "Philosopher\n", timeout=5).exit()

@check50.check(exists)
def test22():
    """correctly identifies sequences/dynamic_2.txt"""
    check50.run("python3 generate_dynamic_test.py dynamic_2.csv dynamic_2.txt 7 && python3 dna.py databases/dynamic_2.csv sequences/dynamic_2.txt").stdout("^Philosopher", "Philosopher\n", timeout=5).exit()

@check50.check(exists)
def test23():
    """correctly identifies sequences/dynamic_3.txt"""
    check50.run("python3 generate_dynamic_test.py dynamic_3.csv dynamic_3.txt 31 && python3 dna.py databases/dynamic_3.csv sequences/dynamic_3.txt").stdout("^Philosopher", "Philosopher\n", timeout=5).exit()

@check50.check(exists)
def test24():
    """correctly identifies sequences/dynamic_4.txt"""
    check50.run("python3 generate_dynamic_test.py dynamic_4.csv dynamic_4.txt 4 && python3 dna.py databases/dynamic_4.csv sequences/dynamic_4.txt").stdout("^Philosopher", "Philosopher\n", timeout=5).exit()

@check50.check(exists)
def test25():
    """correctly identifies sequences/dynamic_5.txt"""
    check50.run("python3 generate_dynamic_test.py dynamic_5.csv dynamic_5.txt 141 && python3 dna.py databases/dynamic_5.csv sequences/dynamic_5.txt").stdout("^Philosopher", "Philosopher\n", timeout=5).exit()

@check50.check(exists)
def test26():
    """correctly identifies sequences/dynamic_6.txt"""
    random_seed = random.randint(8,12)
    check50.run(f"python3 generate_dynamic_test.py dynamic_6.csv dynamic_6.txt {random_seed} && python3 dna.py databases/dynamic_6.csv sequences/dynamic_6.txt").stdout("^Philosopher", "Philosopher\n", timeout=5).exit()

@check50.check(exists)
def test27():
    """correctly identifies sequences/dynamic_7.txt"""
    random_seed = random.randint(16,20)
    check50.run(f"python3 generate_dynamic_test.py dynamic_7.csv dynamic_7.txt {random_seed} && python3 dna.py databases/dynamic_7.csv sequences/dynamic_7.txt").stdout("^Philosopher", "Philosopher\n", timeout=5).exit()

@check50.check(exists)
def test28():
    """correctly identifies sequences/dynamic_8.txt"""
    random_seed = random.randint(200,225)
    check50.run(f"python3 generate_dynamic_test.py dynamic_8.csv dynamic_8.txt {random_seed} && python3 dna.py databases/dynamic_8.csv sequences/dynamic_8.txt").stdout("^Philosopher", "Philosopher\n", timeout=5).exit()