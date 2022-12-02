
with open("day2.txt") as f:
  counter = 0
  for line in f:
    theirs = ord(line[0]) - ord('A')
    mine = ord(line[2]) - ord('X')

    if (mine - theirs) in [1, -2]:
      counter += 6
    elif theirs == mine:
      counter += 3
    else:
      counter += 0
    counter += mine + 1
  print(counter)
