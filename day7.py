import pathlib
import pprint

def flatten(tree: dict, prefix: pathlib.PurePath):
  total = 0
  sizes = {}
  for k, v in tree.items():
    if isinstance(v, dict):
      dir_size, dir_sizes = flatten(v, prefix / k)
      total += dir_size
      sizes.update(dir_sizes)
    else:
      total += v
  sizes[str(prefix)] = total
  return total, sizes

with open("day7.txt") as f:
  path = pathlib.PurePath("/")
  tree = {}
  subtree = tree
  for line in f:
    line = line.strip()
    if line == "$ cd /":
      pass
    elif line == "$ cd ..":
      path = path.parent
      subtree = tree
      for p in path.parts[1:]:
        subtree = subtree[p]
    elif line.startswith("$ cd "):
      subdir = line[5:]
      path = path.joinpath(subdir)
      if subdir not in subtree:
        subtree[subdir] = {}
      subtree = subtree[subdir]
    elif line == "$ ls":
      pass
    elif line.startswith("dir "):
      pass
    else:
      size, name = line.split(" ")
      subtree[name] = int(size)
  pprint.pprint(tree)
  total, large = flatten(tree, pathlib.PurePath("/"))
  pprint.pprint(large)
  pprint.pprint(sorted(large.items(), key=lambda p: p[1]))
  print("total:", total)
  print("free:", 70000000 - total)
  needed = 30000000 - (70000000 - total)
  print("needed:", needed)
  print(sum(v for v in large.values() if v <= 100000))
  print(min(v for v in large.values() if v >= needed))