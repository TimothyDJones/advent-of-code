# puzzle13a.py

def main():

    (ts, buses) = read_file()

    wait_time = ts
    bus = 0

    for i in range(ts, (ts + max(buses))):
        for b in buses:
            if (i % b == 0) and (i - ts < wait_time):
                bus = b
                wait_time = i - ts

    result = (bus * wait_time)

    print("Bus ID [" + str(bus) + "] x wait time [" + str(wait_time) + \
        "]: " + str(result))

def read_file():
    
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        ts = int(lines[0])
        buses = [int(x) for x in lines[1].split(",") if x != "x"]

        return (ts, buses)

if __name__ == "__main__":
    main()