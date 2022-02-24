instructions = []
accumulator = 0
with open("input.txt", "r") as f:
	for line in f:
		instructions.append(line.strip(" \n").split(" "))
		instructions[-1].append(0)

change = {"nop":"jmp", "jmp":"nop", "acc":"acc"}
for x in range(len(instructions)):
	instructions[x][0] = change[instructions[x][0]]
	
	accumulator = 0
	index = 0
	for y in range(len(instructions)):
		instructions[y][2] = 0

	while index < len(instructions):
		if instructions[index][2] == 1:
			break

		if instructions[index][0] == "nop":
			instructions[index][2] = 1
			index += 1
		elif instructions[index][0] == "acc":
			accumulator += int(instructions[index][1])
			instructions[index][2] = 1
			index += 1
		elif instructions[index][0] == "jmp":
			instructions[index][2] = 1
			index += int(instructions[index][1])
	else:
		print(f"Accumulator: {accumulator}")
		break
	instructions[x][0] = change[instructions[x][0]]
