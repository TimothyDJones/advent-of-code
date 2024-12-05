

def main():
    data = list()
    sum_mid = 0

    with open("input05.txt", "r") as f:
        data = f.read().split("\n\n")
       
    # Parse the rules in tuple pairs.
    rules = [tuple(int(n) for n in line.split("|")) for line in data[0].splitlines()]
    # Parse the updates into list of dictionaries of page numbers and position of page.
    updates = list()
    for line in data[1].splitlines():
        items = [int(i) for i in line.split(",")]
        update = dict()
        for i in range(len(items)):
            update[items[i]] = i
        updates.append(update)
        
        
    for u in updates:
        passed = True
        for r in rules:
            # Check that:
            # (a) *Both* pages for given rule are in the update, *AND*
            # (b) Position of first page for rule is after (greater than) that of second page.
            if (r[0] in u.keys() and r[1] in u.keys()) and (u[r[0]] > u[r[1]]):
                passed = False
                break
                
        if passed:
            keys = list(u.keys())
            middle = keys[len(keys) // 2]
            sum_mid += middle
            
    
    print("Sum of middle page numbers of *CORRECTLY* ordered reports: {s}".format(s=sum_mid))
    
    
if __name__ == "__main__":
    main()