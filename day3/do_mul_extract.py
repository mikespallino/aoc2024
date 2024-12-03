import re
import sys

MUL = re.compile(r"(mul\((\d+),(\d+)\)|(don\'t\(\))|(do\(\)))")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE: python -m do_mul_extract FILENAME")
        exit(-1)

    with open(sys.argv[1], "r") as f:
        raw_data = f.read()
        
        instructions = MUL.findall(raw_data)

        total = 0
        should_mul = True
        for instruction in instructions:
            full_ins = instruction[0]
            if full_ins == "don't()":
                should_mul = False
            if full_ins == "do()":
                should_mul = True

            if should_mul and full_ins.startswith("mul"):            
                total += (int(instruction[1]) * int(instruction[2]))
        print(total)
