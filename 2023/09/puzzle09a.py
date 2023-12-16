# puzzle09a.py
from pprint import pformat

def parse_data():
    input_file = open("input09.txt", "r")
    # input_file = open("test.txt", "r")
    data = input_file.readlines()
    
    data_map = [line.strip().split() for line in data]
    data_map = [[int(item) for item in row] for row in data_map]

    # print("{d}".format(d=pformat(object=data_map, indent=2)))
    
    return (data_map[14:15]) 

def main():
    data = parse_data()
    
    history_next_values = list()
    
    for row in data:
        sequences = list()
        sequences.append(row)
        curr_seq = row
        next_seq = list()
        while True:
            for i in range(1, len(curr_seq)):
                next_seq.append((curr_seq[i] - curr_seq[i - 1]))
            sequences.append(next_seq)
            # print(sequences)
            # if not i%5:
            #    input()
            # When all values of sequence are "0", break out of loop.
            if not sum(next_seq):
                break
            curr_seq = next_seq
            next_seq = list()
            
        # Work up from bottom of list of sequences and append 
        # new value by adding value from end of subsequent sequence.
        prev_last_value = 0
        for i in range(len(sequences) - 1, -1, -1):
            if i == len(sequences) - 1:
                prev_last_value = sequences[i][-1]
            else:
                prev_last_value += sequences[i][-1]
            print(sequences[i], prev_last_value)
                
        history_next_values.append(prev_last_value)
    
    print(history_next_values)
    
    print("Sum of extrapolated values for all sequences: {n}\n".format(n=sum(history_next_values)))
    # Answer: 18673

if __name__ == "__main__":
    main()