import collections

with open("day5.txt") as f:
  lines = f.read().rstrip().split("\n")
  split = lines.index("")
  stack_lines = lines[:split]
  instructions = lines[split+1:]

  stacks = collections.defaultdict(list)
  for i, k in enumerate(stack_lines[-1].split()):
    col = i*4 + 1
    for line in reversed(stack_lines[:-1]):
      if line[col] != ' ':
        stacks[k].append(line[col])

  for l in instructions:
    parts = l.split(" ")
    count = int(parts[1])
    src = parts[3]
    to = parts[5]

    stacks[to] += reversed(stacks[src][-count:])  # part 1
    # stacks[to] += stacks[src][-count:]  # part 2
    stacks[src] = stacks[src][:-count]

  print("".join(s[-1] for s in stacks.values()))