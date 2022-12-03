
with open("day3.txt") as f:
    group = []
    counter = 0
    for line in f:
        group.append(set(line.strip()))
        if len(group) == 3:
            for alphebet in group[0]:
                if alphebet in group[1] and alphebet in group[2]:
                    if ord(alphebet) >= 96:
                        score = ord(alphebet) - 96
                    else:
                        score = ord(alphebet) - 38
                    # print(alphebet, score)
                    counter += score
            group = []
    print(counter)
        