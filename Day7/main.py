rules = list()
bags = dict()
bags_reverse = dict()

with open("input.txt", "r") as f:
	for line in f:
		rules.append(line.strip(". \n").split(" "))

for entry in range(len(rules)):
	outer = f"{rules[entry][0]} {rules[entry][1]}"

	kinds = (len(rules[entry])-4)//4
	inner = set()

	for b in range(4, 4+kinds*4, 4):
		inner.add((f"{rules[entry][b+1]} {rules[entry][b+2]}", int(rules[entry][b])))
	
	bags[outer]=inner
	for x in inner:
		if x[0] in bags_reverse:
			bags_reverse[x[0]].append(outer)
		else:
			bags_reverse[x[0]] = [outer]

res1 = set()
res2 = 0

def count1(name):
	global res1
	global bags_reverse
	if name in bags_reverse:
		res1.update(bags_reverse[name])
		for x in bags_reverse[name]:
			count1(x)

def count2(name):
	global res2
	global bags
	rec = 1
	for x in bags[name]:
		rec += x[1] * count2(x[0])
	return rec


print(bags_reverse["shiny gold"])
count1("shiny gold")
print(len(res1))

print(count2("shiny gold")-1)