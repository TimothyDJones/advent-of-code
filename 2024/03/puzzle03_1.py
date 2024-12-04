import re

def main():
    _sum = 0

    with open("input03.txt", "r") as f:
        line = f.readline()
        nums = re.findall(r"mul\((\d+,\d+)\)", line)
        for n in nums:
            a, b = n.split(",")
            _sum += int(a) * int(b)

    print("Sum of `mul(a,b)` entries: {s}".format(s=_sum))
    
    
if __name__ == "__main__":
    main()