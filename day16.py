
import dataclasses
import re

@dataclasses.dataclass
class Position:
	name: str
	flow: int
	tunnels: list[str]

with open("day16small.txt") as f:
	positions = {}
	for line in f:
		parts = re.findall(r"Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.+)", line)
		if parts:
			pos, flow, tunnels = parts[0]
			positions[pos] = Position(pos, int(flow), tunnels.split(", "))
			print(positions[pos])
	
	