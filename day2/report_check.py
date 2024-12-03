import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE: python -m report_check FILENAME")
        exit(-1)

    with open(sys.argv[1], "r") as f:
        raw_data = f.read()

        safe_reports = []
        for l in raw_data.split("\n"):
            if not l:
                continue
            report = [int(x) for x in l.split(" ")]
            is_safe = True
            last_direction = None
            for idx, n in enumerate(report):
                if idx == len(report)-1:
                    break
                diff = n - report[idx+1]
                max_diff = bool(1 <= abs(diff) <= 3)
                if not max_diff:
                    print(f"{l} is UNSAFE because the adjacent diff is {diff} for {n} and {report[idx+1]}")
                    is_safe = False
                    break
                direction = "up" if diff > 0 else "down"
                same_dir = last_direction is None or (last_direction is not None and last_direction == direction)
                if not same_dir:
                    print(f"{l} is UNSAFE because the direction changed {last_direction} -> {direction}")
                    is_safe = False
                    break
                last_direction = direction

            if is_safe:
                print(f"{l} is SAFE")
                safe_reports.append(report)

    print(len(safe_reports))
