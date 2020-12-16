# puzzle6a.py

def main():
    customs_forms = read_file()

    custom_form_total = 0
    for form in customs_forms:
        custom_form_total += calc_form(form)

    print("Custom form count total: " + str(custom_form_total))

def calc_form(_str):
    return len(set(_str))
            
def read_file():
    input_file = open("input.txt", "r")
    lines = input_file.readlines()

    new_lines = []
    new_lines.append("")
    new_lines_index = 0
    for line in lines:
        if len(line.rstrip("\n")) > 0:
            new_lines[new_lines_index] += line.rstrip("\n")
        else:
            new_lines[new_lines_index] = new_lines[new_lines_index].strip()
            new_lines_index += 1
            new_lines.append("")

    return new_lines

if __name__ == "__main__":
    main()