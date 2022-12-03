
with open("day3.txt") as f:
    counter = 0
    for line in f:
        line = line.strip()
        length = len(line)
        bag1 = set(line[0:length//2])
        bag2 = set(line[length//2:length])

        # print(bag1, bag2)
        alphebet = 0
        for alphebet in bag1:
            if alphebet in bag2:
                if ord(alphebet) >= 96:
                    score = ord(alphebet) - 96
                else:
                    score = ord(alphebet) - 38
                # print(alphebet, score)
                counter += score

    print(counter)