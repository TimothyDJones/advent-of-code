import re

def main():
    sum_invalid_ids = 0

    with open("input02.txt", "r") as f:
        data = f.readline().split(",")
        ranges = [d.split("-") for d in data]

    for r in ranges:
        for v in range(int(r[0]), int(r[1]) + 1):
            vs = str(v)
            if (len(vs) % 2):
                continue
            if not (vs[:(len(vs) // 2)] == vs[(len(vs) // 2):]):
                continue
            if not bool(re.fullmatch(r"(.+)\1+", vs)):
                continue

            # print("\t", v)
            sum_invalid_ids += v

    print("Sum of invalid IDs: {i}".format(i=sum_invalid_ids))


if __name__ == "__main__":
    main()
