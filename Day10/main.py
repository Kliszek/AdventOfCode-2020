adapters = set()

with open("input.txt", "r") as f:
	for line in f:
		adapters.add( int(line.strip(" \n")) )

print(len(adapters))

current = 0
diff_1=0
diff_3=1
for x in range(0,99):
	if current+1 in adapters:
		diff_1+=1
		current+=1
	elif current+2 in adapters:
		current+=2
	elif current+3 in adapters:
		diff_3+=1
		current+=3
	else:
		print("error")
		break
print(f"Answer: {diff_1*diff_3}")
print(max(adapters))

max_jolts = max(adapters)

#combinations = 0
saved = dict()

def count(n):
	if n == max_jolts:
		return 1
	if n in saved:
		return saved[n]

	combinations=0
	if n+1 in adapters:
		combinations += count(n+1)
	if n+2 in adapters:
		combinations += count(n+2)
	if n+3 in adapters:
		combinations += count(n+3)
	saved[n] = combinations
	return combinations


result = count(0)

print(f"There are {result} possibilities")