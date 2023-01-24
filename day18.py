# with open("day18tiny.txt") as f:
# with open("day18small.txt") as f:
with open("day18.txt") as f:
	rock = set()
	max_x = 0
	max_y = 0
	max_z = 0
	for line in f:
		coord = tuple(map(int, line.strip().split(",")))
		max_x = max(max_x, coord[0] + 1)
		max_y = max(max_y, coord[1] + 1)
		max_z = max(max_z, coord[2] + 1)
		rock.add(coord)

	water = set()
	flood = set()
	flood.add((-1, -1, -1))

	def add(x, y, z):
		if (-1 <= x <= max_x and -1 <= y <= max_y and 0 <= z <= max_z and
			(x, y, z) not in water and (x, y, z) not in rock):
			flood.add((x, y, z))

	while flood:
		x, y, z = flood.pop()
		water.add((x, y, z))
		add(x+1, y, z)
		add(x-1, y, z)
		add(x, y+1, z)
		add(x, y-1, z)
		add(x, y, z+1)
		add(x, y, z-1)


	total_water_area = 0
	total_surf_area = 0
	for x, y, z in sorted(rock):
		water_area = (
			((x+1, y, z) in water) +
			((x-1, y, z) in water) +
			((x, y+1, z) in water) +
			((x, y-1, z) in water) +
			((x, y, z+1) in water) +
			((x, y, z-1) in water)
		)
		surf_area = (
			((x+1, y, z) not in rock) +
			((x-1, y, z) not in rock) +
			((x, y+1, z) not in rock) +
			((x, y-1, z) not in rock) +
			((x, y, z+1) not in rock) +
			((x, y, z-1) not in rock)
		)
		total_surf_area += surf_area
		total_water_area += water_area

	print(total_surf_area, total_water_area)