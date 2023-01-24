import itertools

start = (500, 0)

# with open("day14small.txt") as f:
with open("day14.txt") as f:
	blocked = {}
	for line in f:
		parts = [list(map(int, p.split(",")))
				 for p in line.strip().split(" -> ")]
		for (sx, sy), (ex, ey) in zip(parts[:-1], parts[1:]):
			sx, ex = min(sx, ex), max(sx, ex)
			sy, ey = min(sy, ey), max(sy, ey)
			for y in range(sy, ey+1):
				for x in range(sx, ex+1):
					blocked[(x, y)] = "#"

	# part 2:
	floor = max(b[1] for b in blocked) + 2
	for x in range(500 - floor - 2, 500 + floor + 2):
		blocked[(x, floor)] = "="

	min_x = min(b[0] for b in blocked)
	max_x = max(b[0] for b in blocked)
	min_y = min(0, min(b[1] for b in blocked))
	max_y = max(b[1] for b in blocked)

	def output():
		for y in range(min_y, max_y+2):
			print(f"{y:3}", end="")
			for x in range(min_x-1, max_x+2):
				if (x, y) in blocked:
					print(blocked[(x, y)], end="")
				elif (x, y) == start:
					print("+", end="")
				else:
					print(".", end="")
			print()


	output()
	for i in itertools.count():
		if i % 100 == 0:
			output()
		x, y = start
		while True:
			if y > max_y:
				break
			elif (x, y+1) not in blocked:
				y += 1
			elif (x-1, y+1) not in blocked:
				x, y = x-1, y+1
			elif (x+1, y+1) not in blocked:
				x, y = x+1, y+1
			else:
				break
		if y > max_y or y == 0:
			output()
			print(i)
			break
		else:
			blocked[(x, y)] = "o"

	print(sum(1 for b in blocked.values() if b == "o"))