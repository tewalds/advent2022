
with open("day2.txt") as f:
  counter = 0
  for line in f:
    theirs = ord(line[0]) - ord('A')
    outcome = ord(line[2]) - ord('X')

    if outcome == 2:
      counter += 6
      mine = (theirs + 1) % 3
    elif outcome == 1:
      counter += 3
      mine = theirs
    else:
      counter += 0
      mine = (theirs + 2) % 3
    counter += mine + 1
  print(counter)
