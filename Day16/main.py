rules = dict()
my_ticket = list()
nearby_tickets = list()

part=1
with open("input.txt", "r") as f:
	for line in f:
		if line.strip(" \n") == "":
			f.readline()
			part+=1
			continue
		if part == 1:
			field_name = line.strip(" \n").split(": ")[0]
			ranges = line.strip(" \n").split(": ")[1].split(" or ")
			rules[field_name] = set(range(int(ranges[0].split("-")[0]), 1+int(ranges[0].split("-")[1])))
			rules[field_name].update(range(int(ranges[1].split("-")[0]), 1+int(ranges[1].split("-")[1])))
		elif part == 2:
			my_ticket = [int(x) for x in line.strip(" \n").split(",")]
		else:
			nearby_tickets.append(list(int(x) for x in line.strip(" \n").split(",")))
	
all_possible_numbers = set()
for field in rules:
	for x in rules[field]:
		all_possible_numbers.add(x)
	
valid_tickets = list()

error_scanning_rate = 0
for x in nearby_tickets:
	valid = True
	for y in x:
		if not y in all_possible_numbers:
			error_scanning_rate += y
			valid = False
	if valid == True:
		valid_tickets.append(x)
valid_tickets.append(my_ticket)

print(f"Error scanning rate: {error_scanning_rate}")

poss_indexes = dict()
for key_name in rules:
	poss_indexes[key_name] = set(range(len(my_ticket)))

for ticket in valid_tickets:
	for x in range(len(ticket)):
		for r in rules:
			if not ticket[x] in rules[r]:
				poss_indexes[r].discard(x)

for i in range(5):
	for key in poss_indexes:
		if len(poss_indexes[key]) == 1:
			for key_ in poss_indexes:
				if not key==key_:
					poss_indexes[key_].discard(list(poss_indexes[key])[0])
	for key in poss_indexes:
		for x in poss_indexes[key]:
			unique = True
			for key_ in poss_indexes:
				if not key==key_:
					if x in poss_indexes[key_]:
						unique = False
						break
			if unique == True:
				poss_indexes[key] = set([x])

print(poss_indexes)

res=1
for key_name in poss_indexes:
	if key_name[0:9] == "departure":
		res *= my_ticket[ max(poss_indexes[key_name]) ]

print(f"Result: {res}")