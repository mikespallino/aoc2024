import sys
from typing import Tuple, List

def parse_data(file_name: str) -> Tuple[List[int], List[int]]:
    with open(file_name, "r") as f:
        raw = f.read()
        left_list = []
        right_list = []
        for l in raw.split("\n"):
            if not l:
                continue
            lft, rgt = l.split("   ")
            left_list.append(int(lft))
            right_list.append(int(rgt))

        return left_list, right_list


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE: python -m diff_list.py FILE_NAME")
        exit(-1)

    left_list, right_list = parse_data(sys.argv[1])

    left_list = sorted(left_list)
    right_list = sorted(right_list)

    differences = []
    for lft, rgt in zip(left_list, right_list):
        differences.append(abs(lft-rgt))

    print(sum(differences))

