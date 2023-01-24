
import re

def dist(ax, ay, bx, by):
	return abs(ax - bx) + abs(ay - by)	

# with open("day15small.txt") as f:
with open("day15.txt") as f:
	min_x = 0
	min_y = 0
	# max_x = 20
	# max_y = 20
	max_x = 4000000
	max_y = 4000000
	# min_x = 2**30
	# min_y = 2**30
	# max_x = -2**30
	# max_y = -2**30

	sensors = {}
	for line in f:
		sx, sy, bx, by = map(int, re.findall(r"(\-?\d+)", line))
		d = dist(sx, sy, bx, by)
		sensors[(sx, sy)] = (bx, by, d)
		# min_x = min(min_x, sx-d, bx-d)
		# min_y = min(min_y, sy-d, by-d)
		# max_x = max(max_x, sx+d, bx+d)
		# max_y = max(max_y, sy+d, by+d)

	print((min_x, min_y), (max_x, max_y))


	count = 0
	for y in range(min_y, max_y+1):
		ranges = []
		for (sx, sy), (bx, by, d) in sensors.items():
			w = d - abs(y - sy)
			if w > 0:
				ranges.append((sx - w, sx + w))
		ranges.sort()
		# print(y, ranges)
		cur = min_x
		for l, r in ranges:
			if cur + 1 < l:
				print(y, cur+1, (cur+1) * 4000000 + y)
			cur = max(cur, r)

	# for y in range(min_y, max_y+1):
	# 	print(f"{y:3} ", end="")
	# 	for x in range(min_x, max_x+1):
	# 		found = None
	# 		for i, ((sx, sy), (bx, by, d)) in enumerate(sensors.items()):
	# 			if (x, y) == (sx, sy):
	# 				found = chr(ord("A") + i)
	# 				break
	# 			elif (x, y) == (bx, by):
	# 				found = "@"
	# 				break
	# 			elif dist(x, y, sx, sy) <= d:
	# 				if found is None:
	# 					found = chr(ord("a") + i)
	# 		if found is None:
	# 			found = "."
	# 		print(found, end="")
	# 	print()