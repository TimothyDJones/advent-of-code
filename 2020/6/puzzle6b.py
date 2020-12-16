# puzzle6b.py

def main():
    custom_form_total = 0

    input_file = open("input.txt", "r")
    lines = input_file.readlines()

    form_list = []
    for line in lines:
        if len(line.rstrip("\n")) > 0:
            form_list.append(line.rstrip("\n"))
        else:
            common = set.intersection(*[set(form) for form in form_list])
            custom_form_total += len(common)
            form_list = []

    print("Custom form count total: " + str(custom_form_total))

if __name__ == "__main__":
    main()