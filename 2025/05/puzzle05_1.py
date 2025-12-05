

def main():
    valid_ingredients = list()
    ingr_range_list = list()
    ingr_list = list()

    with open("input05.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
        

    for item in data:
        if "-" in item:
            ingr_range_list.append(item)
        elif len(item):
            ingr_list.append(int(item))
            
    # print(ingr_range_list)
    # print(ingr_list)
            
    for ingr in ingr_list:
        if check_valid_ingredient(valid_ingr_range_list=ingr_range_list,
            test_ingr=ingr):
            valid_ingredients.append(ingr)

    # print(valid_ingredients)
    print("Number of valid ingredient IDs: {i}".format(i=len(valid_ingredients)))

def check_valid_ingredient(valid_ingr_range_list: list, test_ingr: int):
    for _range in valid_ingr_range_list:
        low, high = tuple(list(map(int, (_range.split("-")))))
        if (test_ingr >= low
            and test_ingr <= high):
            return True
            
    return False

if __name__ == "__main__":
    main()
