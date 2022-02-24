sum = 0
group = set()
alphabet = "abcdefghijklmnopqrstuvwxyz"
with open("input.txt", "r") as f:
		for line in f:
				if line.strip(" \n") == "":
						sum += 26-len(group)
						group = set()
				else:
						for x in alphabet:
							  if not x in line.strip(" \n"):
								    group.add(x)
		if len(group) > 0:
				sum += 26-len(group)
print(sum)