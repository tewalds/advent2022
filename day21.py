# with open("day21small.txt") as f:
with open("day21.txt") as f:

	rules = {}
	for line in f:
		name, rule = line.strip().split(": ", 1)
		rules[name] = rule

	def compute(name):
		rule = rules[name]
		if " " in rule:
			a, op, b = rule.split(" ")
			a, ha = compute(a)
			b, hb = compute(b)
			if op == "+": return a + b, ha or hb
			if op == "-": return a - b, ha or hb
			if op == "*": return a * b, ha or hb
			if op == "/": return a / b, ha or hb
			assert False, rule
		return int(rule), (name == "humn")

	root, _ = compute("root")
	print("root", root)

	a, b = rules["root"].split(" + ")

	aout, ha = compute(a)
	bout, hb = compute(b)

	print(aout, bout)

	def inverse(name, goal):
		rule = rules[name]
		if " " in rule:
			a, op, b = rule.split(" ")
			va, ha = compute(a)
			vb, hb = compute(b)
			assert ha != hb, name
			n, v = (a, vb) if ha else (b, va)
			if op == "+": return inverse(n, goal - v)
			if op == "-": return inverse(n, goal + v)
			if op == "*": return inverse(n, goal / v)
			if op == "/": return inverse(n, goal * v)
			assert False, rule
		return goal

	human = inverse(a, -bout)
	print("human", human)

	rules["humn"] = str(int(human))
	aout, ha = compute(a)
	bout, hb = compute(b)
	print(aout == bout, aout, bout, aout / bout)
