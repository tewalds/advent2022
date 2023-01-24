
import functools
import itertools
import json

def cmp(a, b):
	# print(a, b)
	if isinstance(a, int) and isinstance(b, int):
		if a == b:
			return 0
		return -1 if a < b else 1
	if isinstance(a, list) and isinstance(b, list):
		for a, b in itertools.zip_longest(a, b):
			# print("  ", a, b)
			if a is None:
				return -1
			if b is None:
				return 1
			outcome = cmp(a, b)
			if outcome != 0:
				return outcome
		return 0
	if isinstance(a, int):
		return cmp([a], b)
	if isinstance(b, int):
		return cmp(a, [b])
	assert False, (a, b)


# with open("day13small.txt") as f:
with open("day13.txt") as f:
	lines = [json.loads(l) for l in f.readlines() if l != "\n"]

	total = 0
	for i in range(len(lines) // 2):
		a = lines[i * 2]
		b = lines[i * 2 + 1]
		outcome = cmp(a, b)
		print(i, outcome, a, b)
		if outcome < 0:
			total += i + 1
	print(total)

	lines.append([[2]])
	lines.append([[6]])

	correct = sorted(lines, key=functools.cmp_to_key(cmp))
	for l in correct:
		print(l)
	print((correct.index([[2]]) + 1) * (correct.index([[6]]) + 1))

