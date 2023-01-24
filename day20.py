with open("day20small.txt") as f:
# with open("day20.txt") as f:
	inputs = [int(l) for l in f]
	outputs = inputs[:]

	print(inputs)
	for value in inputs:
		i = outputs.index(value)
		new_i = (i + value) % (len(inputs)-1)
		print(f"{value} moves from {i} to {new_i}, between {outputs[new_i]} and {outputs[new_i+1]}")
		outputs.pop(i)
		outputs.insert(new_i, value)
		print(outputs)
