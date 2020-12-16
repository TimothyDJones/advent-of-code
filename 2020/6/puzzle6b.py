# puzzle6b.py

def main():
    custom_form_total = 0

    input_file = open("input.txt", "r")
    lines = input_file.readlines()

    form_set = set()
    loop_count = 0
    for line in lines:
        if len(line.rstrip("\n")) > 0:
            if loop_count == 0:
                form_set = set(line.rstrip("\n"))
            else:
                form_set = set(line.rstrip("\n")).intersection(form_set)
            loop_count += 1
        else:
            custom_form_total += len(set(form_set))
            form_set = set()
            loop_count = 0

    print("Custom form count total: " + str(custom_form_total))

def calc_form(_str):
    return len(set(_str))

if __name__ == "__main__":
    main()