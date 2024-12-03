import sys
from typing import Any, Tuple, List

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


def findall(needle: Any, haystack: List[Any]) -> List[int]:
    indicies = []    

    try:
        idx = haystack.index(needle)
    except ValueError:
        idx = None

    while idx is not None:
        indicies.append(idx)
        try:
            idx = haystack.index(needle, idx+1)
        except ValueError:
            idx = None

    return indicies


def similarity_score(lft: List[int], rgt: List[int]) -> int:
    count_score = []
    for l in lft:
        indicies = findall(l, rgt)
        score = len(indicies) * l
        print(f"Item: {l}, Right Indicies: {indicies}, Score: {score}")
        count_score.append(score)

    return sum(count_score)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE: python -m sim_score FILE_NAME")
        exit(-1)

    left_list, right_list = parse_data(sys.argv[1])

    score = similarity_score(left_list, right_list)
    print(score)

