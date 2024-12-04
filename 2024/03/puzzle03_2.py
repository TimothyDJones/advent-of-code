import re

def main():
    _sum = 0

    with open("input03.txt", "r") as f:
        line = f.readline()
        sections = re.findall(r"(do\(\).*?don't\(\))", line)
        for section in sections:
            _sum += calc_section(section)

    print("Sum of `mul(a,b)` entries in `do()/don't()` sections: {s}".format(s=_sum))
    
    
def calc_section(data):
    _sum = 0

    nums = re.findall(r"mul\((\d+,\d+)\)", data)
    for n in nums:
        a, b = n.split(",")
        _sum += int(a) * int(b)

    return _sum
    
    
if __name__ == "__main__":
    main()