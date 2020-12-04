import os
import re
import uuid

import attr

import check50
import check50.c

@attr.s(slots=True)
class Time:
    load = attr.ib(default=0.0)
    check = attr.ib(default=0.0)
    size = attr.ib(default=0.0)
    unload = attr.ib(default=0.0)
    total = attr.ib(default=0.0)

@attr.s(slots=True)
class Memory:
    stack = attr.ib(default=0)
    heap = attr.ib(default=0)

@check50.check()
def exists():
    """dictionary.c exists"""
    check50.exists("dictionary.c")
    check50.include("Makefile", "speller.c", "dictionaries", "texts", "sols", "dictionary.h")

@check50.check(exists)
def compiles():
    """speller compiles"""
    check50.run("make").exit(0)

@check50.check(compiles, timeout=120)
def qualifies():
    """qualifies for Big Board"""
    try:
        # inject canary
        canary = str(uuid.uuid4())
        check50.run("sed -i -e 's/CANARY/{}/' speller.c".format(canary)).exit(0)
        check50.run("make -B").exit(0)

        # Run on aca.txt
        check50.c.valgrind("./speller dictionaries/large texts/aca.txt 0 > actual.out").exit(0, timeout=60)
        actual = open("actual.out").read().splitlines()
        expected = open("sols/aca.txt").read().splitlines()

        # check for canary
        if canary != actual[-1]:
            raise check50.Failure("Your Makefile doesn't seem to have compiled speller.c")
        del actual[-1]

        # Compare output line for line.
        if len(actual) != len(expected):
            raise check50.Failure("{} lines expected, not {}".format(len(expected), len(actual)))
        for actual_line, expected_line in zip(actual, expected):
            if actual_line != expected_line:
                raise check50.Failure("expected {}, not {}".format(expected_line, actual_line))

    # Clear log to avoid clutter.
    finally:
        check50._log.clear()

@check50.check(qualifies)
def benchmark():
    """passes benchmarking"""

    time = Time()

    for text in os.listdir("texts"):
        out = check50.run("./speller dictionaries/large texts/{} 1".format(text)).stdout(timeout=20)
        try:
            load, check, size, unload = map(float, out.split())
        except ValueError:
            check50.log(out)
            raise check50.Failure("program has unexpected output or runtime error",
                                  help="If your hash function is causing an integer overflow error, "
                                       "try removing -fsanitize=integer from CFLAGS in your Makefile!")
        time.load += load
        time.check += check
        time.size += size
        time.unload += unload

    time.total = sum(attr.astuple(time))

    # Memory data.
    memory = Memory()
    check50.run("valgrind --tool=massif --heap=yes --stacks=yes --massif-out-file=massif.out ./speller dictionaries/large texts/holmes.txt 1").stdout(timeout=20)

    re_heap = re.compile("mem_heap_B=(\d+)")
    re_stack = re.compile("mem_stacks_B=(\d+)")
    with open("massif.out") as f:
        for line in f:
            heap_match = re_heap.match(line)
            stack_match = re_stack.match(line)
            if heap_match:
                memory.heap = max(memory.heap, int(heap_match.groups()[0]))
            elif stack_match:
                memory.stack = max(memory.stack, int(stack_match.groups()[0]))

    check50.data(time=attr.asdict(time), memory=attr.asdict(memory))
