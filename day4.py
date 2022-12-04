
with open("day4.txt") as f:

    counter = 0
    
    for line in f:
        line = line.strip()
        group = line.split(",")
        a_min, a_max = map(int, group[0].split("-"))
        b_min, b_max = map(int, group[1].split("-"))

        if b_min <= a_max and b_max >= a_max:
            counter += 1
        elif a_min <= b_max and a_max >= b_max:
            counter += 1

        print(counter)