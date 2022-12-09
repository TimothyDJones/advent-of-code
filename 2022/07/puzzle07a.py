# puzzle07a.py
import string

class Tree(object):
    def __init__(self, data, children=None, parent=None):
        self.data = data
        self.children = children or []
        self.parent = parent

    def add_child(self, data):
        new_child = Tree(data, parent=self)
        self.children.append(new_child)
        return (new_child)

    def is_root(self) -> bool:
        return (self.parent is None)

    def is_leaf(self) -> bool:
        return (not self.children)

    def __str__(self) -> str:
        if self.is_leaf():
            return (self.data)
        return ("{data} [{children}]".format(data=self.data,
            children=", ".join(map(str, self.children))))

def main():
    input_file = open("input07.txt", "r")
    lines = input_file.readlines()

    num_lines = len(lines)

    for i in range(num_lines):
        line = lines[i].strip()
        if line[0:4] in ["$ cd"]:
            dir_name


    print("Characters before first start-of-packet marker: {n}\n".format(n=char))
    # Answer: 1909

if __name__ == "__main__":
    main()
