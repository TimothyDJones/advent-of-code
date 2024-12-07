

def main():
    data = list()
    sum_valid = 0

    with open("input07.txt", "r") as f:
        line = f.readline()
        while line:
            data.append(line.strip())
            line = f.readline()
    
    for item in data:
        if is_valid_expression(item):
            vals = item.split(":")
            sum_valid += int(vals[0])
    
   
    print("Sum of valid target values: {s}".format(s=sum_valid))


def is_valid_expression(expression):
    """
    Check if the numbers on the right of the colon can be combined
    using + and * (left-to-right) to make the number on the left.
    """
    # Split the input into the target number and the list of numbers
    target, numbers = expression.split(":")
    target = int(target.strip())
    numbers = list(map(int, numbers.strip().split()))
    
    # Helper function to calculate left-to-right operations
    def calculate_left_to_right(nums, ops):
        result = nums[0]
        for i in range(len(ops)):
            if ops[i] == "+":
                result += nums[i + 1]
            elif ops[i] == "*":
                result *= nums[i + 1]
        return result

    # Generate all combinations of "+" and "*" for the operations
    operations = ["+", "*"]
    all_combinations = [[]]

    for _ in range(len(numbers) - 1):
        new_combinations = []
        for combo in all_combinations:
            for op in operations:
                new_combinations.append(combo + [op])
        all_combinations = new_combinations
        
    # print("all_combinations:", all_combinations)

    # Check each combination to see if it produces the target
    for ops in all_combinations:
        if calculate_left_to_right(numbers, ops) == target:
            return True

    return False
   
    
if __name__ == "__main__":
    main()