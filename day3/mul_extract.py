import re
import sys

MUL = re.compile(r"mul\((\d+),(\d+)\)")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE: python -m mul_extract FILENAME")
        exit(-1)

    with open(sys.argv[1], "r") as f:
        raw_data = f.read()
        mul_pairs = [(int(p[0]), int(p[1])) for p in MUL.findall(raw_data)]
        total = 0
        for pair in mul_pairs:
            total += (pair[0] * pair[1])
        print(total)
