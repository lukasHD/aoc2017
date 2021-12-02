import sys
import inspect
from codetiming import Timer
sys.path.insert(0, '/home/lukas/aoc2017')
from helper import loadingUtils, pretty

DAY = -1
def get_path():
    return "day{:02d}".format(DAY)

@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    # code here
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    # code here
    print("Result = {}".format(result))
    return result

def part1():
    run_part_1(get_path() + "/input")

def part2():
    run_part_2(get_path() + "/input")


if __name__ == "__main__":
    run_part_1(get_path() + "/test", True)
    run_part_1(get_path() + "/input")
    run_part_2(get_path() + "/test", True)
    run_part_2(get_path() + "/input")
